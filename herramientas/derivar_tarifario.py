"""Deriva el tarifario que lee el copiloto a partir de las dos listas internas de DOMINIA.

Las planillas originales NO se versionan: tienen comisiones, hojas por inmobiliaria y datos
de compradores. Este script toma solo las columnas comerciales y escribe
herramientas/tarifario_vigente.csv, que es lo único que el agente puede leer.

Uso:
    python herramientas/derivar_tarifario.py <lista_casona2.xlsx> <lista_casona3.xlsx>
"""
import csv
import sys
from pathlib import Path

import openpyxl

SALIDA = Path(__file__).parent / "tarifario_vigente.csv"

# Expensas mensuales por cantidad de dormitorios (confirmadas por el desarrollista, ago-2026).
EXPENSAS_ARS = {1: 220000, 2: 270000, 3: 330000}

# Unidades que existen en la planilla pero NO se ofrecen (decisión del desarrollista).
# El texto de la observación lo puede leer un cliente: se escribe como se le diría, sin jerga interna.
NO_SE_OFRECEN = {("Casona 3", "PB H"): "No está a la venta"}

COLUMNAS = [
    "edificio", "unidad", "estado", "entrega", "dormitorios", "banos", "planta",
    "m2_cubiertos", "m2_balcon", "m2_jardin_uso_exclusivo", "m2_propios", "m2_boleto_total",
    "cochera", "precio_lista_usd", "usd_m2_boleto", "forma_de_pago", "anticipo_usd",
    "cuotas", "cuota_mensual_usd", "saldo_contra_entrega_usd", "expensas_mensuales_ars",
    "expensas_desde", "disponible", "observacion", "lista", "fecha_lista",
]


def tipologia(texto):
    """'2 dormitorios - 1 Baño' -> (2, 1)"""
    partes = texto.replace("-", " ").split()
    return int(partes[0]), int(partes[partes.index("Baño" if "Baño" in partes else "Baños") - 1])


def planta(unidad):
    return "PB" if unidad.startswith("PB") else unidad.split("º")[0] + "º piso"


def num(v, dec=2):
    return round(float(v), dec) if v not in (None, "", "NO") else 0


def casona2(ruta):
    ws = openpyxl.load_workbook(ruta, data_only=True).active
    titulo = ws.cell(3, 2).value  # 'LISTA DE PRECIO ... (Nº5) - ENERO 2025 (01/10/2025)'
    filas = []
    for r in ws.iter_rows(min_row=8, max_row=40, values_only=True):
        if not r[1] or not str(r[1]).strip().startswith(("PB", "1º", "2º", "3º")):
            continue
        unidad = str(r[1]).strip()
        dorm, banos = tipologia(r[2])
        amoblado = r[16] is None and r[17] is not None
        precio = r[17] if amoblado else r[16]
        m2_boleto = num(r[15])
        filas.append({
            "edificio": "Casona 2", "unidad": unidad, "estado": "terminado", "entrega": "inmediata",
            "dormitorios": dorm, "banos": banos, "planta": planta(unidad),
            "m2_cubiertos": num(r[3]), "m2_balcon": num(r[4]), "m2_jardin_uso_exclusivo": num(r[5]),
            "m2_propios": num(r[6]), "m2_boleto_total": m2_boleto, "cochera": "si",
            "precio_lista_usd": round(precio), "usd_m2_boleto": round(precio / m2_boleto),
            "forma_de_pago": "contado o crédito hipotecario del comprador",
            "anticipo_usd": "", "cuotas": "", "cuota_mensual_usd": "", "saldo_contra_entrega_usd": "",
            "expensas_mensuales_ars": EXPENSAS_ARS[dorm], "expensas_desde": "posesión",
            "disponible": "si",
            "observacion": ("Se entrega amoblado y equipado por Interiores B.AP; su USD/m² no es "
                            "comparable con el resto" if amoblado else ""),
            "lista": "Lista N°5 Casona 2", "fecha_lista": "2025-10-01",
        })
    return filas, titulo


def casona3(ruta):
    ws = openpyxl.load_workbook(ruta, data_only=True)["LISTA DE PRECIOS "]
    filas = []
    for r in ws.iter_rows(min_row=7, max_row=40, values_only=True):
        if not r[1] or not str(r[1]).strip().startswith(("PB", "1º", "2º", "3º")) or r[26] is None:
            continue
        unidad = str(r[1]).strip()
        dorm, banos = tipologia(r[2])
        precio, m2_boleto = float(r[26]), num(r[23])
        no_ofrece = NO_SE_OFRECEN.get(("Casona 3", unidad))
        filas.append({
            "edificio": "Casona 3", "unidad": unidad, "estado": "en obra", "entrega": "2029 (estimada)",
            "dormitorios": dorm, "banos": banos, "planta": planta(unidad),
            "m2_cubiertos": num(r[4]), "m2_balcon": num(r[5]), "m2_jardin_uso_exclusivo": num(r[8]),
            "m2_propios": num(r[9]), "m2_boleto_total": m2_boleto, "cochera": "si",
            "precio_lista_usd": round(precio), "usd_m2_boleto": round(precio / m2_boleto),
            "forma_de_pago": "40% anticipo + 40% en 30 cuotas (USD o pesos ajustados por CAC) + 20% contra entrega",
            "anticipo_usd": round(r[30]), "cuotas": 30, "cuota_mensual_usd": round(r[31]),
            "saldo_contra_entrega_usd": round(r[32]),
            "expensas_mensuales_ars": EXPENSAS_ARS[dorm], "expensas_desde": "posesión (2029)",
            "disponible": "no" if no_ofrece else "si", "observacion": no_ofrece or "",
            "lista": "Lista financiada Casona 3 (planilla de superficies Rev. 25)",
            "fecha_lista": "2025-10-21",
        })
    return filas


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    c2, titulo = casona2(sys.argv[1])
    c3 = casona3(sys.argv[2])
    with SALIDA.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNAS)
        w.writeheader()
        w.writerows(c2 + c3)
    print(f"{titulo}")
    print(f"Casona 2: {len(c2)} unidades · USD {sum(x['precio_lista_usd'] for x in c2):,}")
    print(f"Casona 3: {len(c3)} unidades · USD {sum(x['precio_lista_usd'] for x in c3):,} "
          f"· disponibles {sum(x['disponible'] == 'si' for x in c3)}")
    print(f"-> {SALIDA}")
