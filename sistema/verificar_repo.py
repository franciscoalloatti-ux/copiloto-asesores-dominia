"""Verificación del repositorio antes de cada commit: que no se haya roto nada.

Salió de los errores reales de la construcción (ver DECISIONES D-27): conteos que quedaron viejos,
horas en UTC anotadas como locales, un salto de línea dentro de una expresión regular, una tabla
cortada por líneas en blanco y chequeos que cambiaban sin que las corridas guardadas lo reflejaran.
No llama a ninguna API.

Uso:
    python sistema/verificar_repo.py
Sale con código 1 si encuentra algún problema.
"""
import ast
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import copiloto as c  # noqa: E402

RAIZ = c.RAIZ
problemas, avisos = [], []


def problema(texto):
    problemas.append(texto)


def textos(*patrones):
    for patron in patrones:
        for p in RAIZ.glob(patron):
            if ".git" not in p.parts and p.is_file():
                yield p


# 1 · El código compila
for p in textos("sistema/*.py", "herramientas/*.py"):
    try:
        ast.parse(p.read_text(encoding="utf-8"))
    except SyntaxError as e:
        problema(f"Sintaxis de Python rota en {p.relative_to(RAIZ)}: línea {e.lineno}")

# 2 · El JavaScript del front compila (si hay Node)
plantilla = (RAIZ / "visor" / "plantilla.html").read_text(encoding="utf-8")
if shutil.which("node"):
    js = "\n".join(re.findall(r"<script>(.*?)</script>", plantilla, re.S)).replace("/*__DATOS__*/null", "null")
    js = (RAIZ / "visor" / "chequeos.js").read_text(encoding="utf-8") + chr(10) + js.replace("/*__CHEQUEOS__*/", "")
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as tmp:
        tmp.write(js)
    r = subprocess.run(["node", "--check", tmp.name], capture_output=True, text=True)
    if r.returncode:
        problema("JavaScript del front roto: " + (r.stderr.strip().splitlines() or ["?"])[-1])
else:
    avisos.append("No hay Node: no se revisó la sintaxis del JavaScript del front")

# 3 · Sin caracteres de control ocultos
for p in textos("**/*.md", "**/*.py", "**/*.html", "**/*.json", "**/*.csv"):
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", p.read_text(encoding="utf-8", errors="replace")):
        problema(f"Caracteres de control en {p.relative_to(RAIZ)}")

# 4 · Los esquemas son JSON válido
for p in textos("sistema/*.json"):
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        problema(f"JSON inválido en {p.relative_to(RAIZ)}: {e}")

# 5 · Lo que dicen las corridas del front coincide con los chequeos de hoy
for p in textos("corridas/vivo/*.md"):
    t = p.read_text(encoding="utf-8")
    ficha = json.loads(re.search(r"```json\n(.*?)\n```", t, re.S).group(1))
    ficha.setdefault("seguimiento", [])
    bloque = re.search(r"```markdown\n(.*?)\n```", t, re.S).group(1)
    datos = dict(re.findall(r"^(asesor|canal|fecha): (.*)$", bloque, re.M))
    datos["consulta"] = bloque.split("## Consulta", 1)[1].strip()
    v = c.verificar(ficha, datos, [{}])
    malos = [x["codigo"] for x in v["chequeos"] if not x["ok"]]
    calculado = "aprobada para revisión" if v["aprobada_para_revision"] else f"BLOQUEADA ({', '.join(malos)})"
    dicho = re.search(r"^\| Con los chequeos vigentes[^|]*\| (.*?) \|$", t, re.M)
    if not dicho:
        problema(f"{p.name}: falta la fila «Con los chequeos vigentes»")
    elif dicho.group(1) != calculado:
        problema(f"{p.name}: dice «{dicho.group(1)}» y con los chequeos de hoy da «{calculado}»")

# 6 · Ninguna corrida es posterior al commit que la agregó
for p in textos("corridas/**/*.md"):
    m = re.search(r"^\| Fecha de la corrida \| (\d{4}-\d{2}-\d{2} \d{2}:\d{2})", p.read_text(encoding="utf-8"), re.M)
    if not m:
        continue
    # Sin --follow: con él, git confunde corridas parecidas (la C04 de las 17:42 con la de las 17:31) como si
    # fueran el mismo archivo renombrado, y toma la fecha del commit equivocado.
    log = subprocess.run(["git", "log", "--diff-filter=A", "--format=%ad", "--date=format:%Y-%m-%d %H:%M",
                          "--", str(p.relative_to(RAIZ))], cwd=RAIZ, capture_output=True, text=True).stdout.split()
    if len(log) >= 2:
        agregado = datetime.strptime(" ".join(log[-2:]), "%Y-%m-%d %H:%M")
        if datetime.strptime(m.group(1), "%Y-%m-%d %H:%M") > agregado:
            problema(f"{p.name}: la corrida ({m.group(1)}) es posterior al commit que la agregó ({agregado:%Y-%m-%d %H:%M})")

# 7 · Tablas de markdown sin cortar por líneas en blanco
for p in textos("*.md", "conocimiento/*.md", "prompts/*.md"):
    t = p.read_text(encoding="utf-8")
    for m in re.finditer(r"\|\s*\n\s*\n(\| *\d+ *\|)", t):
        problema(f"Tabla cortada por una línea en blanco en {p.name}, antes de «{m.group(1)}»")

# 8 · Conteos escritos que ya se quedaron viejos alguna vez
frases = [r"\b\d+ técnicas", r"\b\d+ chequeos en código", r"\b\d+</b> reglas", r"\b\d+</b> iteraciones",
          r"\b(doce|trece|catorce|quince|dieciséis|diecisiete) (chequeos|reglas|corridas del botón)\b(?! (de entonces|que existían))",
          r"V1[–-]V1\d"]
for p in (RAIZ / "README.md", RAIZ / "GOBIERNO.md", RAIZ / "visor" / "plantilla.html"):
    for f in frases:
        for m in re.finditer(f, p.read_text(encoding="utf-8")):
            problema(f"Conteo escrito en {p.name}: «{m.group(0)}» — nombrá el archivo que tiene el dato")

# 8 bis · Los tests: regresión de chequeos y paridad Python / JavaScript
for test in ("test_regresion.py", "test_paridad.py"):
    r = subprocess.run([sys.executable, str(RAIZ / "pruebas" / test)], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        problema(f"Falló pruebas/{test}: " + " | ".join(l.strip() for l in r.stdout.splitlines() if "❌" in l)[:300])

# 9 · El visor publicado está al día con el repositorio
index = RAIZ / "visor" / "index.html"
anterior = index.read_text(encoding="utf-8")
subprocess.run([sys.executable, str(RAIZ / "sistema" / "generar_visor.py")], cwd=RAIZ, capture_output=True, text=True)
if index.read_text(encoding="utf-8") != anterior:
    problema("visor/index.html no estaba al día: se regeneró ahora, hay que commitearlo y republicar el artefacto")

print("Verificación del repositorio")
for a in avisos:
    print("  ⚠", a)
for x in problemas:
    print("  ❌", x)
print("  ✅ Sin problemas" if not problemas else f"  {len(problemas)} problema(s)")
sys.exit(1 if problemas else 0)
