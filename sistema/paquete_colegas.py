"""Paquete mensual para inmobiliarias colegas: listas actualizadas, brochure y disponibilidad.

Se corre solo el primer día de cada mes (tarea programada de Windows «Copiloto DOMINIA - Paquete
colegas») y deja en corridas/paquete_colegas/AAAA-MM/:
  - lista_casona2.html y lista_casona3.html: las dos listas por separado, listas para imprimir a PDF
  - mensaje.md: el borrador del mensaje para los colegas, con la disponibilidad del mes
  - paquete.md: qué adjuntar, qué revisar y los chequeos
No envía nada: el asesor revisa y manda (L2). No llama a ninguna API.

Uso:
    python sistema/paquete_colegas.py                 # mes actual
    python sistema/paquete_colegas.py --mes 2026-10 --asesor Francisco --avisar
"""
import argparse
import html
import subprocess
from collections import Counter
from datetime import date, datetime
from pathlib import Path

from copiloto import RAIZ, TARIFARIO, leer_tarifario

MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
         "octubre", "noviembre", "diciembre"]
BROCHURE = "BROCHURE DOMINIA_3.pdf (29 páginas, planos tipo, amenities y terminaciones)"
DIAS_TARIFARIO_VIEJO = 35
usd = lambda n: "USD " + f"{int(n):,}".replace(",", ".")


def lista_html(edificio, filas, mes):
    """Una lista de precios por edificio, en HTML imprimible. Solo unidades disponibles."""
    c3 = edificio == "Casona 3"
    cab = ["Unidad", "Tipología", "m² cubiertos", "Balcón", "Jardín de uso exclusivo", "m² boleto", "Precio de lista"]
    cab += ["Anticipo 40 %", "30 cuotas de", "Saldo 20 %"] if c3 else ["Expensas"]
    filas_html = []
    for f in filas:
        celdas = [f["unidad"], f"{f['dormitorios']} dorm · {f['banos']} baño{'s' if f['banos'] != '1' else ''}",
                  f["m2_cubiertos"], f["m2_balcon"] if f["m2_balcon"] != "0" else "—",
                  f["m2_jardin_uso_exclusivo"] if f["m2_jardin_uso_exclusivo"] != "0" else "—",
                  f["m2_boleto_total"], usd(f["precio_lista_usd"])]
        celdas += [usd(f["anticipo_usd"]), usd(f["cuota_mensual_usd"]), usd(f["saldo_contra_entrega_usd"])] if c3 \
            else [f"$ {int(f['expensas_mensuales_ars']):,}".replace(",", ".")]
        nota = f"<tr class='nota'><td colspan='{len(cab)}'>{html.escape(f['observacion'])}</td></tr>" if f["observacion"] else ""
        filas_html.append("<tr>" + "".join(f"<td>{html.escape(str(c))}</td>" for c in celdas) + "</tr>" + nota)
    sub = ("En obra · entrega estimada 2029 · boleto de compraventa con precio en USD · 40 % de anticipo, "
           "30 cuotas (en USD o en pesos ajustados por CAC) y 20 % contra entrega · expensas desde la posesión"
           if c3 else "Terminado · entrega inmediata · contado o crédito hipotecario del comprador · todas con cochera")
    return f"""<!doctype html><meta charset="utf-8"><title>{edificio} · lista {mes}</title>
<style>body{{font:13px/1.45 system-ui,Segoe UI,sans-serif;margin:28px;color:#17201D}}h1{{font-size:20px;margin:0}}
p{{margin:4px 0 14px;color:#3E4A46}}table{{border-collapse:collapse;width:100%}}th,td{{border-bottom:1px solid #D5DCD9;padding:6px 8px;text-align:left}}
th{{font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:#66736E}}td:nth-child(n+3){{font-variant-numeric:tabular-nums}}
tr.nota td{{font-size:11px;color:#66736E;border-bottom:1px solid #BCC7C3}}footer{{margin-top:16px;font-size:11px;color:#66736E}}</style>
<h1>Casona de los Arcos · {edificio}</h1><p>{sub}</p>
<table><thead><tr>{''.join(f'<th>{c}</th>' for c in cab)}</tr></thead><tbody>{''.join(filas_html)}</tbody></table>
<footer>DOMINIA · Costanera de La Cañada 4140, Manantiales I, Córdoba · Disponibilidad al {mes} · {filas[0]['lista']} ({filas[0]['fecha_lista']}).
Precios de lista sujetos a confirmación del asesor. Las unidades vendidas o no ofrecidas no figuran.</footer>"""


def resumen(filas):
    tipos = Counter(int(f["dormitorios"]) for f in filas)
    partes = [f"{n} de {d} dormitorio{'s' if d > 1 else ''}" for d, n in sorted(tipos.items())]
    return f"{len(filas)} unidades ({', '.join(partes)}), desde {usd(min(int(f['precio_lista_usd']) for f in filas))}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mes", default=f"{date.today():%Y-%m}", help="AAAA-MM")
    ap.add_argument("--asesor", default="Francisco")
    ap.add_argument("--jornada", default="", help="Fecha y franja de la jornada para colegas, si hay")
    ap.add_argument("--avisar", action="store_true", help="Muestra un aviso en Windows cuando termina")
    a = ap.parse_args()
    anio, m = map(int, a.mes.split("-"))
    nombre_mes = f"{MESES[m - 1]} {anio}"

    filas = leer_tarifario()
    disp = {e: [f for f in filas if f["edificio"] == e and f["disponible"] == "si"] for e in ("Casona 2", "Casona 3")}
    no_ofrecidas = [f"{f['edificio']} {f['unidad']}" for f in filas if f["disponible"] != "si"]
    edad = (datetime.now() - datetime.fromtimestamp(TARIFARIO.stat().st_mtime)).days

    carpeta = RAIZ / "corridas" / "paquete_colegas" / a.mes
    carpeta.mkdir(parents=True, exist_ok=True)
    for e, archivo in (("Casona 2", "lista_casona2.html"), ("Casona 3", "lista_casona3.html")):
        (carpeta / archivo).write_text(lista_html(e, disp[e], nombre_mes), encoding="utf-8")

    jornada = (f"\nEste mes hacemos una jornada para colegas: {a.jornada}. Recorremos los edificios terminados, "
               f"los amenities y la obra de Casona 3. ¿Te anoto?\n") if a.jornada else ""
    mensaje = f"""Hola! {a.asesor}, de DOMINIA, por acá. Te paso la información actualizada de Casona de los Arcos para {nombre_mes}.

Casona 2, terminada y con entrega inmediata: {resumen(disp['Casona 2'])}. Contado o crédito hipotecario del comprador.

Casona 3, en obra con entrega estimada en 2029: {resumen(disp['Casona 3'])}. Boleto con precio en dólares: 40 % de anticipo, 30 cuotas (en dólares o en pesos ajustados por CAC) y 20 % contra entrega.

Te adjunto las dos listas por separado y el brochure. Un pedido: a cada cliente mostrale solo la lista que le corresponde según cómo va a pagar. El terminado, a quien compra con crédito o contado; el de obra, a quien necesita cuotas o busca una tipología que en terminado no hay.
{jornada}
Si querés mostrar, avisame el día y la franja y coordino. Los honorarios los hablamos aparte.

{a.asesor}, Asesor Comercial de DOMINIA"""
    (carpeta / "mensaje.md").write_text(mensaje, encoding="utf-8")

    chequeos = [
        ("K1", "La lista de precios tiene menos de 35 días", edad <= DIAS_TARIFARIO_VIEJO,
         f"el tarifario se derivó hace {edad} día(s)" + ("" if edad <= DIAS_TARIFARIO_VIEJO else
                                                          ": actualizá la planilla interna y regenerá con herramientas/derivar_tarifario.py")),
        ("K2", "Ninguna unidad no ofrecida aparece en las listas", all(u.split(" ", 2)[2] not in
         (carpeta / f"lista_casona{u.split()[1]}.html").read_text(encoding="utf-8") for u in no_ofrecidas),
         f"no ofrecidas: {', '.join(no_ofrecidas) or '—'}"),
        ("K3", "Las dos listas van en archivos separados", disp["Casona 2"] and disp["Casona 3"], "lista_casona2.html · lista_casona3.html"),
        ("K4", "El mensaje no menciona descuentos ni comisiones",
         not any(p in mensaje.lower() for p in ("descuento", "comisión", "bonificaci")), ""),
    ]
    ok = all(c[2] for c in chequeos)
    paquete = [f"# Paquete para colegas · {nombre_mes}", "",
               f"Generado el {datetime.now():%Y-%m-%d %H:%M} por `sistema/paquete_colegas.py` · tarifario `{TARIFARIO.name}`",
               f"· **{'listo para revisar y enviar' if ok else 'REVISAR ANTES DE ENVIAR'}**", "",
               "## Qué adjuntar", "",
               "1. `lista_casona2.html` → imprimir a PDF (Ctrl+P → Guardar como PDF)",
               "2. `lista_casona3.html` → imprimir a PDF", f"3. {BROCHURE}", "",
               "## Disponibilidad del mes", "",
               f"- **Casona 2:** {resumen(disp['Casona 2'])}", f"- **Casona 3:** {resumen(disp['Casona 3'])}", "",
               "## Mensaje para los colegas", "", "```text", mensaje, "```", "",
               "## Chequeos", "", "| | Regla | Detalle |", "|---|---|---|"]
    paquete += [f"| {'✅' if c[2] else '❌'} {c[0]} | {c[1]} | {c[3]} |" for c in chequeos]
    paquete += ["", "## Revisión humana", "",
                "- ¿Se actualizó la planilla interna con las ventas del mes antes de generar el paquete?",
                "- ¿A quiénes se envió?", "- ¿Qué respondieron?", ""]
    (carpeta / "paquete.md").write_text("\n".join(paquete), encoding="utf-8")

    print(f"Paquete de {nombre_mes} en {carpeta.relative_to(RAIZ).as_posix()} · "
          f"{'listo para revisar' if ok else 'REVISAR: hay chequeos en rojo'}")
    for c in chequeos:
        if not c[2]:
            print(f"  ❌ {c[0]} {c[1]} — {c[3]}")
    if a.avisar:
        texto = (f"El paquete de {nombre_mes} para colegas está listo para revisar y enviar."
                 if ok else f"El paquete de {nombre_mes} tiene chequeos en rojo: revisalo antes de enviar.")
        subprocess.run(["powershell", "-NoProfile", "-Command",
                        "Add-Type -AssemblyName System.Windows.Forms; "
                        f"[System.Windows.Forms.MessageBox]::Show('{texto}', 'Copiloto DOMINIA') | Out-Null; "
                        f"Start-Process '{carpeta}'"], check=False)


if __name__ == "__main__":
    main()
