"""Arma, para cada corrida guardada, la ficha, los datos y la cantidad de llamadas a la herramienta.

Lo usan los tests de regresión y de paridad Python/JavaScript: los dos tienen que evaluar exactamente
los mismos casos.
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "sistema"))
import copiloto as c  # noqa: E402

EXCLUIDAS = ("errores", "plan_mensual", "paquete_colegas")


def _datos_de_vivo(texto):
    bloque = re.search(r"```markdown\n(.*?)\n```", texto, re.S).group(1)
    datos = dict(re.findall(r"^(consulta_id|asesor|canal|fecha): (.*)$", bloque, re.M))
    datos["consulta"] = bloque.split("## Consulta", 1)[1].strip()
    return datos


def casos():
    entradas = {}
    for p in (RAIZ / "entradas").rglob("*.md"):
        _, d = c.leer_entrada(p)
        entradas[d["consulta_id"]] = d
    for ruta in sorted(list((RAIZ / "corridas").rglob("*.md")) + list((RAIZ / "pruebas" / "corridas").glob("*.md"))):
        if any(x in ruta.parts for x in EXCLUIDAS):
            continue
        texto = ruta.read_text(encoding="utf-8")
        m = re.search(r"```json\n(.*?)\n```", texto, re.S)
        if not m:
            continue
        ficha = json.loads(m.group(1))
        ficha.setdefault("seguimiento", [])
        if "vivo" in ruta.parts:
            datos = _datos_de_vivo(texto)
            llamadas = 1
        else:
            datos = entradas.get(ficha["consulta_id"])
            if datos is None:
                _, datos = c.leer_entrada(RAIZ / "pruebas" / "entradas" / "humo-01.md")
            llamadas = len(re.findall(r"^\d+\. `consultar_tarifario\(", texto, re.M))
        yield {
            "nombre": ruta.relative_to(RAIZ).as_posix(),
            "ficha": ficha,
            "datos": {k: datos.get(k, "") for k in ("asesor", "canal", "fecha", "consulta")},
            "llamadas": llamadas,
        }


def resultado_python(caso):
    v = c.verificar(caso["ficha"], caso["datos"], [{}] * caso["llamadas"])
    return {x["codigo"]: x["ok"] for x in v["chequeos"]}
