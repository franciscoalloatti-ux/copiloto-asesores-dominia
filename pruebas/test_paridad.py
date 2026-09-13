"""Test de paridad: los chequeos de Python (sistema/copiloto.py) y los de JavaScript (visor/chequeos.js)
tienen que dar lo mismo sobre todas las corridas guardadas. Si alguien cambia una regla en un solo
lado, este test falla.

Uso:
    python pruebas/test_paridad.py
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from casos import RAIZ, c, casos, resultado_python  # noqa: E402

lista = list(casos())
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tmp:
    json.dump({"casos": lista, "tarifario": c.leer_tarifario()}, tmp, ensure_ascii=False)
r = subprocess.run(["node", str(RAIZ / "pruebas" / "correr_chequeos_js.js"), tmp.name],
                   capture_output=True, text=True, encoding="utf-8")
if r.returncode:
    print("  ❌ JavaScript falló:", r.stderr.strip()[-400:])
    sys.exit(1)
js = json.loads(r.stdout)
diferencias = []
for caso in lista:
    py, jv = resultado_python(caso), js.get(caso["nombre"], {})
    for codigo in sorted(set(py) | set(jv), key=lambda x: int(x[1:])):
        if py.get(codigo) != jv.get(codigo):
            diferencias.append(f"{caso['nombre']} · {codigo}: Python {py.get(codigo)}, JavaScript {jv.get(codigo)}")
print("Test de paridad Python / JavaScript")
for d in diferencias:
    print("  ❌", d)
print(f"  ✅ {len(lista)} corridas, mismas respuestas en los dos" if not diferencias else f"  {len(diferencias)} diferencia(s)")
sys.exit(1 if diferencias else 0)
