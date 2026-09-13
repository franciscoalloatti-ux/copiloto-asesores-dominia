"""Ejecutor del Copiloto para Asesores Comerciales de DOMINIA.

Lee una consulta de entradas/, arma el contrato (prompts/ + conocimiento/), deja que el modelo
consulte el tarifario con una herramienta, valida la ficha contra las reglas duras y guarda la
corrida completa en corridas/ (entrada, llamadas a la herramienta, salida, verificación, costo).

Uso:
    python sistema/copiloto.py entradas/consulta-01.md
    python sistema/copiloto.py entradas/consulta-01.md --modelo claude-haiku-4-5 --carpeta corridas/comparacion_modelos

La API key se toma de ANTHROPIC_API_KEY o del archivo ~/.anthropic-key. Nunca se imprime ni se guarda.
"""
import argparse
import csv
import hashlib
import json
import os
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import anthropic

RAIZ = Path(__file__).resolve().parent.parent
TARIFARIO = RAIZ / "herramientas" / "tarifario_vigente.csv"
ESQUEMA = json.loads((Path(__file__).parent / "esquema_ficha.json").read_text(encoding="utf-8"))

# Precios por millón de tokens (USD). Fuente: https://platform.claude.com/docs/en/about-claude/pricing,
# consultada el 11/9/2026. Escritura en caché (5 min) = 1,25 × entrada; lectura de caché = 0,1 × entrada.
PRECIOS = {
    "claude-opus-5": {"entrada": 5.00, "salida": 25.00},
    "claude-sonnet-5": {"entrada": 2.00, "salida": 10.00},
    "claude-haiku-4-5": {"entrada": 1.00, "salida": 5.00},
}

COLUMNAS_HERRAMIENTA = [
    "edificio", "unidad", "estado", "entrega", "dormitorios", "banos", "planta", "m2_cubiertos",
    "m2_balcon", "m2_jardin_uso_exclusivo", "m2_boleto_total", "precio_lista_usd", "usd_m2_boleto",
    "forma_de_pago", "anticipo_usd", "cuotas", "cuota_mensual_usd", "saldo_contra_entrega_usd",
    "expensas_mensuales_ars", "expensas_desde", "disponible", "observacion",
]

HERRAMIENTA = {
    "name": "consultar_tarifario",
    "description": (
        "Devuelve las unidades del tarifario vigente de Casona de los Arcos que cumplen los filtros, "
        "con precio de lista, superficies, forma de pago, expensas y disponibilidad. Es la ÚNICA "
        "fuente de precios: usala antes de nombrar cualquier unidad o precio. Los filtros en null "
        "no filtran. Por defecto solo devuelve unidades disponibles."
    ),
    "strict": True,
    "input_schema": {
        "type": "object",
        "additionalProperties": False,
        "required": ["edificio", "dormitorios", "unidad", "precio_max_usd", "incluir_no_disponibles"],
        "properties": {
            "edificio": {"type": "string", "enum": ["Casona 2", "Casona 3", "todos"],
                         "description": "Casona 2 = terminados; Casona 3 = en obra (entrega 2029)."},
            "dormitorios": {"type": ["integer", "null"], "description": "1, 2 o 3."},
            "unidad": {"type": ["string", "null"], "description": "Designación exacta, p. ej. 'PB C' o '2º F'."},
            "precio_max_usd": {"type": ["integer", "null"]},
            "incluir_no_disponibles": {"type": "boolean"},
        },
    },
}


# ---------------------------------------------------------------- herramienta

def leer_tarifario():
    with TARIFARIO.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def consultar_tarifario(edificio, dormitorios, unidad, precio_max_usd, incluir_no_disponibles):
    filas = leer_tarifario()
    norm = lambda s: s.replace("°", "º").replace(" ", "").upper()
    salida = []
    for n, fila in enumerate(filas, start=2):  # n = número de fila en el CSV (1 = encabezado)
        if edificio != "todos" and fila["edificio"] != edificio:
            continue
        if dormitorios is not None and int(fila["dormitorios"]) != dormitorios:
            continue
        if unidad and norm(fila["unidad"]) != norm(unidad):
            continue
        if precio_max_usd is not None and int(fila["precio_lista_usd"]) > precio_max_usd:
            continue
        if not incluir_no_disponibles and fila["disponible"] != "si":
            continue
        salida.append({"fila_csv": n, **{c: fila[c] for c in COLUMNAS_HERRAMIENTA}})
    return {
        "fuente": "herramientas/tarifario_vigente.csv",
        "sha256_tarifario": hashlib.sha256(TARIFARIO.read_bytes()).hexdigest()[:12],
        "listas": sorted({f"{f['edificio']}: {f['lista']} ({f['fecha_lista']})" for f in filas}),
        "cantidad": len(salida),
        "unidades": salida,
    }


# ---------------------------------------------------------------- contrato

def leer_entrada(ruta):
    """Encabezado 'clave: valor' y secciones '## Historial', '## Notas', '## Consulta'."""
    texto = Path(ruta).read_text(encoding="utf-8")
    datos = {"historial": "", "notas": "", "consulta": ""}
    encabezado, _, cuerpo = texto.partition("\n## ")
    for linea in encabezado.splitlines():
        if ":" in linea and not linea.startswith("#"):
            k, v = linea.split(":", 1)
            datos[k.strip().lower()] = v.strip()
    for bloque in ("## " + cuerpo).split("\n## "):
        titulo, _, contenido = bloque.lstrip("# ").partition("\n")
        clave = titulo.strip().lower()
        if clave in datos:
            datos[clave] = contenido.strip()
    for k in ("consulta_id", "asesor", "canal", "fecha"):
        if not datos.get(k):
            sys.exit(f"Falta '{k}' en el encabezado de {ruta}")
    return texto, datos


DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def fecha_consulta(datos):
    """La fecha de la consulta como date, o None si la entrada no la trae completa."""
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", datos["fecha"])
    return date(int(m[1]), int(m[2]), int(m[3])) if m else None


def calendario(datos):
    d = fecha_consulta(datos)
    if d is None:
        return "(no hay fecha exacta de la consulta: no propongas días con fecha, solo días de la semana)", "fecha no disponible"
    dias = [d + timedelta(days=i) for i in range(9)]
    lineas = [f"- {DIAS[x.weekday()]} {x.day}/{x.month}/{x.year}" + (" (día de la consulta)" if i == 0 else "")
              for i, x in enumerate(dias)]
    return "\n".join(lineas), DIAS[d.weekday()]


def armar_contrato(datos):
    solo_prompt = lambda p: p.read_text(encoding="utf-8").split("\n---\n", 1)[-1]
    system = (RAIZ / "prompts" / "system_prompt.md").read_text(encoding="utf-8")
    for anexo in ("proyecto.md", "playbook.md"):
        system += "\n\n---\n\n# ANEXO · " + (RAIZ / "conocimiento" / anexo).read_text(encoding="utf-8")
    plantilla = solo_prompt(RAIZ / "prompts" / "user_prompt.md")
    user = plantilla
    datos["calendario"], datos["dia_consulta"] = calendario(datos)
    for campo in ("asesor", "canal", "fecha", "dia_consulta", "consulta_id", "notas", "historial",
                  "calendario", "consulta"):
        user = user.replace("{" + campo + "}", datos.get(campo) or "(sin datos)")
    version = hashlib.sha256((system + plantilla).encode("utf-8")).hexdigest()[:12]
    return system, user, version


# ---------------------------------------------------------------- verificación de reglas duras

def verificar(ficha, datos, llamadas):
    filas = leer_tarifario()
    por_clave = {(f["edificio"], f["unidad"]): f for f in filas}
    lista = ficha["lista_asignada"]["lista"]
    edificio_lista = {"casona_2_terminados": "Casona 2", "casona_3_pozo": "Casona 3"}.get(lista)
    borrador = ficha["borrador_mensaje"]
    chequeos = []

    def chequeo(codigo, regla, ok, detalle=""):
        chequeos.append({"codigo": codigo, "regla": regla, "ok": ok, "detalle": detalle})

    chequeo("V1", "Consultó el tarifario antes de responder", len(llamadas) > 0,
            f"{len(llamadas)} llamada(s)")

    edificios = {u["edificio"] for u in ficha["unidades_propuestas"]}
    if edificio_lista:
        ok = edificios <= {edificio_lista}
    else:
        ok = not ficha["unidades_propuestas"]
    chequeo("V2", "Lista única: unidades de un solo edificio y coherentes con la lista asignada",
            ok, f"lista={lista}; edificios propuestos={sorted(edificios) or '—'}")

    malas = []
    for u in ficha["unidades_propuestas"]:
        fila = por_clave.get((u["edificio"], u["unidad"].replace("°", "º")))
        if fila is None:
            malas.append(f"{u['edificio']} {u['unidad']}: no existe en el tarifario")
        elif int(fila["precio_lista_usd"]) != u["precio_lista_usd"]:
            malas.append(f"{u['unidad']}: USD {u['precio_lista_usd']} ≠ tarifario USD {fila['precio_lista_usd']}")
        elif fila["disponible"] != "si":
            malas.append(f"{u['unidad']}: no está disponible")
    chequeo("V3", "Precios y disponibilidad idénticos al tarifario", not malas, "; ".join(malas))
    chequeo("V4", "Hasta 3 unidades propuestas", len(ficha["unidades_propuestas"]) <= 3,
            f"{len(ficha['unidades_propuestas'])} unidad(es)")

    # Montos en USD dentro del borrador: tienen que ser valores del tarifario de la lista asignada.
    montos = {int(m.replace(".", "")) for m in re.findall(r"USD\s*([\d.]{4,})", borrador)}
    permitidos = set()
    for f in filas:
        if f["edificio"] == edificio_lista:
            for c in ("precio_lista_usd", "anticipo_usd", "cuota_mensual_usd", "saldo_contra_entrega_usd"):
                if f[c]:
                    permitidos.add(int(f[c]))
    fuera = sorted(montos - permitidos)
    chequeo("V5", "Todo monto en USD del borrador sale del tarifario de la lista asignada",
            not fuera, f"montos no respaldados: {fuera}" if fuera else f"{len(montos)} monto(s)")

    # Los toques de seguimiento también le llegan al cliente: V6, V7 y V14 los leen junto con el borrador.
    al_cliente = (borrador + " " + " ".join(s["texto"] for s in ficha.get("seguimiento") or [])).lower()
    prohibidas = [p for p in ("descuento", "bonificaci", "comisi", "rebaja") if p in al_cliente]
    chequeo("V6", "El borrador y el seguimiento no mencionan descuentos ni comisiones", not prohibidas, ", ".join(prohibidas))

    promesas = [p for p in ("garantiz", "te aseguro", "sin dudas", "se revaloriza", "rentabilidad asegurada",
                            "olímpica", "semiolímpica", "seguro de caución", "fecha cierta",
                            "últimas unidades", "última unidad", "solo por hoy", "decidí hoy")
                if p in al_cliente]
    chequeo("V7", "El borrador no promete lo que no se puede cumplir ni mete urgencia artificial",
            not promesas, ", ".join(promesas))

    firma = f"{datos['asesor']}, Asesor Comercial de DOMINIA"
    chequeo("V8", "Firma exacta del asesor", borrador.rstrip().endswith(firma), f"esperada: «{firma}»")
    # Cada «día dd/mm» que aparezca en el borrador o en la propuesta de visita tiene que ser coherente.
    d0 = fecha_consulta(datos)
    texto_fechas = borrador + " " + (ficha["proximo_paso"]["propuesta_de_visita"] or "")
    pares = re.findall(r"(lunes|martes|miércoles|jueves|viernes|sábado|domingo)\s+(\d{1,2})/(\d{1,2})",
                       texto_fechas.lower())
    errados = []
    if d0:
        for dia, dd, mm in pares:
            anio = d0.year + (1 if int(mm) < d0.month else 0)
            try:
                real = DIAS[date(anio, int(mm), int(dd)).weekday()]
            except ValueError:
                real = "fecha inexistente"
            if real != dia:
                errados.append(f"«{dia} {dd}/{mm}» es {real}")
    chequeo("V12", "Días de la semana coherentes con las fechas propuestas", not errados,
            "; ".join(errados) or (f"{len(pares)} fecha(s) verificada(s)" if d0 else "sin fecha exacta de consulta"))

    primera = borrador.strip().splitlines()[0] if borrador.strip() else ""
    chequeo("V11", "El asesor se presenta en la primera línea", datos["asesor"] in primera,
            f"primera línea: «{primera[:80]}»")

    preguntas = borrador.count("?")
    chequeo("V9", "Como máximo dos preguntas", preguntas <= 2, f"{preguntas} pregunta(s)")

    palabras = len(borrador.split())
    corto = datos["canal"].lower() in ("whatsapp", "instagram")
    chequeo("V10", "Menos de 120 palabras en WhatsApp o Instagram", (palabras < 120) or not corto,
            f"{palabras} palabras · canal {datos['canal']}")

    # V13 y V14 salieron de la auditoría comercial del 12/9 (ver DECISIONES).
    # Solo cuando la visita queda acordada (restricción 8): proponer dos horarios todavía no la acuerda.
    hay_visita = ficha["camino_del_comprador"]["etapa"] == "listo_para_visita"
    b = borrador.lower()
    falta = [t for t, ok in (("la dirección", "costanera de la cañada 4140" in b),
                             ("el aviso de confirmación", "confirmo el día anterior" in b or "te confirmo" in b))
             if not ok]
    chequeo("V13", "Si la visita quedó acordada, el borrador lleva dirección y aviso de confirmación",
            not hay_visita or not falta,
            "la visita todavía no está acordada" if not hay_visita else ("falta " + " y ".join(falta) if falta else "dirección y confirmación"))

    vocabulario = [v for v in ("jardín privado", "jardin privado", "jardín propio", "patio privado",
                               "monoambiente", "pileta olímpica") if v in al_cliente]
    chequeo("V14", "Sin vocabulario que la ficha desmiente (el jardín es de uso exclusivo)",
            not vocabulario, ", ".join(vocabulario))

    # V15 salió de la iteración 9: el borrador entró en el largo y perdió la pregunta de pago (T-28).
    boton = re.search(r"me interesa .+ de casona (iii|3)\b", datos.get("consulta", "").lower())
    preguntas = re.findall(r"[^.!?\n]*\?", borrador)
    # Una pregunta que propone horario («¿el sábado a las 10…?») no cuenta aunque nombre el pago (D-22).
    pregunta_pago = any(re.search(r"pag|cuota|contado|crédito|credito|financ", q.lower())
                        and not re.search(r"a las \d", q.lower()) for q in preguntas)
    chequeo("V15", "Si la consulta vino del botón de la web, el borrador pregunta cómo paga (T-28)",
            not boton or pregunta_pago,
            "la consulta no vino del botón de la web" if not boton
            else ("pregunta por la forma de pago" if pregunta_pago else "no pregunta cómo piensa pagar"))

    return {"aprobada_para_revision": all(c["ok"] for c in chequeos), "chequeos": chequeos}


# ---------------------------------------------------------------- ejecución

def cliente():
    clave = os.environ.get("ANTHROPIC_API_KEY")
    archivo = Path.home() / ".anthropic-key"
    if not clave and archivo.exists():
        clave = archivo.read_text(encoding="utf-8").strip()
    return anthropic.Anthropic(api_key=clave) if clave else anthropic.Anthropic()


def correr(modelo, system, user):
    api = cliente()
    mensajes = [{"role": "user", "content": user}]
    params = {
        "model": modelo,
        "max_tokens": 16000,
        "system": [{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        "tools": [HERRAMIENTA],
        "output_config": {"format": {"type": "json_schema", "schema": ESQUEMA}},
    }
    if not modelo.startswith("claude-haiku"):
        params["thinking"] = {"type": "adaptive"}
    llamadas, consumo = [], []
    for _ in range(8):  # tope de vueltas: una consulta no necesita más
        r = api.messages.create(messages=mensajes, **params)
        u = r.usage
        consumo.append({
            "entrada": u.input_tokens, "salida": u.output_tokens,
            "cache_escritura": u.cache_creation_input_tokens or 0,
            "cache_lectura": u.cache_read_input_tokens or 0, "stop_reason": r.stop_reason,
        })
        if r.stop_reason == "refusal":
            raise RuntimeError(f"El modelo rechazó la consulta: {r.stop_details}")
        if r.stop_reason != "tool_use":
            texto = next(b.text for b in r.content if b.type == "text")
            return json.loads(texto), llamadas, consumo
        mensajes.append({"role": "assistant", "content": r.content})
        resultados = []
        for b in r.content:
            if b.type == "tool_use":
                resultado = consultar_tarifario(**b.input)
                llamadas.append({"input": b.input, "cantidad": resultado["cantidad"],
                                 "unidades": [f"{x['edificio']} {x['unidad']} (fila {x['fila_csv']})"
                                              for x in resultado["unidades"]]})
                resultados.append({"type": "tool_result", "tool_use_id": b.id,
                                   "content": json.dumps(resultado, ensure_ascii=False)})
        mensajes.append({"role": "user", "content": resultados})
    raise RuntimeError("Se alcanzó el tope de 8 vueltas sin respuesta final")


def costo(modelo, consumo):
    p = PRECIOS[modelo]
    t = {k: sum(c[k] for c in consumo) for k in ("entrada", "salida", "cache_escritura", "cache_lectura")}
    usd = (t["entrada"] * p["entrada"] + t["cache_escritura"] * p["entrada"] * 1.25
           + t["cache_lectura"] * p["entrada"] * 0.1 + t["salida"] * p["salida"]) / 1_000_000
    return t, usd


def guardar(carpeta, ruta_entrada, texto_entrada, datos, modelo, version, ficha, llamadas, consumo,
            verificacion, error):
    ahora = datetime.now()
    carpeta.mkdir(parents=True, exist_ok=True)
    corto = modelo.replace("claude-", "")
    destino = carpeta / f"{ahora:%Y-%m-%d_%H%M}_{datos['consulta_id']}_{corto}.md"
    t, usd = costo(modelo, consumo) if consumo else ({}, 0.0)
    L = [f"# Corrida · {datos['consulta_id']} · {ahora:%d/%m/%Y %H:%M}", "",
         "| Campo | Valor |", "|---|---|",
         f"| Fecha de la corrida | {ahora:%Y-%m-%d %H:%M} |",
         f"| Modelo | `{modelo}` |",
         f"| Versión del contrato (sha256 de system + user) | `{version}` |",
         f"| Tarifario (sha256) | `{hashlib.sha256(TARIFARIO.read_bytes()).hexdigest()[:12]}` |",
         f"| Archivo de entrada | `{Path(ruta_entrada).as_posix()}` |",
         f"| Resultado | {'ERROR' if error else ('aprobada para revisión' if verificacion['aprobada_para_revision'] else 'BLOQUEADA: corregir antes de enviar')} |",
         "", "## Entrada", "", "```markdown", texto_entrada.strip(), "```", "",
         "## Llamadas a la herramienta", ""]
    for i, ll in enumerate(llamadas, 1):
        L.append(f"{i}. `consultar_tarifario({json.dumps(ll['input'], ensure_ascii=False)})` → "
                 f"{ll['cantidad']} unidad(es): {', '.join(ll['unidades']) or '—'}")
    if not llamadas:
        L.append("Ninguna.")
    L += ["", "## Salida", ""]
    if error:
        L += ["```text", error, "```"]
    else:
        L += ["```json", json.dumps(ficha, ensure_ascii=False, indent=2), "```", "",
              "### Borrador, tal como lo vería el asesor", ""]
        L += ["> " + linea if linea else ">" for linea in ficha["borrador_mensaje"].splitlines()]
        if ficha.get("seguimiento"):
            L += ["", "### Seguimiento preparado, si no contesta", "", "| Cuándo | Aporte de valor | Texto |",
                  "|---|---|---|"]
            L += [f"| {s['cuando']} | {s['aporte_de_valor']} | {s['texto'].replace(chr(10), ' ')} |"
                  for s in ficha["seguimiento"]]
        L += ["", "## Verificación automática de reglas duras", "", "| | Regla | Detalle |", "|---|---|---|"]
        for c in verificacion["chequeos"]:
            L.append(f"| {'✅' if c['ok'] else '❌'} {c['codigo']} | {c['regla']} | {c['detalle']} |")
    L += ["", "## Consumo y costo", "", "| Vuelta | Entrada | Escritura caché | Lectura caché | Salida | stop_reason |",
          "|---|---|---|---|---|---|"]
    for i, c in enumerate(consumo, 1):
        L.append(f"| {i} | {c['entrada']} | {c['cache_escritura']} | {c['cache_lectura']} | {c['salida']} | {c['stop_reason']} |")
    if consumo:
        p = PRECIOS[modelo]
        L += [f"| **Total** | **{t['entrada']}** | **{t['cache_escritura']}** | **{t['cache_lectura']}** | **{t['salida']}** | |",
              "", f"Precio `{modelo}`: USD {p['entrada']:.2f} / MTok de entrada y USD {p['salida']:.2f} / MTok de "
              f"salida (página de precios de Anthropic, consultada el 11/9/2026). Caché: escritura 1,25×, lectura 0,1×.",
              "", f"**Costo de la corrida: USD {usd:.4f}**"]
    L += ["", "## Revisión humana", "",
          "_A completar por el asesor. Las tres últimas son las que miden si el copiloto sirve._",
          "", "- Revisó:", "- Cambios al borrador (pegar el texto que se envió de verdad):",
          "- ¿Se envió?: sí / no / se reescribió entero", "- Respuesta del interesado:",
          "- **¿Contestó?**: sí / no", "- **¿Se agendó visita?**: sí / no / todavía no",
          "- **¿Se hizo la visita?**: sí / no / reprogramada",
          "- Toques de seguimiento enviados: 48 h ☐ · 7 días ☐ · 21 días ☐", ""]
    destino.write_text("\n".join(L), encoding="utf-8")
    return destino, usd


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entrada")
    ap.add_argument("--modelo", default="claude-opus-5", choices=sorted(PRECIOS))
    ap.add_argument("--carpeta", default="corridas")
    a = ap.parse_args()

    texto, datos = leer_entrada(a.entrada)
    system, user, version = armar_contrato(datos)
    ficha, llamadas, consumo, verificacion, error = None, [], [], None, None
    try:
        ficha, llamadas, consumo = correr(a.modelo, system, user)
        verificacion = verificar(ficha, datos, llamadas)
    except (anthropic.APIError, RuntimeError, json.JSONDecodeError, KeyError) as e:
        error = f"{type(e).__name__}: {e}"
    destino, usd = guardar(RAIZ / a.carpeta, a.entrada, texto, datos, a.modelo, version, ficha, llamadas,
                           consumo, verificacion, error)
    print(f"Corrida guardada en {destino.relative_to(RAIZ).as_posix()} · USD {usd:.4f}")
    if error:
        print(error)
    else:
        for c in verificacion["chequeos"]:
            if not c["ok"]:
                print(f"  ❌ {c['codigo']} {c['regla']} — {c['detalle']}")
        print("  Resultado:", "aprobada para revisión" if verificacion["aprobada_para_revision"] else "BLOQUEADA")


if __name__ == "__main__":
    main()
