@echo off
rem Lo ejecuta la tarea programada "Copiloto DOMINIA - Paquete colegas" el dia 1 de cada mes a las 9.
rem Genera el paquete del mes para inmobiliarias colegas y avisa en pantalla. No envia nada.
cd /d "%~dp0.."
set PYTHONUTF8=1
python sistema\paquete_colegas.py --avisar >> corridas\paquete_colegas\_ultima_ejecucion.log 2>&1
