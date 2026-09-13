# Copiloto para Asesores Comerciales de DOMINIA

> Trabajo final · Creación de Agentes de IA · MBA UCEMA · 2026 2T · Francisco Alloatti
> Estado al 13/9/2026: contrato en su versión 5, dos módulos y un envío mensual funcionando, 26
> corridas reales exitosas y dos auditorías hechas (la comercial contra los manuales y la de la
> rúbrica de la materia). Pendiente: la comparación de modelos, frenada por falta de crédito en la
> API, y correr las iteraciones 6 a 8 (ver *Qué falta o qué falló*).

| Documento | Qué tiene |
|---|---|
| `prompts/` | El contrato: `system_prompt.md` y `user_prompt.md` (módulo 1) y `variantes/` (módulo 2) |
| `corridas/` | Las ejecuciones reales: entrada, llamadas a la herramienta, salida, chequeos, tokens, costo y fecha |
| `DECISIONES.md` | La historia completa: cada decisión numerada (D-01 en adelante) y cada iteración del contrato con el error textual que la motivó |
| `auditorias/` | La auditoría comercial del 12/9: dieciséis hallazgos contra los manuales, con el texto exacto que había que cambiar |
| `ECONOMIA.md` | Costo por corrida medido, la cuenta rehecha, proyección y elección de modelo |
| `GOBIERNO.md` | Permisos, los modos de falla con su mitigación, el control humano y quién firma |
| `visor/index.html` | **Para usarlo y para mirarlo.** Publicado como artefacto privado en la cuenta del autor (el link no es público; el archivo del repositorio es la copia que se puede abrir sin permisos). La pestaña «Usar el copiloto» toma una consulta nueva, consulta el tarifario, arma la ficha y el borrador y corre los doce chequeos, sin usar la API (capacidad `sample`, a cuenta de quien abre la página). Abierto como archivo local queda solo el visor: elegí una consulta. Muestra lo que respondió el asesor real, el borrador del copiloto en cada versión del contrato, la ficha, los doce chequeos y el plan de octubre. Se regenera con `python sistema/generar_visor.py` |

## Qué construí

Un agente que prepara la respuesta a cada consulta de un interesado en **Casona de los Arcos**
(DOMINIA, Manantiales, Córdoba). Lee la consulta —llegue por WhatsApp, Instagram, un portal o una
inmobiliaria colega—, consulta el tarifario vigente, ubica a la persona en el camino del comprador,
decide **qué lista le corresponde** (terminados de Casona 2 o pozo de Casona 3, nunca las dos),
propone hasta tres unidades con su precio exacto y deja un **borrador de mensaje** cuyo objetivo es
conseguir la visita. **El agente nunca le escribe al cliente**: el asesor revisa, corrige y envía
con su firma. Es para los asesores comerciales de DOMINIA y las inmobiliarias que venden el proyecto.

Un segundo módulo arma el **plan mensual de ventas y publicaciones**: lee el registro de consultas
que dejó el primero y el stock, y propone qué unidades empujar, por qué canal y con qué mensaje. Y
el día 1 de cada mes, una **tarea programada** arma el **paquete para inmobiliarias colegas**: las
dos listas actualizadas por separado, el brochure, la disponibilidad y el mensaje, listo para que el
asesor lo revise y lo mande.

Nivel de delegación: **L2 — ejecuta con revisión**. Responsable del sistema: **Francisco Alloatti,
responsable general de DOMINIA**.

## Cómo se lo pedí

Los pedidos, en orden y textuales (con sus errores de tipeo), en la conversación con el agente
constructor (Claude, en Claude Code):

**1 · Elección del tema**

> Quiero que actues como un especialista en creacion de agentes. Estoy llegando al final de la materia del mba de ucema creacion de agentes con ia (del cual hicimos varios trabajos y cargue documentación) y tengo que presentar mi trabajo final que corresponde al pdf que subi. Necesito que me ayudes a legir un tema y poisterior a eso voy a armar mi prompt para que arranquemos lo cual te pido que me vayas ayudando para cumplir consignas y rubricas necesarias

**2 · El pedido del sistema** (el agente constructor había propuesto una plantilla con corchetes;
así la devolví, con algunos corchetes todavía sin completar)

> bueno hagamos el copiloto comercial de casona de los arcos. anoche finalmente no se eligio ninguno en particular si no que van a tomar lo mejor de cada uno para potenciar lo de los profes
>
> Quiero que actues como un especialista en creacion de agentes, especializados en agentes inmobiliarios. Quiero construir mi trabajo final de Creación de Agentes de IA (MBA UCEMA), pero ademas que sea una herramienta muy potente que pueda usar para comoercialisar nuestros productos: un copiloto comercial para la venta de Casona de los Arcos. La consigna es el PDF trabajo_final.
>
> Objetivo: quiero un agente que me vaya armando planes de ventas y publicaciones en portales mensualmente y que cuando me escribe un interesado  [por dónde llegan: WhatsApp, Instagram, portales], el agente lee la consulta, consulta el tarifario vigente, decide qué lista corresponde mostrarle, me propone unidades con precio y me deja un borrador de respuesta. que arme el camino del consumidor lo clasifique y de la mejor estrategia para concretar la venta, para eso tener en cuenta peapers como 📓 La "Biblia" del Real Estate (Estructura y Escala), 📈 Marca Personal y Cierre de Alto Impacto, "El cierre de la venta inmobiliaria, "Everybody Wins" de Dave Liniger, Comunicar para vender, El camino del Real Estate Argentino, Marketing para Inmobiliarios: Corredores y Tasadore, Fideicomisos al Costo
> Yo reviso y lo mando: el agente nunca le escribe al cliente. Hoy eso me lleva [cuánto tiempo por consulta / cuántas consultas por semana].
>
> Contexto del negocio: [stock: 8 terminadas en Casona 2, 28 en pozo en Casona 3 con entrega 2029; plan de pago en periodo de obra; expensas; lo que sepas que siempre preguntan].
>
> Reglas que el agente no puede romper: [nunca mostrar las dos listas al mismo comprador y por qué; descuento máximo; unidades que no se ofrecen; qué hacer si pide algo que no existe; qué no puede prometer nunca].
>
> Herramienta: la lista de precios. La planilla original es interna (tiene comisiones y datos de compradores), así que el agente solo lee una versión derivada con [qué columnas].
>
> Supervisión: L2. El agente propone, yo reviso [qué reviso en concreto antes de mandar] y firmo como [nombre, rol].
>
> Pruebas: te voy a pasar tres consultas reales, anonimizadas.
>
> Cómo quiero trabajar: vos proponés y yo decido; una pieza del contrato por vez; cada iteración la documentamos con el error textual y un commit. El repo tiene que respetar la estructura obligatoria: README.md, prompts/, corridas/, DECISIONES.md.
> Las consultas las hacemos despues.
> Me quiero presentar como que pueda agregar el nombre el scesor comercial y luego que diga que es asesor comercial de DOMINIA. Siempre intentar respetar las tecnicas de los manuales para ver que mostrar y que no por mensage, el objetivo final es concretar la visita. El nombre que sea Copiloto para Asesores ccomerciales de dominia

**3 · Respuesta a las preguntas del agente constructor** (alcance, manuales, volumen, firma,
publicación)

> me gustaria que sea completo, los manuales deberiamos descargarlos de la web, las consultas son relativas hay semanas que hay varias otras no tanto a vyeces a traves de inmobiliaria lo importante mas que el tiempo es la coherencia y la efectividad de la respuesta. Mi rol en dominia es general porque es empresa familiar. Se puede publicar todo

**4 · Correcciones de contexto y publicación**

> pero los  manuales tienen que estar en pdf en internet para leerlos ounquesea, podrias aprender de ahi. LAs tres consultas queres que te las cargue como capturas, que te mande audios o que?. Casona 3 se vende con boleto de compraventa financiada a plazo de obra. Casona 1 esta totalmente vendida, Casona 2 estan vendidos 20 de 28 y el complejo se cierra con la tercer torre con lo cual seria muy dificil no terminar con el compromiso en un complejo tan consolidado.
> Subilo al github

**5 · Las consultas reales** (acompañadas de capturas de WhatsApp y un audio; el número de teléfono
quedó anonimizado)

> te voy a mostrar chats de posibles venta. Primero con inmobiliarios y despues de consultas de clientes

> y despues te mando uno puntual con audio. LA ultima foto del numero [número anonimizado] es la que manda el audio subido

**6 · Decisiones sobre las fallas de la primera tanda** (respuestas a cuatro preguntas del agente
constructor; dos fueron la elección de una opción)

> Colegas: lo que pida, si esta buscando en poso lista casona 3 y si no la 2. Pero esta bueno lo del perfil de cliente. LA casona 3 es un excel que lo mandaria en formato de lista tambien
>
> Presentación: «Presentación y firma» (opción elegida)
>
> Precio en el primer mensaje: Sin precio como recomendas y siguiendo los pasos de los manuales. Justamente quiero transformar asesores comunes en los mejores
>
> Iteraciones: «Sí, en ese orden» (opción elegida: restricciones → formato → contexto)

**7 · Datos que faltaban**

> es un espacio comun de uso exclusivo quiere decir que lo usas vos pero lo mantiene el consorcio. Si hemos aceptado canjes. Exactamente ese libro

**8 · Qué aprendí, y un pedido nuevo** (acompañado del brochure de Casona 3 en PDF)

> lo que aprendi es la importancia de decirlo que no tiene que hacer el agente y lo importante de correr varias veces por los cambios generados en visitas confirmadas. Pensar el proceso del agente me ayudo a organizar mi propio proceso de venta y de la importancia de registrar cada proceso.
> Esta muy buena la idea es mas hay que poner recordatorios mensuales donde se vuelva a mandar la info de listas de precis brochure de venta y disponibilidades

Se omiten los mensajes de logística (iniciar sesión en GitHub, abrir el navegador). Qué hizo el
agente constructor con cada pedido, y qué se decidió distinto de lo pedido (por ejemplo, no
descargar copias no autorizadas de los manuales), está en `DECISIONES.md`.

## Qué funciona

**Las piezas del sistema:**

- **El contrato** (`prompts/system_prompt.md` v4 y `prompts/user_prompt.md` v2), con las seis piezas
  marcadas por nombre, más dos anexos: `conocimiento/proyecto.md` (la ficha del proyecto) y
  `conocimiento/playbook.md` (28 técnicas, cada una con su fuente verificada).
- **La herramienta real**: `consultar_tarifario` lee `herramientas/tarifario_vigente.csv`, derivado
  de las listas de precios internas sin comisiones ni compradores. Cada corrida registra qué filas
  del CSV consultó y el sha256 del tarifario.
- **La salida estructurada**: JSON validado por la API contra `sistema/esquema_ficha.json`, con los
  mismos trece campos en todas las corridas.
- **Catorce reglas verificadas en código** después de cada corrida (V1–V14: lista única, precios
  idénticos al tarifario, sin descuentos ni urgencia, fechas coherentes, firma, presentación,
  preguntas, largo, dirección y aviso de confirmación cuando hay visita, y vocabulario que la ficha
  desmiente). Si una falla, la corrida queda **BLOQUEADA** y el asesor no la envía.
- **El seguimiento del que no contesta**: cada ficha deja preparados tres toques —48 h, 7 días y 21
  días— con su aporte de valor y su texto. Los manda el asesor.
- **La transcripción de audios**, local (`herramientas/transcribir_audio.py`, Whisper).
- **El módulo 2**: `sistema/plan_mensual.py`, con su contrato en `prompts/variantes/`.
- **El front, probado**: el 12/9 corrió de punta a punta desde la página publicada, sin API, y pasó
  los doce chequeos de entonces (`corridas/vivo/`). Fue con la consulta de ejemplo y con el contrato
  v4, antes de las iteraciones 6 a 8.
- **El paquete mensual para colegas**: `sistema/paquete_colegas.py`, sin API, con la tarea programada
  de Windows «Copiloto DOMINIA - Paquete colegas» (día 1 de cada mes, 9:00). Probado el 11/9: generó
  `corridas/paquete_colegas/2026-09/` y el aviso en pantalla.

**Lo que se probó y anduvo**, con consultas reales anonimizadas de WhatsApp (`entradas/`):

- **Cuatro de inmobiliarias colegas y cinco de clientes** (una por audio), cada una guardada con lo
  que respondió el asesor en la realidad para poder comparar. Las corridas finales con el contrato
  vigente (`corridas/2026-09-11_1739_…` a `…_1745_…`) pasan los doce chequeos.
- **Tres corridas de referencia**, una por tipo de caso:

  | Corrida | Caso | Qué muestra |
  |---|---|---|
  | `corridas/2026-09-11_1741_C03-inmob-mostrar-hoy_opus-5.md` | Un colega quiere mostrar hoy a las 12:30 | Confirma la visita sin condiciones y adjunta la lista de Casona 2 (iteración 1) |
  | `corridas/2026-09-11_1745_C06-cliente-PBA-C3_opus-5.md` | Un cliente pide el PB A de Casona 3 desde la web | Se presenta, no da precio en el primer mensaje, pregunta cómo paga y propone la visita (iteraciones 2 a 4) |
  | `corridas/2026-09-11_1707_C09-cliente-audio-canje_opus-5.md` | Un proveedor, por audio, quiere comprar con canje | No confirma el canje; el borrador sale **bloqueado** por 124 palabras (una falla real que frenó el chequeo) |

- **Coherencia**: la misma consulta, escrita por tres personas distintas, da la misma lista, las
  mismas tres unidades y el mismo precio (`corridas/coherencia/`).
- **El plan de octubre** (`corridas/plan_mensual/`): cita sus once consultas como señales de demanda.

**Qué versión del contrato produjo cada corrida.** Cada archivo trae el sha256 de system + user:

| sha256 | Contrato | Corridas |
|---|---|---|
| `911bac10d216` | v1 + playbook v0 | humo (`pruebas/`) |
| `07325a31ef33` | v1 + playbook v1 | 01–09 y coherencia (16:48–17:07) |
| `cae72a3c838e` | v2 (iteración 1) | 03 y 04 de las 17:16 y 17:18 |
| `230238bc0c27` | v3 (iteración 2) | 01 y 06 de las 17:21 y 17:22 |
| `c59fefd13d70` | v3 + playbook v2 (iteración 3) | 06 y 05 de las 17:24 y 17:26 |
| `b856d022cd4b` | v4 (iteración 4) | 06 y 05 de las 17:28 y 17:29 |
| `d48ad9997e10` | v4 + user prompt v2 (iteración 5) | 04 de las 17:31 |
| `6a60ec936cf3` | Vigente: la anterior + ficha D-11 | 01–06 de las 17:39–17:45 |

Cómo se usa:

```bash
python sistema/copiloto.py entradas/consulta-06.md
```

```bash
python sistema/plan_mensual.py --mes 2026-10 --desde 2026-06-01 --hasta 2026-09-11
```

```bash
python sistema/paquete_colegas.py --mes 2026-10 --asesor Francisco
```

## Qué falta o qué falló

- **La comparación de modelos no se hizo.** El 11/9 a las 17:45 se terminó el crédito de la API y
  las corridas con Haiku 4.5 y Sonnet 5 fallaron con *«Your credit balance is too low to access the
  Anthropic API»* (`corridas/errores/`). Después se decidió no cargar más crédito (D-12). El sistema
  corre con Opus 5, el más caro de los tres, y no hay una prueba de que uno más chico no alcance.
- **Las corridas finales 07, 08, 09 y las de coherencia** quedaron sin repetir con el contrato
  vigente por la misma razón. Sus versiones con el contrato v1 están en `corridas/`.
- **El plan de octubre salió bloqueado.** Una de las dos piezas marcadas, la jornada con colegas
  que entrega las dos listas, se resolvió con la decisión D-13 (a los colegas se les mandan las dos,
  por separado). La otra es un falso positivo del chequeo, que se dejó así a propósito: un control
  por palabras no distingue *mencionar* de *ofrecer*.
- **Las iteraciones 6, 7 y 8 están aplicadas y sin corrida que las pruebe.** Salieron de la
  auditoría comercial del 12/9 (seguimiento, post-visita, dirección y confirmación, el otro camino
  para colegas, la implicancia por escrito, el precio con su plan, la persona antes que la consulta).
  Sin crédito de API no se pudieron correr; el front permite hacerlo sin API y esa corrida es la que
  falta. La lista de qué mirar en cada una está en `DECISIONES.md`.
- **La auditoría de formato encontró una contradicción real en este README**: decía «trece
  decisiones» cuando `DECISIONES.md` ya tenía catorce, un número de índice que quedó viejo.
  Corregido, y la lección quedó anotada: no escribir en un documento un número que otro documento
  puede cambiar.
- **El plan contó mal el stock**: *«14 unidades de 2 dorm y 9 de 3»* en Casona 3, cuando son 15 y 8.
  Ningún chequeo lo vio; se descubrió cuando el paquete mensual hizo la cuenta en código. La regla
  nueva del contrato (*«No cuentes unidades de memoria»*) no se pudo probar sin crédito.
- **Lo que ningún chequeo mide**: si una respuesta sirve. Las cuatro primeras corridas pasaron los
  diez chequeos de entonces, y una de ellas le proponía a un colega *«¿lo corremos a las 16?»* cuando
  ya tenía la visita confirmada para las 12:30. Se encontró comparando contra lo que respondió el
  asesor real, no con los chequeos.
- **La transcripción de audio se equivoca**: *«Toda es muy buena pérdida»* por «calidad». Se
  revisa a mano antes de correr el copiloto.
- **Todavía no se envió al cliente ningún borrador del copiloto**: las consultas son de junio a
  septiembre y ya tenían respuesta. La prueba de uso real queda para la primera consulta nueva.

## Qué aprendí

- **La importancia de decirle al agente lo que no tiene que hacer.** La pieza que más cambió los
  resultados fueron las **restricciones**: con una sola regla nueva («si ya propusieron día y hora,
  se confirma») el copiloto dejó de proponerle a un colega mover una visita que ya estaba confirmada
  (corrida 03, iteración 1).
- **Lo importante de correr varias veces.** Cada cambio arreglaba algo y movía otra cosa: después de
  arreglar las visitas confirmadas y agregar mi presentación, los mensajes se pasaron de largo y
  tuve que volver a correr y ajustar. Con una sola corrida no lo hubiera visto.
- **Pensar el proceso del agente me ayudó a organizar mi propio proceso de venta**: a quién le
  muestro qué lista, cuándo doy el precio y cuándo no, cómo le hablo a un colega y cómo a un cliente.
- **La importancia de registrar cada proceso.** Guardar lo que respondí yo en cada consulta real fue
  lo que me permitió ver dónde fallaba el agente aunque pasara todos los controles.
