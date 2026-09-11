# Copiloto para Asesores Comerciales de DOMINIA

> Trabajo final · Creación de Agentes de IA · MBA UCEMA · 2026 2T · Francisco Alloatti
> **Estado: en construcción** (11/9/2026). Este README se actualiza con cada iteración.

## Qué construí

Un agente que prepara la respuesta a cada consulta de un interesado en **Casona de los Arcos**
(DOMINIA, Manantiales, Córdoba). Lee la consulta —llegue por WhatsApp, Instagram, un portal o una
inmobiliaria colega—, consulta el tarifario vigente, ubica a la persona en el camino del comprador,
decide **qué lista le corresponde** (terminados de Casona 2 o pozo de Casona 3, nunca las dos),
propone hasta tres unidades con su precio exacto y deja un **borrador de mensaje** cuyo objetivo es
conseguir la visita. **El agente nunca le escribe al cliente**: el asesor revisa, corrige y envía
con su firma. Es para los asesores comerciales de DOMINIA y las inmobiliarias que venden el proyecto.

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

Qué hizo el agente constructor con cada pedido, y qué se decidió distinto de lo pedido (por
ejemplo, no descargar los manuales), está en `DECISIONES.md`.

## Qué funciona

- **El tarifario derivado** (`herramientas/tarifario_vigente.csv`): 8 unidades de Casona 2 y 28 de
  Casona 3, sin comisiones ni compradores. Se regenera con `python herramientas/derivar_tarifario.py
  <lista Casona 2> <lista Casona 3>`.
- **El contrato** (`prompts/system_prompt.md` y `prompts/user_prompt.md`, versión 1), con las seis
  piezas marcadas, más dos anexos de conocimiento: la ficha del proyecto y el playbook comercial.
- **El ejecutor** (`sistema/copiloto.py`): corre una consulta, deja que el modelo use la herramienta,
  valida diez reglas duras y guarda la corrida completa con tokens y costo.
- **La prueba de humo** del 11/9 (`pruebas/`, con una consulta inventada): pasó de punta a punta y
  los diez chequeos en el primer intento.

Cómo se usa:

```bash
python sistema/copiloto.py entradas/consulta-01.md
```

## Qué falta o qué falló

- **Las tres corridas reales** con consultas anonimizadas: todavía no se hicieron.
- **El playbook v1** con los manuales pedidos: en investigación, solo con fuentes verificables.
- **El módulo 2** (plan mensual de ventas y publicaciones): sin empezar.
- **La comparación de modelos** y el análisis económico: hay una sola corrida de humo con Opus 5,
  que costó USD 0,2145.
- **Primera falla detectada** en la prueba de humo: el agente consultó las dos listas aunque ya
  había decidido cuál correspondía (detalle en `DECISIONES.md`).

## Qué aprendí

_(Se completa al cerrar.)_
