"""Transcribe un audio de WhatsApp (.ogg/.opus/.mp3) a texto, en la computadora del asesor.

Muchas consultas llegan como audio. El copiloto trabaja con texto, así que el audio se transcribe
primero con Whisper (modelo abierto, corre local: el audio del interesado no sale de la máquina)
y el texto resultante se pega en la sección «## Consulta» de la entrada.

Uso:
    python herramientas/transcribir_audio.py <audio.ogg> [--modelo small]

La primera vez descarga el modelo elegido de Hugging Face (Systran/faster-whisper-*).
"""
import argparse
import time

from faster_whisper import WhisperModel

import sys
if hasattr(sys.stdout, "reconfigure"):  # que funcione en un Windows sin UTF-8 (D-29)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ap = argparse.ArgumentParser()
ap.add_argument("audio")
ap.add_argument("--modelo", default="small", help="tiny, base, small, medium")
a = ap.parse_args()

inicio = time.time()
modelo = WhisperModel(a.modelo, device="cpu", compute_type="int8")
segmentos, info = modelo.transcribe(a.audio, language="es", vad_filter=True)
texto = " ".join(s.text.strip() for s in segmentos)
print(f"[modelo whisper-{a.modelo} · idioma {info.language} · {info.duration:.0f} s de audio · "
      f"{time.time() - inicio:.0f} s de proceso]")
print(texto)
