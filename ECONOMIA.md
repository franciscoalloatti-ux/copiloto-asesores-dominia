# Análisis económico

> Todos los tokens de este documento son **medidos**: salen del campo `usage` que devuelve la API
> en cada vuelta, y cada corrida los guarda en su sección *Consumo y costo*. Nada es estimado salvo
> las proyecciones, que dicen su supuesto.

## Precios usados

Fuente: https://platform.claude.com/docs/en/about-claude/pricing, **consultada el 11/9/2026**.

| Modelo | Entrada | Escritura en caché (5 min) | Lectura de caché | Salida |
|---|---|---|---|---|
| `claude-opus-5` | USD 5,00 / MTok | USD 6,25 / MTok | USD 0,50 / MTok | USD 25,00 / MTok |
| `claude-sonnet-5` | USD 2,00 / MTok | USD 2,50 / MTok | USD 0,20 / MTok | USD 10,00 / MTok |
| `claude-haiku-4-5` | USD 1,00 / MTok | USD 1,25 / MTok | USD 0,10 / MTok | USD 5,00 / MTok |

## Costo por consulta (módulo 1, Opus 5)

> **Qué contrato se midió.** Todas las mediciones de este documento son de las corridas por API del 11/9
> (hasta las 17:45), con el contrato de ese momento (sha `6a60ec936cf3` para las últimas). El contrato
> que rige hoy es más largo —el system prompt con sus anexos pasó de 28.783 a 38.170 caracteres— y la
> ficha suma el campo `seguimiento`, así que **una consulta con el contrato de hoy cuesta más que lo
> medido acá, y no se volvió a medir** porque no hay crédito de API (D-12). El front corre con la
> capacidad `sample` de la página, a cuenta de la suscripción de quien la usa, y no expone tokens:
> su costo no se puede medir con este método.

Cada consulta hace **dos vueltas**: en la primera el modelo pide el tarifario, en la segunda
escribe la ficha. El prefijo fijo (system prompt, ficha del proyecto, playbook, herramienta y
esquema) mide **~15.400 tokens** y se guarda en caché. Por eso el costo depende de si la consulta
llega **en frío** (el caché venció, porque pasaron más de 5 minutos desde la anterior) o **en
caliente**.

| | Corrida de referencia | Entrada | Escritura caché | Lectura caché | Salida | Costo |
|---|---|---|---|---|---|---|
| **En frío** (el caso real: consultas separadas) | `corridas/2026-09-11_1739_C01-inmob-1dorm_opus-5.md` | 3.769 | 15.425 | 15.425 | 4.359 | **USD 0,2319** |
| **En caliente** (varias seguidas) | `corridas/2026-09-11_1745_C06-cliente-PBA-C3_opus-5.md` | 7.279 | 0 | 30.850 | 4.456 | **USD 0,1632** |

**La cuenta, rehecha a mano para la corrida en frío:**

```text
entrada          3.769 × 5,00 / 1.000.000 = 0,0188
escritura caché 15.425 × 6,25 / 1.000.000 = 0,0964
lectura caché   15.425 × 0,50 / 1.000.000 = 0,0077
salida           4.359 × 25,00 / 1.000.000 = 0,1090
                                    total = 0,2319 USD
```

**Sobre 26 corridas exitosas con Opus 5** (todas las de `corridas/` y `corridas/coherencia/`):
costo medio USD 0,1628 (mínimo 0,1034, máximo 0,2319); salida media 3.779 tokens (entre 2.136 y
5.181). La mayoría se corrió en tandas, en caliente. **Para proyectar se usa el costo en frío**,
porque en la vida real las consultas llegan separadas por horas.

**Dónde se va la plata.** En frío, el 47 % del costo es la **salida** (la ficha JSON más el
razonamiento adaptativo del modelo) y el 42 % es **escribir el caché**. La ficha de esa corrida tiene
5.282 caracteres, que son entre 1.800 y 2.500 tokens según la densidad medida más abajo: **casi la
mitad de los 4.359 tokens de salida es razonamiento**. Es la primera palanca para bajar el costo
(ver *Elección de modelo*).

### ¿Es plausible el conteo de tokens?

El prefijo cacheable tiene **32.920 caracteres** (system prompt con anexos: 28.783; herramienta:
995; esquema: 3.142) y la API lo midió en **15.425 tokens**: **2,13 caracteres por token**, algo por
debajo del rango habitual para el español (2,5 a 5). Tres razones lo explican:

- **La API suma texto propio** a lo que uno manda: 286 tokens de instrucciones de uso de herramientas
  en Opus 5 (dato de la página de precios) y la gramática de la salida estructurada.
- **El texto es denso en tokens**: tablas markdown, montos, códigos (`T-19`, `casona_3_pozo`), tildes
  y eñes.
- **Desde Claude 4.7 el tokenizador genera cerca de un 30 % más de tokens** para el mismo texto
  (nota de la misma página de precios).

## Módulo 2: el plan mensual

Una corrida por mes. La del plan de octubre (`corridas/plan_mensual/2026-09-11_1744_plan-2026-10_opus-5.md`):
15.250 tokens de entrada, 12.161 de escritura y 12.161 de lectura de caché, 13.292 de salida:
**USD 0,4906 por mes, USD 5,89 por año.**

## Proyección

El responsable no tiene un volumen fijo: *«las consultas son relativas hay semanas que hay varias
otras no tanto a vyeces a traves de inmobiliaria»*. El registro del proyecto tiene 11 consultas
entre el 22/6 y el 10/9, pero son las capturas que se eligieron para probar, no el total. Por eso se
proyectan **tres escenarios**, con el costo en frío de Opus 5 (USD 0,2319 por consulta) más el plan
mensual:

| Supuesto de volumen | Por semana | Por año (52 semanas + 12 planes) |
|---|---|---|
| **Bajo**: 5 consultas por semana | USD 1,16 | USD 66,18 |
| **Medio**: 15 consultas por semana | USD 3,48 | USD 186,77 |
| **Alto**: 30 consultas por semana | USD 6,96 | USD 367,65 |

**Contra qué se compara.** Una unidad de Casona de los Arcos vale entre USD 126.022 y USD 349.725.
El escenario alto cuesta al año menos del 0,3 % del precio de la unidad más barata. El responsable
dijo que lo que busca no es ahorrar tiempo sino *«la coherencia y la efectividad de la respuesta»*:
el costo del copiloto no es la variable que decide, y **una sola visita que se pierde por una
respuesta mal dada** (la corrida 03 en su versión 1 casi pierde una) cuesta más que un año de uso.

## Elección de modelo

**Criterio del curso: el modelo más chico que hace bien la tarea.** El sistema se construyó e iteró
con Opus 5 porque, mientras el contrato cambiaba, hacía falta separar los errores del contrato de los
errores del modelo.

**Estado de la prueba: incompleta.** El 11/9 a las 17:46 estaban programadas las mismas tres
consultas (03 colega, 06 cliente, 09 audio y canje) con `claude-haiku-4-5` y `claude-sonnet-5`, y
las seis fallaron antes de empezar:

```text
BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}
```

Las corridas fallidas están en `corridas/errores/`. **Hasta que la prueba se haga no hay elección de
modelo justificada con evidencia**: solo lo que dicen los precios. Con el mismo consumo de tokens,
una consulta en frío costaría unos USD 0,093 con Sonnet 5 y USD 0,046 con Haiku 4.5. Pero Haiku 4.5
no tiene razonamiento adaptativo y la tarea tiene reglas que compiten entre sí (lista única, sin
precio al cliente, visita ya propuesta, dos preguntas en total). Si el modelo chico falla una sola
de esas reglas, los chequeos lo frenan, pero el asesor tiene que reescribir el borrador, y ese
trabajo cuesta más que la diferencia de precio.
