"""Test de regresión de los chequeos: que verificar() dé, sobre todas las corridas guardadas, lo mismo
que la última vez que se aprobó a mano.

Un chequeo nuevo o cambiado muestra solo qué corridas cambian. Si el cambio es el buscado, se
regenera la foto con --actualizar y se documenta en DECISIONES.

Uso:
    python pruebas/test_regresion.py
    python pruebas/test_regresion.py --actualizar
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from casos import RAIZ, casos, resultado_python  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):  # que funcione en un Windows sin UTF-8 (D-29)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

FOTO = RAIZ / "pruebas" / "esperado_chequeos.json"

actual = {caso["nombre"]: resultado_python(caso) for caso in casos()}
if "--actualizar" in sys.argv:
    FOTO.write_text(json.dumps(actual, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Foto actualizada: {len(actual)} corridas")
    sys.exit(0)

esperado = json.loads(FOTO.read_text(encoding="utf-8"))
diferencias = []
for nombre in sorted(set(actual) | set(esperado)):
    a, e = actual.get(nombre), esperado.get(nombre)
    if a is None or e is None:
        diferencias.append(f"{nombre}: {'nueva' if e is None else 'ya no existe'}")
        continue
    for codigo in sorted(set(a) | set(e), key=lambda x: int(x[1:])):
        if a.get(codigo) != e.get(codigo):
            diferencias.append(f"{nombre} · {codigo}: esperado {e.get(codigo)}, da {a.get(codigo)}")
print("Test de regresión de chequeos")
for d in diferencias:
    print("  ❌", d)
print(f"  ✅ {len(actual)} corridas, sin cambios" if not diferencias else f"  {len(diferencias)} diferencia(s)")
sys.exit(1 if diferencias else 0)
