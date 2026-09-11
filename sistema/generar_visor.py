"""Genera visor/index.html: una página para recorrer las corridas del copiloto sin abrir los .md.

Lee entradas/, corridas/ (incluidas coherencia/ y plan_mensual/) y la plantilla visor/plantilla.html,
y escribe visor/index.html con los datos embebidos. No llama a ninguna API.

Uso:
    python sistema/generar_visor.py
"""
import json
import re
from pathlib import Path

from copiloto import RAIZ, leer_entrada

VERSIONES = {
    "911bac10d216": ("v1", "Contrato v1 + playbook v0 (prueba de humo)"),
    "07325a31ef33": ("v1", "Contrato v1 + playbook v1"),
    "cae72a3c838e": ("v2", "Iteración 1 · restricciones"),
    "230238bc0c27": ("v3", "Iteración 2 · formato"),
    "c59fefd13d70": ("v3+", "Iteración 3 · contexto (playbook v2)"),
    "b856d022cd4b": ("v4", "Iteración 4 · formato"),
    "d48ad9997e10": ("v4+", "Iteración 5 · calendario y V12"),
    "6a60ec936cf3": ("vigente", "Contrato vigente"),
}


def seccion(texto, titulo):
    m = re.search(r"^## " + re.escape(titulo) + r"[^\n]*\n(.*?)(?=^## |\Z)", texto, re.S | re.M)
    return m.group(1).strip() if m else ""


def leer_corrida(ruta):
    t = ruta.read_text(encoding="utf-8")
    campo = lambda n: (re.search(r"^\| " + re.escape(n) + r"[^|]*\| (.*?) \|$", t, re.M) or [None, ""])[1].strip("` ")
    j = re.search(r"```json\n(.*?)\n```", t, re.S)
    total = re.search(r"\*\*Total\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\*", t)
    costo = re.search(r"Costo de la corrida: USD ([\d.]+)", t)
    h = campo("Versión del contrato")
    return {
        "archivo": ruta.relative_to(RAIZ).as_posix(),
        "fecha": campo("Fecha de la corrida"),
        "modelo": campo("Modelo"),
        "hash": h,
        "version": VERSIONES.get(h, ("?", "Versión sin registrar"))[0],
        "version_detalle": VERSIONES.get(h, ("?", "Versión sin registrar"))[1],
        "resultado": campo("Resultado"),
        "herramienta": re.findall(r"^\d+\. `(\w+)\((.*?)\)` → (.*)$", t, re.M),
        "ficha": json.loads(j.group(1)) if j else None,
        "chequeos": [{"ok": ok == "✅", "codigo": c, "regla": r, "detalle": d}
                     for ok, c, r, d in re.findall(r"^\| (✅|❌) (\w+) \| (.*?) \| (.*?) \|$", t, re.M)],
        "tokens": dict(zip(["entrada", "cache_escritura", "cache_lectura", "salida"], map(int, total.groups()))) if total else None,
        "costo": float(costo.group(1)) if costo else None,
    }


def main():
    consultas = []
    for ruta in sorted((RAIZ / "entradas").rglob("*.md")):
        texto, datos = leer_entrada(ruta)
        titulo = texto.splitlines()[0].split("—", 1)[-1].strip()
        real = seccion(texto, "Lo que pasó en la realidad")
        corridas = sorted((leer_corrida(p) for p in (RAIZ / "corridas").rglob(f"*_{datos['consulta_id']}_*.md")
                           if "errores" not in p.parts), key=lambda c: c["fecha"])
        consultas.append({
            "id": datos["consulta_id"], "titulo": titulo, "canal": datos["canal"], "fecha": datos["fecha"],
            "asesor": datos["asesor"], "notas": datos["notas"], "historial": datos["historial"],
            "consulta": datos["consulta"], "real": real, "transcripcion": seccion(texto, "Transcripción"),
            "grupo": "coherencia" if "coherencia" in ruta.parts else ("colega" if datos["canal"] == "inmobiliaria" else "cliente"),
            "corridas": corridas,
        })
    plan = [leer_corrida(p) for p in sorted((RAIZ / "corridas" / "plan_mensual").glob("*.md"))]
    datos = {"consultas": consultas, "plan": plan[-1] if plan else None}
    plantilla = (RAIZ / "visor" / "plantilla.html").read_text(encoding="utf-8")
    salida = plantilla.replace("/*__DATOS__*/null", json.dumps(datos, ensure_ascii=False).replace("</", "<\\/"))
    (RAIZ / "visor" / "index.html").write_text(salida, encoding="utf-8")
    print(f"visor/index.html · {len(consultas)} consultas · {sum(len(c['corridas']) for c in consultas)} corridas")


if __name__ == "__main__":
    main()
