"""Módulo 2 del copiloto: plan mensual de ventas y publicaciones.

Lee el registro de consultas (entradas/) y el tarifario con dos herramientas, propone el plan del mes
con el contrato de prompts/variantes/, valida reglas duras y guarda la corrida en corridas/plan_mensual/.

Uso:
    python sistema/plan_mensual.py --mes 2026-10 --desde 2026-06-01 --hasta 2026-09-11
"""
import argparse
import hashlib
import json
import re
from datetime import date, datetime, timedelta
from pathlib import Path

import anthropic

from copiloto import (DIAS, HERRAMIENTA, PRECIOS, RAIZ, TARIFARIO, cliente, consultar_tarifario, costo,
                      fecha_consulta, leer_entrada, leer_tarifario)

ESQUEMA = json.loads((Path(__file__).parent / "esquema_plan.json").read_text(encoding="utf-8"))
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
         "octubre", "noviembre", "diciembre"]

RESUMEN = {
    "name": "resumen_consultas",
    "description": (
        "Devuelve las consultas registradas por el copiloto (entradas/) entre dos fechas: "
        "identificador, fecha, canal, notas de origen y el texto de la consulta. Las consultas sin "
        "fecha exacta se incluyen marcadas. Es la única fuente de señales de demanda."
    ),
    "strict": True,
    "input_schema": {
        "type": "object",
        "additionalProperties": False,
        "required": ["desde", "hasta"],
        "properties": {"desde": {"type": "string", "description": "AAAA-MM-DD"},
                       "hasta": {"type": "string", "description": "AAAA-MM-DD"}},
    },
}


def resumen_consultas(desde, hasta):
    d0, d1 = date.fromisoformat(desde), date.fromisoformat(hasta)
    salida = []
    for ruta in sorted((RAIZ / "entradas").rglob("*.md")):
        _, datos = leer_entrada(ruta)
        f = fecha_consulta(datos)
        if f and not (d0 <= f <= d1):
            continue
        salida.append({
            "consulta_id": datos["consulta_id"], "fecha": datos["fecha"],
            "fecha_exacta": f is not None, "canal": datos["canal"],
            "origen": datos["notas"][:220], "consulta": datos["consulta"][:500],
        })
    return {"fuente": "entradas/", "cantidad": len(salida), "consultas": salida}


def semanas(anio, mes):
    """Semanas de lunes a domingo que tocan el mes, como texto para el prompt."""
    d = date(anio, mes, 1)
    inicio = d - timedelta(days=d.weekday())
    partes, n = [], 1
    while inicio.month <= mes and inicio.year == anio or inicio < d:
        fin = inicio + timedelta(days=6)
        partes.append(f"semana {n}: {DIAS[0]} {inicio.day}/{inicio.month} a {DIAS[6]} {fin.day}/{fin.month}")
        inicio, n = fin + timedelta(days=1), n + 1
        if inicio.month != mes:
            break
    return "; ".join(partes)


def correr(modelo, system, user):
    api = cliente()
    mensajes = [{"role": "user", "content": user}]
    params = {"model": modelo, "max_tokens": 32000,
              "system": [{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
              "tools": [HERRAMIENTA, RESUMEN],
              "output_config": {"format": {"type": "json_schema", "schema": ESQUEMA}}}
    if not modelo.startswith("claude-haiku"):
        params["thinking"] = {"type": "adaptive"}
    llamadas, consumo = [], []
    for _ in range(8):
        with api.messages.stream(messages=mensajes, **params) as s:
            r = s.get_final_message()
        u = r.usage
        consumo.append({"entrada": u.input_tokens, "salida": u.output_tokens,
                        "cache_escritura": u.cache_creation_input_tokens or 0,
                        "cache_lectura": u.cache_read_input_tokens or 0, "stop_reason": r.stop_reason})
        if r.stop_reason != "tool_use":
            return json.loads(next(b.text for b in r.content if b.type == "text")), llamadas, consumo
        mensajes.append({"role": "assistant", "content": r.content})
        resultados = []
        for b in r.content:
            if b.type == "tool_use":
                res = consultar_tarifario(**b.input) if b.name == "consultar_tarifario" else resumen_consultas(**b.input)
                llamadas.append({"herramienta": b.name, "input": b.input, "cantidad": res["cantidad"]})
                resultados.append({"type": "tool_result", "tool_use_id": b.id,
                                   "content": json.dumps(res, ensure_ascii=False)})
        mensajes.append({"role": "user", "content": resultados})
    raise RuntimeError("Se alcanzó el tope de 8 vueltas sin respuesta final")


def verificar(plan, llamadas, desde, hasta):
    filas = leer_tarifario()
    ids = {c["consulta_id"] for c in resumen_consultas(desde, hasta)["consultas"]}
    chequeos = []

    def chequeo(codigo, regla, ok, detalle=""):
        chequeos.append({"codigo": codigo, "regla": regla, "ok": ok, "detalle": detalle})

    usadas = {ll["herramienta"] for ll in llamadas}
    chequeo("P1", "Consultó el registro de consultas y el tarifario", usadas == {"consultar_tarifario", "resumen_consultas"},
            ", ".join(sorted(usadas)))
    citadas = {c for s in plan["diagnostico"]["senales_de_demanda"] for c in s["consultas"]}
    chequeo("P2", "Cada señal de demanda cita consultas que existen en el registro", citadas <= ids,
            f"no existen: {sorted(citadas - ids)}" if citadas - ids else f"{len(citadas)} consulta(s) citada(s)")
    mezcla, fuera = [], []
    for i, p in enumerate(plan["publicaciones"], 1):
        texto = f"{p['pieza']} {p['foco']} {p['mensaje_clave']}"
        otro = r"Casona\s*(3|III)" if p["lista"] == "casona_2_terminados" else r"Casona\s*(2|II)\b"
        if re.search(otro, texto):
            mezcla.append(f"#{i}")
        edif = "Casona 2" if p["lista"] == "casona_2_terminados" else "Casona 3"
        permitidos = {int(f[c]) for f in filas if f["edificio"] == edif
                      for c in ("precio_lista_usd", "anticipo_usd", "cuota_mensual_usd", "saldo_contra_entrega_usd") if f[c]}
        montos = {int(m.replace(".", "")) for m in re.findall(r"USD\s*([\d.]{4,})", p["mensaje_clave"])}
        if montos - permitidos:
            fuera.append(f"#{i}: {sorted(montos - permitidos)}")
    chequeo("P3", "Cada publicación habla de una sola lista", not mezcla, "piezas que nombran la otra lista: " + ", ".join(mezcla) if mezcla else "")
    chequeo("P4", "Los montos en USD salen del tarifario de la lista de esa pieza", not fuera, "; ".join(fuera))
    no_disp = {f["unidad"] for f in filas if f["disponible"] != "si"}
    # Solo lo que se prioriza y lo que ve el público: la descripción de la pieza puede nombrar una
    # unidad para darla de baja (falso positivo de la primera corrida, ver DECISIONES).
    en_plan = json.dumps([p["unidades"] for p in plan["prioridades_de_stock"]]
                         + [p["mensaje_clave"] for p in plan["publicaciones"]], ensure_ascii=False)
    publicadas = [u for u in no_disp if re.search(re.escape(u) + r"\b", en_plan)]
    chequeo("P5", "No prioriza ni publica unidades que no están a la venta", not publicadas, ", ".join(publicadas))
    todo = json.dumps(plan["publicaciones"], ensure_ascii=False).lower()
    prohibidas = [w for w in ("descuento", "bonificaci", "últimas unidades", "última unidad", "olímpica",
                              "garantiz", "rentabilidad asegurada", "se revaloriza") if w in todo]
    chequeo("P6", "Sin descuentos, urgencia artificial ni promesas en las piezas", not prohibidas, ", ".join(prohibidas))
    return {"aprobado_para_revision": all(c["ok"] for c in chequeos), "chequeos": chequeos}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mes", required=True, help="AAAA-MM")
    ap.add_argument("--desde", required=True)
    ap.add_argument("--hasta", required=True)
    ap.add_argument("--notas", default="")
    ap.add_argument("--modelo", default="claude-opus-5", choices=sorted(PRECIOS))
    a = ap.parse_args()

    anio, mes = map(int, a.mes.split("-"))
    nombre_mes = f"{MESES[mes - 1]} {anio}"
    system = (RAIZ / "prompts" / "variantes" / "plan_mensual_system.md").read_text(encoding="utf-8")
    for anexo in ("proyecto.md", "playbook.md"):
        system += "\n\n---\n\n# ANEXO · " + (RAIZ / "conocimiento" / anexo).read_text(encoding="utf-8")
    plantilla = (RAIZ / "prompts" / "variantes" / "plan_mensual_user.md").read_text(encoding="utf-8").split("\n---\n", 1)[-1]
    user = (plantilla.replace("{mes}", nombre_mes).replace("{desde}", a.desde).replace("{hasta}", a.hasta)
            .replace("{semanas}", semanas(anio, mes)).replace("{notas}", a.notas or "(sin notas)"))
    version = hashlib.sha256((system + plantilla).encode("utf-8")).hexdigest()[:12]

    plan, llamadas, consumo, verif, error = None, [], [], None, None
    try:
        plan, llamadas, consumo = correr(a.modelo, system, user)
        verif = verificar(plan, llamadas, a.desde, a.hasta)
    except (anthropic.APIError, RuntimeError, json.JSONDecodeError, KeyError) as e:
        error = f"{type(e).__name__}: {e}"

    ahora = datetime.now()
    carpeta = RAIZ / "corridas" / "plan_mensual"
    carpeta.mkdir(parents=True, exist_ok=True)
    destino = carpeta / f"{ahora:%Y-%m-%d_%H%M}_plan-{a.mes}_{a.modelo.replace('claude-', '')}.md"
    t, usd = costo(a.modelo, consumo) if consumo else ({}, 0.0)
    L = [f"# Corrida · Plan mensual {nombre_mes} · {ahora:%d/%m/%Y %H:%M}", "",
         "| Campo | Valor |", "|---|---|", f"| Fecha de la corrida | {ahora:%Y-%m-%d %H:%M} |",
         f"| Modelo | `{a.modelo}` |", f"| Versión del contrato del módulo 2 | `{version}` |",
         f"| Tarifario (sha256) | `{hashlib.sha256(TARIFARIO.read_bytes()).hexdigest()[:12]}` |",
         f"| Resultado | {'ERROR' if error else ('aprobado para revisión' if verif['aprobado_para_revision'] else 'BLOQUEADO: corregir antes de publicar')} |",
         "", "## Entrada", "", "```markdown", user.strip(), "```", "", "## Llamadas a las herramientas", ""]
    L += [f"{i}. `{ll['herramienta']}({json.dumps(ll['input'], ensure_ascii=False)})` → {ll['cantidad']} resultado(s)"
          for i, ll in enumerate(llamadas, 1)] or ["Ninguna."]
    L += ["", "## Salida", ""]
    if error:
        L += ["```text", error, "```"]
    else:
        L += ["```json", json.dumps(plan, ensure_ascii=False, indent=2), "```", "",
              "### Calendario, tal como lo leería el equipo", "",
              "| Semana | Canal | Pieza | Lista | Técnica | Mensaje clave |", "|---|---|---|---|---|---|"]
        for p in sorted(plan["publicaciones"], key=lambda x: x["semana"]):
            L.append(f"| {p['semana']} | {p['canal']} | {p['pieza']} | {p['lista']} | {p['tecnica']} | "
                     f"{p['mensaje_clave'].replace(chr(10), ' ').replace('|', '/')} |")
        L += ["", "## Verificación automática de reglas duras", "", "| | Regla | Detalle |", "|---|---|---|"]
        L += [f"| {'✅' if c['ok'] else '❌'} {c['codigo']} | {c['regla']} | {c['detalle']} |" for c in verif["chequeos"]]
    L += ["", "## Consumo y costo", "", "| Vuelta | Entrada | Escritura caché | Lectura caché | Salida | stop_reason |",
          "|---|---|---|---|---|---|"]
    L += [f"| {i} | {c['entrada']} | {c['cache_escritura']} | {c['cache_lectura']} | {c['salida']} | {c['stop_reason']} |"
          for i, c in enumerate(consumo, 1)]
    if consumo:
        L += [f"| **Total** | **{t['entrada']}** | **{t['cache_escritura']}** | **{t['cache_lectura']}** | **{t['salida']}** | |",
              "", f"**Costo de la corrida: USD {usd:.4f}** (precios del 11/9/2026, ver `sistema/copiloto.py`)"]
    L += ["", "## Revisión humana", "", "- Revisó:", "- Qué se cambió del plan:", "- Qué se publicó:", ""]
    destino.write_text("\n".join(L), encoding="utf-8")
    print(f"Corrida guardada en {destino.relative_to(RAIZ).as_posix()} · USD {usd:.4f}")
    if error:
        print(error)
    else:
        for c in verif["chequeos"]:
            if not c["ok"]:
                print(f"  ❌ {c['codigo']} {c['regla']} — {c['detalle']}")
        print("  Resultado:", "aprobado para revisión" if verif["aprobado_para_revision"] else "BLOQUEADO")


if __name__ == "__main__":
    main()
