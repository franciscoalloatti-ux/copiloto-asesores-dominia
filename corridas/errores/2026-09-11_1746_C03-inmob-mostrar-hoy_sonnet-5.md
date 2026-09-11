# Corrida · C03-inmob-mostrar-hoy · 11/09/2026 17:46

| Campo | Valor |
|---|---|
| Fecha de la corrida | 2026-09-11 17:46 |
| Modelo | `claude-sonnet-5` |
| Versión del contrato (sha256 de system + user) | `6a60ec936cf3` |
| Tarifario (sha256) | `9a5c093faa46` |
| Archivo de entrada | `entradas/consulta-03.md` |
| Resultado | ERROR |

## Entrada

```markdown
# Entrada real 03 — inmobiliaria colega quiere mostrar hoy
consulta_id: C03-inmob-mostrar-hoy
asesor: Francisco
canal: inmobiliaria
fecha: 2026-09-01 09:28
notas: Llegó por WhatsApp. Corredor inmobiliario colega, trato informal. Transcripto de una captura; nombre del corredor anonimizado.

## Historial

[Mensaje anterior de otra fecha del corredor: «y me sumare con ellos». Sin más contexto.]

## Consulta

hola wasooooooo
si quiero mostrar casonas hoy a las 12 30

## Lo que pasó en la realidad (NO se le pasa al copiloto: sirve para comparar)

- 09:57 · Asesor: audio de 0:14 (contenido no transcripto).
- 09:58 · Asesor: reenvió dos mensajes: «Te mando un código» / «De validación».
```

## Llamadas a la herramienta

Ninguna.

## Salida

```text
BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CexJk2zLsuyKk6Tp9KPkD'}
```

## Consumo y costo

| Vuelta | Entrada | Escritura caché | Lectura caché | Salida | stop_reason |
|---|---|---|---|---|---|

## Revisión humana

_A completar por el asesor antes de enviar: qué corrigió del borrador, si lo envió, y qué respondió el interesado._

- Revisó:
- Cambios al borrador:
- ¿Se envió?:
- Respuesta del interesado:
