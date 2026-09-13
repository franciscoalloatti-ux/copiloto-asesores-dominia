# DECISIONES — la historia de la construcción

> Registro cronológico y **aditivo**: lo que se decidió no se borra; si cambia, se agrega una
> entrada nueva que lo corrige. Cada iteración del contrato lleva el error textual que la motivó,
> la pieza que se tocó y el commit donde quedó.

---

## Viernes 11/9/2026

### D-01 · El tema

Se evaluaron cinco candidatos contra la rúbrica y contra el tiempo disponible (dos días y medio):
copiloto comercial de Casona de los Arcos, prefactibilidad de terrenos, costos de obra v2, el Pool
de los Miércoles y el legajo técnico de obra.

**Elegido: el copiloto comercial.** Resuelve un problema real y actual (36 unidades a la venta), la
herramienta existe (la lista de precios), las entradas son reales (consultas de interesados) y las
reglas de negocio se vuelven restricciones con consecuencias concretas. **Descartados:** el Pool
(la próxima jornada es el 16/9, después del cierre) y el legajo (fotos más máquina de estados no
entran en dos días).

### D-02 · El alcance: dos módulos, uno principal

El responsable pidió un sistema **completo**: responder consultas *y* armar el plan de ventas y
publicaciones mensual. Son dos tareas con entrada, frecuencia y salida distintas.

**Decisión:** el sistema principal —el de las tres corridas— es el **copiloto de consultas**, y el
camino del comprador, la clasificación y la estrategia van adentro de él. El **plan mensual es el
módulo 2**, con su propio contrato en `prompts/variantes/` y su propio esquema. Motivo: la consigna
pide tres corridas con el **mismo esquema de salida**; mezclar las dos tareas lo rompe.

### D-03 · Los manuales

El responsable pidió basar la estrategia en ocho manuales de ventas inmobiliarias y propuso
«descargarlos de la web». No están en la computadora del proyecto.

**Decisión:** **no se descargan copias de libros con derechos de autor.** Se investigan fuentes
públicas y legítimas (editorial, autor, entrevistas, reseñas) y cada técnica que entra al playbook
se parafrasea y lleva su fuente. Un libro que no se pueda verificar queda sin técnicas atribuidas:
es preferible un hueco declarado a una cita inventada. El playbook arranca en su **versión 0**, con
las técnicas de la Academia Casona (formación interna ya armada: SPIN, intereses y posiciones, los
seis datos, cerrar hacia la visita).

### D-04 · La herramienta: un tarifario derivado, no la planilla interna

Las listas de precios originales tienen comisiones, hojas por inmobiliaria y nombres de
compradores. **El agente no las ve.** `herramientas/derivar_tarifario.py` toma solo las columnas
comerciales y escribe `herramientas/tarifario_vigente.csv`. Las planillas quedan fuera del
repositorio (`.gitignore`).

Salida textual de la primera derivación:

```text
LISTA DE PRECIO CASONA DE LOS ARCOS (Nº5)  - ENERO 2025 (01/10/2025)
Casona 2: 8 unidades · USD 1,870,759
Casona 3: 28 unidades · USD 7,259,368 · disponibles 27
```

**Hallazgo:** la lista de Casona 3 incluye el **PB H**, que DOMINIA no ofrece. Queda en el
tarifario con `disponible = no` (si alguien lo pide, el agente sabe que existe pero no lo ofrece),
y el stock ofrecible de Casona 3 es de 27 unidades, no 28.

### D-05 · Arquitectura: API, una herramienta y reglas verificadas en código

El copiloto corre contra la API de Anthropic (`sistema/copiloto.py`) con **una herramienta propia**,
`consultar_tarifario`, y salida en JSON validada por esquema. Después de cada corrida, el ejecutor
revisa **diez reglas duras** (V1–V10: lista única, precios idénticos al tarifario, sin descuentos,
firma exacta, máximo dos preguntas…) y marca la ficha como *aprobada para revisión* o *bloqueada*.

Por qué así y no pegando la consulta en un chat:

1. **La herramienta es real y deja rastro**: cada corrida guarda qué filas del CSV consultó.
2. **Los tokens son medidos, no estimados**: la API devuelve el consumo de cada vuelta.
3. **Las reglas más caras de romper no dependen solo del prompt**: si el modelo mezcla listas o
   cambia un precio, el código lo detecta antes de que el asesor copie el mensaje.

### D-06 · Sin respaldo automático de modelo

La API ofrece redirigir a otro modelo si el principal rechaza una consulta. **No se activa**: cada
corrida tiene que registrar qué modelo respondió, porque la elección de modelo se va a decidir
comparando corridas. Un rechazo se guarda como error en la corrida.

### Prueba de humo · 11/9 16:17 · `pruebas/corridas/2026-09-11_1617_HUMO-01_opus-5.md`

Consulta **inventada** (pareja que alquila, ambos en relación de dependencia, pregunta precio y
crédito) para probar la cañería. No cuenta como corrida real.

- Funcionó de punta a punta en el primer intento: el agente asignó `casona_2_terminados`, propuso
  PB E, 1º G y PB C con los precios exactos del tarifario, y el borrador pasó los diez chequeos.
- **Hallazgo 1 (costo y riesgo):** después de asignar Casona 2, hizo una segunda consulta con
  `edificio: "todos"` y trajo 19 unidades, incluidas las de Casona 3:

  ```text
  2. consultar_tarifario({"edificio": "todos", "dormitorios": 2, ...}) → 19 unidad(es): Casona 2 PB B (fila 2), ...
  | 2 | 8458 | 0 | 10990 | 3463 | end_turn |
  ```

  Esa vuelta metió 8.458 tokens de entrada que no hacían falta, y puso la lista que no correspondía
  delante del modelo. La causa está en la **tarea**, paso 5: *«Hacelo siempre antes de nombrar una
  unidad o un precio, aunque la lista no esté asignada: sirve para saber qué existe»*.
- **Hallazgo 2 (costo):** USD 0,2145 por consulta con Opus 5, con 3.830 tokens de salida. Queda
  como línea de base para la comparación de modelos.

**Candidato a iteración 1** (se decide con las corridas reales): consultar solo el edificio de la
lista asignada, y `todos` únicamente cuando la lista está `sin_asignar_aun`.

### D-07 · Contexto corregido por el responsable: forma de venta y avance comercial

La ficha del proyecto decía *«Casona 1 y Casona 2 están entregados y habitados»* y no decía cómo se
instrumenta la venta de Casona 3. Se preguntó al responsable, que respondió:

> Casona 3 se vende con boleto de compraventa financiada a plazo de obra. Casona 1 esta totalmente
> vendida, Casona 2 estan vendidos 20 de 28 y el complejo se cierra con la tercer torre con lo cual
> seria muy dificil no terminar con el compromiso en un complejo tan consolidado.

Qué cambió en `conocimiento/proyecto.md` (pieza **contexto**):

- Casona 3 se vende con **boleto de compraventa financiado**, con precio fijado en USD: **no es un
  fideicomiso al costo**. Se agregó la respuesta a «¿es un fideicomiso?».
- El avance comercial (Casona 1 vendida en su totalidad, Casona 2 con 20 de 28 vendidas) pasa a ser
  la evidencia para «¿y si se para la obra?» (T-12).
- El argumento del responsable (*«sería muy difícil no terminar»*) **no se copió como tal**: el
  copiloto presenta los hechos y los invita a comprobar en la visita, pero no garantiza la
  terminación. Una garantía por escrito es justamente lo que prohíbe la restricción 6.

### D-08 · Los manuales: PDFs gratuitos sí, copias no autorizadas no

El responsable insistió: *«los manuales tienen que estar en pdf en internet para leerlos
aunquesea»*. Se amplió la búsqueda a **PDFs que el autor o la editorial publiquen gratis**
(capítulos de muestra, vista previa de Google Books, material de colegios profesionales). Las copias
subidas sin autorización (Scribd, sitios de descarga, Drives de terceros) siguen excluidas: que un
PDF sea accesible no quiere decir que su publicación esté autorizada.

### D-09 · Playbook v1: lo que se pudo verificar de los ocho manuales

El subagente de investigación terminó (resultado completo en `conocimiento/fuentes_manuales.md`,
que **no** se carga en el prompt: es el respaldo). Resultado:

| | Manuales |
|---|---|
| **Identificados (5)** | Villarroya, *El cierre de la venta inmobiliaria*; Harkins y Hollihan, *Everybody Wins*; Migliorisi, *El camino del real estate*; Woscoboinik, *Marketing para inmobiliarios*; Tabakman, *Fideicomisos al costo* |
| **Probable (1)** | *Comunicar para vender* sería de Massimo Forte, en portugués — a confirmar con el responsable |
| **Sin identificar (2)** | «📓 La Biblia del Real Estate» y «📈 Marca Personal y Cierre de Alto Impacto»: son nombres de cuadernos de NotebookLM, no títulos de libros |
| **Leídos completos o en muestra oficial** | Migliorisi (PDF gratuito del autor), prólogo y prefacio de *Everybody Wins* (muestra de la editorial), Ley 9445 y Código de Ética del Colegio de Corredores de Córdoba |

Tres correcciones que salieron de verificar en vez de suponer:

1. **Everybody Wins no es de Dave Liniger.** Lo escribieron Phil Harkins y Keith Hollihan; Liniger
   firma el prólogo. El pedido original lo atribuía a él.
2. **Everybody Wins no es un manual de técnica de venta**: es un libro de cultura y estrategia de
   RE/MAX. Aporta dos ideas (la satisfacción del comprador como base del éxito del agente, y la
   marca única en todos los canales), no técnicas de conversación.
3. **De Woscoboinik solo se verificó el índice.** Se usa como tema («el precio se funda en la
   tasación»), no como técnica atribuida.

Qué cambió en `conocimiento/playbook.md` (pieza **contexto**, anexo del system prompt): diez
técnicas nuevas (T-17 a T-26), entre ellas **T-19 «¿es un fideicomiso?»** y **T-20 «¿qué garantías
tengo?»**, que salen del contexto nuevo de D-07. La restricción 6 del system prompt ya prohibía
prometer lo que no está en la ficha; ahora la ficha no nombra el seguro del art. 2071 ni la fecha
cierta del boleto, porque **DOMINIA no los confirmó**, así que el copiloto no puede usarlos como
garantía. El chequeo V7 del ejecutor suma las frases de urgencia artificial («últimas unidades»,
«decidí hoy») y las garantías no confirmadas.

Quedan cuatro preguntas para DOMINIA / legal antes de que el copiloto pueda usarlas: si Casona 3
tiene el seguro del art. 2071 CCyC, si el boleto tiene fecha cierta, cómo se calcula la cuota en
pesos ajustada por CAC y la base legal de ese ajuste en un contrato en dólares.

### Corridas reales 01–04 · 11/9 16:48–16:50 · contrato v1 + playbook v1

Cuatro consultas reales de **inmobiliarias colegas**, transcriptas de capturas de WhatsApp y
anonimizadas (`entradas/consulta-01.md` a `04.md`). Cada entrada guarda también **lo que respondió
el asesor en la realidad**, en una sección que el ejecutor no le pasa al modelo: sirve para comparar.

| Corrida | Qué pidió el colega | Qué respondió el asesor real | Qué propuso el copiloto | Chequeos | USD |
|---|---|---|---|---|---|
| 01 | Ir mañana por la siesta a ver un 1 dormitorio | «Dale obvio!» → visita a las 14:30 | Confirma, ofrece 15 o 16:30 y pide uso y forma de pago del cliente | 10/10 | 0,1860 |
| 02 | Algo en planta baja de 2 o 3 dormitorios | Audio de 0:29 → el colega entiende «torre 2, a estrenar» | Hay 2 dormitorios en PB; **3 en PB no existe**; pide perfil; ofrece dos horarios | 10/10 | 0,1692 |
| 03 | Mostrar **hoy a las 12:30** | Audio + código de acceso: visita aceptada | «¿Te queda mejor 12:30 o lo corremos a las 16?» | 10/10 | 0,1635 |
| 04 | ¿Hay 2 dormitorios disponibles? | Audio + **la lista N°5 completa de Casona 2** en PDF → «Fran genial» | Dice que hay en dos formatos, pide perfil, no manda lista | 10/10 | 0,1034 |

**Los diez chequeos pasaron en las cuatro, y aun así hay fallas.** Los chequeos miden reglas; no
miden si la respuesta sirve. Lo que muestran las cuatro corridas contra lo que pasó en la realidad:

1. **Falla grave · corrida 03: el copiloto puso en riesgo una visita que ya estaba ganada.** El
   colega propuso mostrar hoy a las 12:30 y el borrador contesta:

   > ¿Te queda mejor 12:30 o lo corremos a las 16 y llegamos con todo armado? Confirmame por acá.

   Ofrecer correrla para «llegar con todo armado» antepone la necesidad del copiloto (tener los
   datos para asignar la lista) al objetivo de todo el sistema (la visita). El asesor real aceptó
   sin condiciones. La causa está en el contrato: la tarea obliga a asignar lista y la restricción 8
   obliga a cerrar con **dos horarios**, aunque el otro ya haya puesto uno.

2. **Tono y largo con colegas.** Los cuatro borradores tienen entre 90 y 110 palabras, abren con una
   fórmula («Hola! Todo bien, gracias por escribir») y firman «Francisco, Asesor Comercial de
   DOMINIA» a colegas que lo tratan de «Fran». El asesor real contestó con cinco palabras. La
   restricción 8 limita el largo solo en WhatsApp e Instagram, y las consultas de colegas llegan
   por WhatsApp pero se registran como canal `inmobiliaria`: el límite no se aplicó.

3. **Con colegas, el copiloto condiciona la información al perfil del cliente final; el asesor real
   manda la lista.** En la 04 el asesor mandó la lista de Casona 2 completa y la colega respondió
   «Fran genial». El copiloto no mandó nada hasta saber cómo paga el cliente. Las dos cosas tienen
   fundamento: la restricción 12 (lista única también con colegas) contra la T-26 (información
   completa a los colegas, Código de Ética). **Es una decisión de negocio, no de prompt**: queda
   para el responsable.

4. **Las cuatro corridas consultaron `edificio: "todos"`**: es lo que el contrato indica cuando la
   lista no está asignada. La 03 trajo el tarifario entero (35 unidades, 12.548 tokens de entrada).

5. **El caché funciona entre corridas**: la 01 escribió 13.445 tokens en caché y las tres siguientes
   los leyeron (26.890 cada una, dos vueltas) a un décimo del precio. Por eso la 04 costó USD 0,1034.

Total de las cuatro: **USD 0,6221**.

### Corridas reales 05–09 y prueba de coherencia · 11/9 16:57–17:07 · contrato v1

Cinco consultas reales de **clientes finales** (cuatro por texto y una por audio) y dos
repeticiones de la consulta 06, escritas palabra por palabra por otras dos personas.

| Corrida | Qué pidió | Lista | Unidades | Chequeos | USD |
|---|---|---|---|---|---|
| 05 | «Me interesa 1° E (2 Dorm · 1 Baño) de Casona III», a las 02:39 | Casona 3 | 1º E, 1º G, PB E | 10/10 | 0,1397 |
| 06 | «Me interesa PB A (2 Dorm · 2 Baños) de Casona III», a las 02:19 | Casona 3 | PB A, PB C, 1º A | 10/10 | 0,1653 |
| 07 | «Busco alojamiento mensual para 2 personas» | sin asignar | — | 10/10 | 0,1359 |
| 08 | PB B **o PB H** de Casona III, «cualquier de los dos» | Casona 3 | PB B, PB D, PB F | 10/10 | 0,1631 |
| 09 | Audio: un proveedor de carpintería quiere comprar y «tomar metros» a cambio de trabajos | Casona 3 | — | **9/10 · BLOQUEADA** | 0,1940 |
| Coherencia 2 | Idéntica a la 06, otra persona | Casona 3 | PB A, PB C, 1º A | 10/10 | 0,1371 |
| Coherencia 3 | Idéntica a la 06, tercera persona | Casona 3 | PB A, PB C, 1º A | 10/10 | 0,1383 |

**Lo que funcionó:**

- **Coherencia.** Las tres consultas idénticas dieron la misma etapa, el mismo perfil, la misma
  lista, las mismas tres unidades y el mismo precio (USD 247.582). Cambió la redacción y, en una,
  el segundo horario («10 o 12» en vez de «10 o 11»). Es lo que el responsable pidió priorizar:
  *«lo importante mas que el tiempo es la coherencia y la efectividad de la respuesta»*.
- **Lo que no existe.** A quien buscaba alojamiento mensual, el borrador le dice de frente *«en
  Casona de los Arcos vendemos unidades, no tenemos alquileres ni alojamiento por mes»*. Al que pidió
  el PB H le ofrece los 1 dormitorio en planta baja que sí están disponibles.
- **Lo que no está en la ficha.** El canje por carpintería: *«no te lo puedo confirmar por acá: lo
  converso con DOMINIA y te aviso»*, con una alerta para separar la negociación de proveedor de la
  compra.
- **Primer bloqueo real.** La 09 salió con 124 palabras y el ejecutor la frenó:

  ```text
  ❌ V10 Menos de 120 palabras en WhatsApp o Instagram — 124 palabras · canal whatsapp
  Resultado: BLOQUEADA
  ```

  El asesor tiene que recortarla antes de enviarla. Es la mitigación funcionando: el modelo rompió
  una regla de formato y el código lo detectó.
- **La herramienta elige bien el alcance cuando la lista es clara.** De la 05 a la 09 consultó solo
  `Casona 3`, nunca `todos`. El hallazgo del humo aparece solo cuando la lista está sin asignar,
  que es lo que el contrato indica.

**Lo que falló o no está bien resuelto:**

1. **Contradicción dentro del playbook sobre el precio en el primer mensaje.** A leads desconocidos
   que escribieron a las 2 de la mañana, el borrador les da precio y plan completos:

   > Precio de lista USD 247.582, con 40% de anticipo, 40% en 30 cuotas (podés elegir dólares o
   > pesos ajustados por CAC) y 20% contra entrega

   El modelo siguió la tabla de *qué se muestra* («una unidad ancla que responde a lo que pidió»),
   pero la T-06 dice *«nunca se da un precio antes de tener el número contra el que se lo quiere
   comparar»*. Las dos reglas están en el mismo anexo y se contradicen. En lo visible de las
   capturas, el asesor real contestó sin precio: presentación, contexto del complejo, «disponible en
   cuotas», cochera y patio.
2. **La lista se asigna por el botón que tocó, no por cómo paga.** En 05, 06 y 08 se asigna Casona 3
   porque el mensaje pre-armado dice «Casona III», y la pregunta que se hace es «¿para vivir o como
   inversión?». La pregunta que define la lista (T-03, «¿cómo pensabas pagarlo?») no se hace. Si esa
   persona califica a crédito, la T-13 dice que le conviene el terminado, y nadie se lo pregunta.
3. **Jerga interna filtrada al cliente.** En la 08: *«El PB H no integra el stock a la venta»*. Es el
   texto del campo `observacion` del tarifario, copiado tal cual. A un cliente se le dice «no está
   disponible».
4. **El asesor no se presenta.** Los mensajes reales abren con *«Hola, buen día, cómo estás? Mi
   nombre es Francisco. El edificio es el último de un complejo cerrado de tres torres…»*. El
   pedido original decía *«Me quiero presentar como que pueda agregar el nombre el scesor comercial
   y luego que diga que es asesor comercial de DOMINIA»*. El copiloto solo firma al final.
5. **Un canal contradice al tarifario.** La página del proyecto tiene un botón de WhatsApp para el
   PB H, que no se ofrece. No es un problema del copiloto, pero él lo detectó y lo marcó en alertas.
6. **Un dato real que la ficha no tiene.** El asesor escribió que el PB A tiene *«un patio privado
   que lo mantiene el consorcio»*. El copiloto no lo sabe; hay que confirmarlo antes de sumarlo.

**La herramienta de audio.** `herramientas/transcribir_audio.py` corre Whisper *small* local: 44
segundos de audio, 45 de proceso, y el audio no sale de la computadora. Cometió errores que
cambiaban el sentido (*«Toda es muy buena pérdida con super buen precio»* por «calidad») y se
corrigieron contra la transcripción de WhatsApp. La transcripción es un paso con revisión humana,
no una entrada confiable.

### D-10 · Decisiones del responsable sobre las fallas (11/9, 17:12)

Se le presentaron las fallas y cuatro preguntas. Respuestas textuales:

- **Colegas:** *«lo que pida, si esta buscando en poso lista casona 3 y si no la 2. Pero esta bueno lo
  del perfil de cliente. LA casona 3 es un excel que lo mandaria en formato de lista tambien»*.
- **Presentación:** presentarse al inicio **y** firmar al final.
- **Precio en el primer mensaje a un cliente:** *«Sin precio como recomendas y siguiendo los pasos
  de los manuales. Justamente quiero transformar asesores comunes en los mejores»*.
- **Plan:** tres iteraciones, una pieza por vez, en este orden: restricciones → formato → contexto.

---

## Iteración 1 · pieza: RESTRICCIONES · contrato v1 → v2 · 11/9 17:15

**Qué falló** (corrida 03, v1, `corridas/2026-09-11_1650_C03-inmob-mostrar-hoy_opus-5.md`). El colega
propuso mostrar hoy a las 12:30 y el borrador respondió:

> ¿Te queda mejor 12:30 o lo corremos a las 16 y llegamos con todo armado? Confirmame por acá.

Y en la 04 (v1), a una colega que preguntó si había 2 dormitorios, el copiloto no le mandó nada:
la lista quedó `sin_asignar_aun` hasta que respondiera el perfil de su cliente.

**Qué se cambió** (solo la pieza *restricciones* de `prompts/system_prompt.md`):

- **Nueva restricción 13 — «La visita ya propuesta se confirma»**: si el interesado o el colega ya
  propuso día y hora, se confirma sin condiciones y sin ofrecer otro horario; lo que falte se pide
  en paralelo, nunca como requisito.
- **Restricción 8**: el cierre del borrador es la confirmación, si la visita ya está propuesta.
- **Restricción 12 reescrita** con la decisión D-10: al colega se le da la lista que pide (Casona 3
  si busca pozo o cuotas; si no, Casona 2), nunca las dos, y el perfil del cliente se pide sin
  condicionar la lista a esa respuesta.

**Qué cambió en la salida** (mismas entradas, contrato v2):

| | v1 | v2 |
|---|---|---|
| **03** · `2026-09-11_1716_…` | «¿Te queda mejor 12:30 o lo corremos a las 16…?» · lista sin asignar | *«te confirmo: hoy 12:30 en Costanera de La Cañada 4140»* · lista `casona_2_terminados` · el perfil se pide «para tenerte preparado lo justo» |
| **04** · `2026-09-11_1718_…` | No manda lista, pide perfil primero | *«Te adjunto la lista con superficies, precios y expensas para que la trabajes con tu cliente»* · `revisar_antes_de_enviar`: *«Adjuntar vos el PDF/planilla de la lista de Casona 2»* |

La v2 hace lo mismo que hizo el asesor real en las dos: aceptar la visita y mandar la lista de Casona 2.

**Lo que la iteración 1 no arregló, y un error nuevo:**

- El tono con colegas sigue igual (*«Hola! Todo bien por acá, gracias por escribir 👍»*) y la
  presentación no aparece: es la iteración 2.
- **Error nuevo en la 04 (v2): fechas con el día de la semana equivocado.** La consulta es del
  jueves 10/9/2026 y el borrador propone:

  > ¿te sirve el jueves 17 hs o el sábado 10 hs?

  con `propuesta_de_visita`: *«Jueves 11/9 a las 17:00 o sábado 13/9 a las 10:00»*. El 11/9/2026 es
  **viernes** y el 13/9 es **domingo**. El modelo calcula mal el día de la semana a partir de la
  fecha. Ninguno de los diez chequeos lo detecta. Queda para una iteración propia: que el ejecutor
  le pase el calendario y que un chequeo nuevo verifique cada par «día + fecha».

## Iteración 2 · pieza: FORMATO · contrato v2 → v3 · 11/9 17:20

**Qué falló** (v1 y v2). Ningún borrador presentaba al asesor, que era parte del pedido original, y
todos abrían con la misma fórmula: *«Hola! Todo bien por acá, gracias por escribir»*. El asesor
real abre así: *«Hola, buen día, cómo estás? Mi nombre es Francisco. El edificio es el último de un
complejo cerrado de tres torres…»*.

**Qué se cambió** (solo la pieza *formato*): el campo `borrador_mensaje` pasa a tener una estructura
en seis pasos: saludo y presentación → contexto en una línea (solo primer contacto con cliente) →
respuesta a lo que preguntó → hasta dos preguntas → próximo paso → firma. Sin fórmulas repetidas ni
emojis. El ejecutor suma el chequeo **V11**: el nombre del asesor tiene que estar en la primera línea.

La pieza *ejemplos* **no se tocó**, aunque su borrador de ejemplo no tiene presentación. Se quería
ver cuál de las dos pesaba más.

**Qué cambió en la salida:**

| | Antes | v3 |
|---|---|---|
| **01** (colega) · `2026-09-11_1721_…` | *«Hola! Todo bien, gracias por escribir.»* | *«Hola! Francisco, de DOMINIA, por acá.»* · 10/10 + V11 |
| **06** (cliente) · `2026-09-11_1722_…` | *«Hola! Gracias por escribir.»* | *«Hola, buen día! Soy Francisco, asesor comercial de DOMINIA. / Casona de los Arcos es un complejo cerrado de tres torres en Manantiales I…»* · **BLOQUEADA** |

1. **La presentación funcionó en las dos**, y pesó más la instrucción de formato que el ejemplo sin
   presentación: el modelo no copió el ejemplo.
2. **Pero la iteración rompió dos reglas en la 06**, y los chequeos la frenaron:

   ```text
   ❌ V9 Como máximo dos preguntas — 3 pregunta(s)
   ❌ V10 Menos de 120 palabras en WhatsApp o Instagram — 125 palabras · canal whatsapp
   Resultado: BLOQUEADA
   ```

   - **Largo:** sumar presentación y contexto (unas 35 palabras) a un borrador que ya traía precio y
     plan completos lo pasó del límite. Las dos piezas compiten por el mismo espacio.
   - **Preguntas:** el formato dice *«hasta dos preguntas»* y después *«el próximo paso»*. El modelo
     leyó que la pregunta de la visita no contaba y escribió *«¿Es para vivir o como inversión? ¿Lo
     decidís solo o con alguien más?»* más *«¿te queda mejor el sábado a las 10 o a las 12?»*. La
     ambigüedad está en el contrato, no en el modelo.

   Lo que hay que sacar para que entre es el precio y el plan del primer mensaje, que es justamente
   la iteración 3. Se deja así a propósito para ver si la iteración 3 lo resuelve sola.

## Iteración 3 · pieza: CONTEXTO (playbook v1 → v2) · 11/9 17:24

**Qué falló** (corridas 05, 06 y coherencia, v1). A leads desconocidos, el primer mensaje daba
precio y plan completos (*«Precio de lista USD 247.582, con 40% de anticipo…»*), porque la tabla
*qué se muestra* permitía «una unidad ancla» y la T-06 decía lo contrario. Y la lista se asignaba
por el botón que tocó sin preguntar cómo paga.

**Qué se cambió** (solo `conocimiento/playbook.md`, anexo del system prompt; el system prompt no se tocó):

- **T-27 · Al cliente, el primer mensaje va sin precio**: disponibilidad, diferencial y forma de pago
  en términos generales; el precio, cuando lo pide (una sola cifra) o en la visita. A un colega sí
  se le manda la lista. Es la decisión D-10 del responsable.
- **T-28 · Si la lista salió del botón, la primera pregunta es cómo paga** (T-03), para poder aplicar
  la T-13 si califica a crédito.
- La tabla *qué se muestra* se separó para el cliente final y se sacó la «unidad ancla».

**Qué cambió en la salida:**

| | v3 (antes) | v3 + playbook v2 |
|---|---|---|
| **06** · `2026-09-11_1724_…` | *«Precio de lista USD 247.582, con 40% de anticipo…»* · 125 palabras | *«Se paga con un anticipo y cuotas mensuales durante la obra, en dólares o en pesos ajustados.»* · primera pregunta: *«¿cómo pensabas pagarlo?»* · **117 palabras** |
| **05** · `2026-09-11_1726_…` | *«Precio USD 241.706, con 40% de anticipo…»* | Sin precio · *«Para pasarte el plan que realmente te sirva, ¿cómo pensabas pagarlo?»* |

El precio salió de los dos y la pregunta que define la lista pasó a ser la primera: el copiloto
citó T-27 y T-28 en su estrategia. **Pero las dos siguen bloqueadas**, cada una por una regla distinta:

```text
06 · ❌ V9 Como máximo dos preguntas — 3 pregunta(s)
05 · ❌ V10 Menos de 120 palabras en WhatsApp o Instagram — 127 palabras · canal whatsapp
```

La hipótesis de la iteración 2 era que, sacando el precio, el borrador iba a entrar solo. **Salió
a medias:** la 06 bajó de 125 a 117 palabras, pero la 05 quedó en 127, porque el modelo usó el
espacio liberado para contar el recorrido de la visita. Y el problema de las tres preguntas no
depende del precio: está en la ambigüedad del formato («hasta dos preguntas» + «el próximo paso»).
Las dos cosas son de la pieza *formato*: van a la iteración 4.

## Iteración 4 · pieza: FORMATO (otra vez) · contrato v3 → v4 · 11/9 17:28

**Qué falló** (iteración 3): *«❌ V9 Como máximo dos preguntas — 3 pregunta(s)»* en la 06 y *«❌ V10
… — 127 palabras»* en la 05.

**Qué se cambió** (solo la pieza *formato*):

- Los pasos 4 y 5 se fusionaron: **dos signos de pregunta en todo el mensaje, incluida la del
  próximo paso**. Si el próximo paso es elegir horario, queda lugar para una sola pregunta más.
- **Presupuesto de largo explícito**: 80 a 110 palabras contando presentación y firma; el recorrido
  de la visita se cuenta en la visita.

**Qué cambió en la salida:**

| | v3 + playbook v2 | v4 |
|---|---|---|
| **06** · `2026-09-11_1728_…` | 3 preguntas · BLOQUEADA | *«¿cómo pensabas pagarlo: contado, crédito o en cuotas?»* + *«¿te queda mejor el sábado a las 10 o a las 11?»* · 107 palabras · **aprobada** |
| **05** · `2026-09-11_1729_…` | 127 palabras · BLOQUEADA | 116 palabras · **aprobada** |

Las dos pasan los once chequeos. La 05 quedó en 116 palabras: pasa el límite duro de la restricción
8 (120), pero se pasa del presupuesto de formato (110). El presupuesto orienta, el chequeo frena:
**se deja así** y se registra, porque subir el chequeo a 110 bloquearía borradores buenos por seis
palabras.

**Qué se aprendió de las iteraciones 2 a 4.** Una pieza por vez no quiere decir que las piezas sean
independientes. La iteración 2 (formato) agregó texto y rompió el largo que fija una restricción; la
3 (contexto) liberó espacio y el modelo lo volvió a llenar; la 4 tuvo que volver sobre el formato
para fijar un presupuesto. **El largo de un mensaje se reparte entre piezas, y alguien tiene que
fijar el total.**

## Iteración 5 · pieza: CONTEXTO del pedido (user prompt v1 → v2) + chequeo V12 · 11/9 17:31

**Qué falló** (corrida 04 con contrato v2, `corridas/2026-09-11_1718_C04-inmob-2dorm_opus-5.md`): la
consulta es del jueves 10/9/2026 y la propuesta de visita decía *«Jueves 11/9 a las 17:00 o sábado
13/9 a las 10:00»*. El 11/9 es viernes y el 13/9 es domingo. El modelo calcula el día de la semana de
memoria, y ningún chequeo lo miraba.

**Qué se cambió:**

- **User prompt** (el pedido puntual, no el system): el ejecutor calcula en código el día de la
  semana de la consulta y un **calendario de nueve días**, y se los pasa con la instrucción *«Usá
  estos pares día-fecha tal cual: no calcules días de la semana por tu cuenta»*.
- **Chequeo V12** en el ejecutor: busca cada «día dd/mm» del borrador y de la propuesta de visita y
  verifica que el día corresponda a la fecha.

**Primero se probó el chequeo contra la corrida que había fallado**, sin volver a llamar al modelo:

```text
('V12', False, '«jueves 11/9» es viernes; «sábado 13/9» es domingo')
```

Detecta el error real. **Después, la misma entrada con el contrato nuevo**
(`2026-09-11_1731_C04-inmob-2dorm_opus-5.md`):

> ¿Te queda mejor el viernes 11 a las 10 o el sábado 12 a las 11?

con `propuesta_de_visita`: *«Viernes 11/9/2026 a las 10 o sábado 12/9/2026 a las 11»* → V12: *«2
fecha(s) verificada(s)»*. Doce chequeos en verde.

**Por qué las dos cosas y no una.** El calendario en el prompt **previene** el error; el chequeo
**lo detecta si igual ocurre**. Es la regla que ya se venía aplicando (D-05): lo que es caro de
equivocar no puede depender solo del prompt. Un borrador con la fecha mal manda al interesado un
domingo a un complejo cerrado.

### D-11 · Tres datos del responsable y dos correcciones de la herramienta (11/9, 17:40)

Respuestas textuales a las preguntas pendientes:

> es un espacio comun de uso exclusivo quiere decir que lo usas vos pero lo mantiene el consorcio.
> Si hemos aceptado canjes. Exactamente ese libro

- **Jardín de planta baja** → `conocimiento/proyecto.md`: es un *espacio común de uso exclusivo* que
  mantiene el consorcio. **Corrige un error que venía de antes**: el tarifario llamaba a la columna
  `m2_jardin_privado` y los borradores escribían *«jardín privado propio»* (corrida 06, v3). En
  sentido legal no es privado. La columna pasa a llamarse `m2_jardin_uso_exclusivo`.
- **Canjes** → la ficha dice que DOMINIA los ha aceptado y que se evalúan caso por caso; el copiloto
  puede decir que se conversan, pero no los confirma ni les pone valor.
- **Comunicar para vender** → confirmado: es el libro de Massimo Forte.
- **Jerga en la herramienta** (falla 3 de las corridas 05–09): la observación del PB H pasa de *«No
  integra el stock a la venta (decisión DOMINIA)»* a *«No está a la venta»*. Lo que devuelve la
  herramienta el modelo lo puede copiar al cliente, así que se escribe como se le diría a un cliente.

## Módulo 2 · plan mensual · primera corrida · 11/9 17:44

El módulo 2 tiene su propio contrato (`prompts/variantes/plan_mensual_system.md` y `_user.md`, con
las seis piezas), su esquema (`sistema/esquema_plan.json`) y su ejecutor (`sistema/plan_mensual.py`).
Suma una segunda herramienta, **`resumen_consultas`**, que lee el registro de `entradas/`: **el
módulo 1 alimenta al 2**. Las consultas que el copiloto responde son la señal de demanda con la que
se planifica el mes siguiente.

**Corrida:** plan de octubre 2026 con las consultas del 1/6 al 11/9
(`corridas/plan_mensual/2026-09-11_1744_plan-2026-10_opus-5.md`, USD 0,4906). El plan lee las 11
consultas y el tarifario completo, y cada señal de demanda cita sus consultas:

- *«tres personas distintas pidieron exactamente la misma unidad desde el botón de la web en cuatro
  días»* (C06, COH-PBA-2, COH-PBA-3) → prioriza la planta baja de Casona 3 y ordena PB C, PB B, PB E y
  PB G como alternativas visibles, porque *«dos de cada tres conversaciones se caen»* si solo se
  ofrece el PB A.
- *«Las inmobiliarias colegas son el canal más activo del período (4 de 11 consultas)»* → un
  protocolo para mostrar el mismo día y una jornada para colegas.
- La web publica el PB H → dar de baja la ficha y el botón en la semana 1.
- Doce datos que faltan, declarados como tales: no hay presupuesto de pauta, no hay resultados de
  publicaciones anteriores, no se sabe si el PB A ya tiene reserva…

**Salió BLOQUEADO**, y los dos chequeos que fallaron enseñan cosas distintas:

```text
❌ P3 Cada publicación habla de una sola lista — piezas que nombran la otra lista: #7, #12
❌ P5 No prioriza ni publica unidades que no están a la venta — PB H
```

1. **P5 era un falso positivo de mi chequeo.** El PB H aparecía en la descripción de la pieza #1:
   *«baja de la ficha y del botón de WhatsApp de PB H»*. El plan hacía lo correcto, **sacarlo**, y el
   chequeo lo leyó como publicarlo. Se corrigió: P5 mira solo las unidades priorizadas y el
   `mensaje_clave` (lo que ve el público), no la descripción de la acción. Reverificada la misma
   salida sin volver a llamar al modelo: P5 pasa.
2. **P3 acertó en una pieza y se equivocó en otra.**
   - **#12 es una falla real.** La jornada para colegas figura como lista `casona_2_terminados`, pero
     su mensaje dice *«Te entregamos por separado el detalle de las unidades terminadas y el de las
     unidades en obra con su plan de pagos»*. Son las dos listas en la misma acción, justo lo que
     prohíbe la restricción 1 del módulo. Hay que partirla en dos, o que el responsable decida que un
     evento con colegas es la excepción.
   - **#7 es un falso positivo.** Es una pieza de Casona 3 que menciona *«Casona 2 terminada con 20 de
     sus 28 unidades vendidas»* como prueba de que la obra se termina (T-12), sin precio ni oferta.
     Eso lo permite el propio playbook.

   **P3 se deja como está**, a propósito. Un chequeo por palabras no distingue «mencionar» de
   «ofrecer»; si se afina para dejar pasar la #7, deja pasar también la #12. Mientras un error de
   este chequeo cueste una revisión y no un aviso mal publicado, conviene que sea desconfiado. **Un
   chequeo por palabras sirve para frenar, no para juzgar: el juicio queda en la revisión humana.**

## Corrida final con el contrato vigente · 11/9 17:39–17:46 · y una falla que frenó todo

Con el contrato v4 + user prompt v2 + playbook v2 se volvieron a correr las consultas, para dejar el
estado final, más la comparación de modelos. **Salieron seis de diecisiete**: 01 a 06 aprobadas,
entre USD 0,1347 y USD 0,2319. A las 17:45, con el plan de octubre corriendo en paralelo, **se
terminó el crédito de la API**, y las once siguientes fallaron antes de llegar al modelo:

```text
BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CexJgRAUg7KPtPxTnaFts'}
```

- **El ejecutor se comportó bien ante la falla**: guardó cada corrida con el error textual y costo
  0, no inventó una salida y siguió con la siguiente. Las once corridas fallidas se movieron a
  `corridas/errores/`, para que no se confundan con corridas válidas.
- **Es un modo de falla que no estaba previsto**, y es de gobierno: si el sistema se usa de verdad,
  una cuenta sin crédito deja a los asesores sin copiloto en medio de una tanda. Lo que corresponde
  es que el asesor responda a mano como antes y que el responsable tenga una alerta de saldo en la
  consola de Anthropic. Se suma a `GOBIERNO.md`.
- **Lo que queda pendiente** es la comparación con Haiku 4.5 y Sonnet 5, justo la prueba de la
  elección de modelo. Sin crédito no se puede hacer.

### D-12 · No se carga más crédito; la comparación de modelos queda sin hacer (11/9, 18:40)

Se le propuso al responsable cargar USD 10 para terminar la comparación de modelos y las corridas
pendientes. Respuesta textual:

> no carguemos creditos solo armemos el artefacto este trabajo es individual

**Consecuencia, dicha sin rodeos:** la elección de modelo queda **argumentada pero no probada**. El
sistema sigue en Opus 5, el más caro de los tres, y `ECONOMIA.md` lo declara así. Las corridas
finales 07, 08, 09 y de coherencia quedan con su versión v1.

En lugar de eso se armó un **visor** (`visor/index.html`, generado por `sistema/generar_visor.py`
desde las corridas guardadas, sin llamar a ninguna API): para cada consulta real muestra lo que
respondió el asesor, el borrador del copiloto en cada versión del contrato, la ficha, los doce
chequeos y el costo, más el plan de octubre. Se abre en cualquier navegador desde el repositorio.

### D-13 · Paquete mensual para colegas, con tarea programada (11/9, 19:00)

El responsable propuso, sobre la jornada con colegas del plan de octubre:

> Esta muy buena la idea es mas hay que poner recordatorios mensuales donde se vuelva a mandar la
> info de listas de precis brochure de venta y disponibilidades

y al preguntarle si a los colegas se les mandan las dos listas:

> dale si mando todos los meses todo junto pero actualizado que sea el mismo agente el que
> entregamos como final

**Qué se decidió y qué se construyó:**

1. **Excepción de lista única, solo para colegas.** Todos los meses reciben las dos listas **en
   archivos separados**, el brochure y la disponibilidad, con el pedido escrito de mostrarle a cada
   cliente solo la que le corresponde. La lista única se sigue cuidando frente al comprador final.
   Queda en la restricción 1 del módulo 2 (v2). **El contrato del módulo 1 no se tocó**: la
   respuesta a una consulta de un colega sigue siendo la lista que pide, que es lo que se probó en
   las corridas.
2. **`sistema/paquete_colegas.py`**, parte del mismo sistema: arma las dos listas en HTML imprimible
   (Casona 3 con anticipo, cuota y saldo de cada unidad, que es el «excel en formato de lista» que
   pidió el responsable en D-10), el mensaje para los colegas y cuatro chequeos. El más importante es
   **K1**: si el tarifario tiene más de 35 días, avisa que hay que actualizar la planilla interna,
   porque *«actualizado»* depende de que alguien cargue las ventas del mes. No usa la API.
3. **Tarea programada de Windows** «Copiloto DOMINIA - Paquete colegas»: el día 1 de cada mes a las
   9:00 genera el paquete, muestra un aviso y abre la carpeta. No envía nada (L2).

**La tarea falló en el primer intento**, con este resultado de `schtasks`:

```text
Último resultado:                                      -2147024894
      <Command>D:\PROYECTO</Command>
      <Arguments>CON AGENTES\copiloto-asesores-dominia\herramientas\paquete_mensual.bat</Arguments>
```

`-2147024894` es «archivo no encontrado»: PowerShell le sacó las comillas a la ruta y Windows la
cortó en el primer espacio de «PROYECTO CON AGENTES». Se volvió a crear pasando el comando por
`cmd /c` con las comillas escapadas, y la prueba manual generó `corridas/paquete_colegas/2026-09/`
(log: *«Paquete de septiembre 2026 … listo para revisar»*). Próxima ejecución: 1/10/2026 a las 9:00.

**Con esto se resuelve la falla de la jornada** (P3, pieza #12 del plan de octubre): una acción con
colegas puede llevar las dos listas. P3 ahora exceptúa el canal `inmobiliarias`; reverificada la
misma salida sin llamar al modelo, **queda solo el falso positivo de la #7**.

**Y el paquete destapó un error del plan que ningún chequeo había visto.** El diagnóstico del plan de
octubre dice que en Casona 3 hay *«4 monoambientes/1 dorm … 14 unidades de 2 dorm y 9 de 3 dorm»*.
El paquete, que cuenta en código desde el tarifario, da **4 de 1 dormitorio, 15 de 2 y 8 de 3**. El
modelo contó mal y llamó «monoambientes» a departamentos de un dormitorio. Es la misma lección del
día de la semana (iteración 5): **lo que se cuenta, se cuenta en código**. Se agregó al contrato del
módulo 2 (*«No cuentes unidades de memoria»*), pero **sin corrida que lo pruebe**, porque no hay
crédito (D-12).

### D-14 · Un front para usarlo, que no depende del crédito de la API (11/9, 19:00)

> pero lo quiero con un front que pueda usarlo

El visor mostraba corridas viejas; el responsable quiere **usar** el copiloto. Se le agregó la
pestaña **«Usar el copiloto»**: se pega la consulta, la página consulta el tarifario, arma la ficha
y el borrador, corre los doce chequeos y ofrece copiar el borrador o descargar la corrida en `.md`
para guardarla en `corridas/`.

**Por qué funciona sin crédito.** Una página publicada puede pedirle una respuesta a Claude con la
capacidad `sample`, **a cuenta de la suscripción de quien la abre**, no de la API. La misma página
implementa la herramienta `consultar_tarifario` en JavaScript sobre el tarifario embebido, así que
el recorrido es el mismo que el del ejecutor de Python: contrato → herramienta → ficha JSON →
chequeos → revisión humana.

**Lo que hay que tener presente, y es una deuda real:** los doce chequeos ahora existen **dos
veces**, en `sistema/copiloto.py` y en `visor/plantilla.html`. Si se toca una regla hay que tocar
las dos, o el front y el ejecutor van a decir cosas distintas sobre el mismo borrador. La forma
correcta de resolverlo sería que las reglas vivan en un solo archivo de datos que lean los dos; no
se hizo por tiempo, y queda declarado como lo que es: duplicación.

**Lo que habilita.** Con esto se puede hacer la prueba que faltaba para la rúbrica: correr una
consulta nueva de verdad, mandar el borrador y anotar qué respondió la persona.

En total se gastaron **USD 4,94** en la API (suma de las 28 corridas con costo registrado): humo, 26 corridas de consultas exitosas, el plan de
octubre y las re-corridas de las cinco iteraciones.

---

## Sábado 12/9/2026

### D-15 · Dos auditorías antes de cerrar: la comercial y la de la rúbrica

El responsable pidió *«Que podemos perfeccionar de esto? Podrías auditarlo con la información de los
manuales para perfeccionarlo? Además auditarlo para ver qué nota tendría para la materia»*. Se
hicieron las dos, en paralelo, con dos agentes distintos, y las dos leyeron el repositorio como lo
leería un tercero.

**La auditoría de formato** aplicó la rúbrica ejecutable y el catálogo de banderas del agente
evaluador del parcial, requisito por requisito y exigiendo una cita por cada requisito dado por
cumplido. **El informe con su puntaje se dejó deliberadamente fuera de este repositorio**: una
evaluación previa guardada adentro del trabajo es un anclaje, y quien corrija tiene que empezar de
cero. Acá va solo lo que hay que arreglar.

- **La bandera G7 era real y la causó este README.** Decía *«La historia: trece decisiones y cinco
  iteraciones»* cuando `DECISIONES.md` ya tenía catorce. Un número de índice que quedó viejo, y en
  contra del propio trabajo. **Corregido**: el índice ya no cuenta, describe. La lección se agrega a
  la lista de lo que no hay que hacer: **no escribir en un documento un número que otro documento
  puede cambiar.**
- **Dos G1 sin penalización**: «publicado como artefacto» sin URL verificable (corregido: ahora dice
  que es privado y que el archivo del repositorio es la copia abrible) y la tarea programada, que
  desde el repositorio solo se puede verificar por su `.bat`, su log y los paquetes que generó.
- **Cero G2, G3a/b/c/d, G4, G5, G6 y G8.** El auditor barrió los 84 archivos por carácter —ancho
  cero, controles bidireccionales, homoglifos— y la historia de git buscando credenciales.
- Rehízo **las 26 multiplicaciones de costo y los ocho agregados de `ECONOMIA.md`**: cierran al
  cuarto decimal. Reprodujo los dos sha256. Enumeró los 13 campos de las 26 salidas: idénticos.
- **La duda que dejó anotada es la misma de siempre**: la exigencia más alta de «sistema completo»
  pide que una salida se haya usado de verdad. Hoy ninguna se envió. Se resuelve mandando un
  borrador real, que ahora se puede preparar desde el front sin crédito de API.

**La auditoría comercial** cruzó los siete borradores del contrato vigente contra las técnicas del
playbook y las fuentes de `conocimiento/fuentes_manuales.md`. Dieciséis hallazgos; el más caro:
**el sistema no tiene seguimiento**. Los tres interesados por el PB A escribieron a las 02:19, 07:53
y 13:24 desde el botón de la web: si no contestan, hoy se pierden en silencio, y las fuentes que el
proyecto ya verificó (MREA con sus secuencias, Forte con tibios y fríos) dicen justamente lo
contrario.

### Iteraciones 6, 7 y 8 · aplicadas juntas y **sin corrida de verificación**

Hasta acá cada iteración tocó **una** pieza y se volvió a correr para ver el antes y el después. Sin
crédito en la API (D-12) eso ya no se puede, así que estos cambios se aplican **declarando que no
están probados**. Cada uno dice qué pieza toca y qué habría que mirar en la próxima corrida; el
front (D-14) permite correrlos sin API, y esa corrida es la que falta.

| # | Pieza | Qué cambió | Por qué |
|---|---|---|---|
| 6 | **Tarea** + esquema | Paso 10: el copiloto deja preparados **tres toques de seguimiento** (48 h, 7 días, 21 días), cada uno con su aporte de valor y su texto; campo `seguimiento` en `esquema_ficha.json` | El agujero más caro: hoy el que no contesta se pierde |
| 7 | **Restricciones** | 8: el post-visita cierra en **reunión de plan y boleto**, no en otra visita (T-31); y cuando hay día y hora, el borrador lleva **dirección y aviso de confirmación** (T-24). 12: con un colega, cuando la lista se asigna por defecto, se **nombra el otro camino sin precios** | T-24 se citaba y no se cumplía en ninguno de los siete borradores; el post-visita no tenía salida; y las cuatro consultas de colegas iban por defecto a Casona 2, que tiene 8 unidades contra 27 |
| 8 | **Formato** y **contexto** (playbook v3) | Formato: **primero la persona** (devolver el saludo, retomar lo que dijo), nada de aperturas clonadas, y la mención de los decisores pegada a la línea del horario. Playbook: T-05 y T-06 habilitan **una** implicancia por escrito; T-28 pide el motivo junto a la pregunta de pago; **T-29 y T-30** (seguimiento), **T-31** (post-visita), **T-32** (el precio viaja con su plan) y **T-33** (no anunciar que no se da el precio) | Los cuatro borradores a colegas abrían con la misma frase palabra por palabra, y tres de los cuatro colegas habían preguntado «cómo estás» sin respuesta. El precio se daba sin anticipo ni cuota, que es el número que se compara con un alquiler |

**Chequeos nuevos en el ejecutor y en el front** (los dos, porque siguen duplicados, D-14):

- **V13**: si hay visita propuesta, el borrador tiene que traer la dirección y el aviso de
  confirmación del día anterior.
- **V14**: vocabulario que la ficha desmiente. Nace de una deriva medida: las dos corridas de
  coherencia sobre la **misma consulta** escribieron *«jardín privado de 29,25 m²»* cuando la ficha
  dice que es un espacio común **de uso exclusivo**. Lo que se escribe integra la oferta (Ley 9445
  art. 16), así que esto no es una cuestión de estilo.

**Y el bloque de revisión humana de cada corrida ahora pregunta lo único que mide si el copiloto
sirve**: si el interesado contestó, si se agendó la visita y si la visita se hizo.

### D-16 · El mensaje mensual a colegas ahora cierra con un próximo paso

`corridas/paquete_colegas/2026-10/mensaje.md` terminaba en *«Si querés mostrar, avisame el día y la
franja y coordino»*, que es exactamente el ejemplo que la T-14 del playbook da como error, en el
mensaje de mayor alcance del sistema. Ahora invita a la jornada para colegas con fecha, pide los
clientes sin definir y cierra preguntando: *«¿Te queda mejor que coordinemos por acá o te llamo?»*.

### D-17 · Franjas de visita, confirmadas por el responsable

La auditoría comercial detectó que los seis borradores que proponían horario lo hacían sin dato: el
copiloto ofrecía siempre 10 y 11 de la mañana, mientras el corpus muestra que **los colegas piden
mostrar al mediodía y a la siesta** («mañana por la siesta», «hoy a las 12 30»). Se le propusieron
franjas al responsable y las confirmó (12/9): lunes a viernes de 10 a 13 y de 16 a 19, sábados de 10
a 13, y la franja de 12 a 15 para los colegas. Quedan en `conocimiento/proyecto.md`, con la
aclaración de que **todo horario que proponga el copiloto es sugerido** y lo confirma el asesor
contra su agenda.

---

## Domingo 13/9/2026

### D-18 · La primera corrida del front, y lo que todavía no prueba

La base de datos de la página publicada guardó una corrida hecha por el responsable el 12/9 a las
13:24, con la consulta de ejemplo del front (`corridas/vivo/2026-09-12_1324_VIVO-ejemplo-PBC_front-v4.md`).

- **Lo que prueba**: que el front funciona de punta a punta sin la API. Llamó dos veces a la
  herramienta, asignó `casona_3_pozo`, propuso PB C, PB A y 1º C con los precios exactos del
  tarifario y pasó los doce chequeos de entonces. El borrador aplicó lo que se había construido: se
  presentó, **no dio precio** (T-27), la pregunta de pago vino con su motivo —*«Para armarles el
  plan que mejor les sirva, ¿cómo pensaban pagarlo…?»*— y la visita se propuso con la pareja:
  *«para que lo vean con tu señora, ¿les queda mejor el sábado 19 a las 10 o a las 11?»*. El 19/9 es
  sábado: V12 en verde.
- **Lo que no prueba**: corrió con el contrato v4, **37 minutos antes** de que se publicaran las
  iteraciones 6 a 8 (commit de las 14:01). Por eso no trae `seguimiento` ni los chequeos V13 y V14,
  y **tampoco trae la dirección ni el aviso de confirmación**, que es justo lo que la iteración 7
  agrega. Y la entrada es un ejemplo, no un interesado real. Las iteraciones 6 a 8 siguen sin corrida.

### Corridas de verificación de las iteraciones 6 a 8 · 13/9 10:37–10:40 · desde el front

El responsable corrió en el front, con el contrato v5, las mismas consultas reales 03, 06 y 08 (con
la fecha del día). Quedaron en `corridas/vivo/`. Es el «después» que les faltaba a las iteraciones
6 a 8.

| Consulta | v1 (11/9) | v5 (13/9) | Chequeos |
|---|---|---|---|
| **03** · colega, «hoy a las 12 30» | *«¿Te queda mejor 12:30 o lo corremos a las 16…?»* | *«Dale, hoy 12:30 queda confirmado, te espero»* · nombra el otro camino sin precios · *«Te espero en Costanera de La Cañada 4140, Manantiales I; te mando la ubicación ahora»* · un solo toque de seguimiento, porque la visita ya está acordada · y avisa que **es domingo, fuera de las franjas** de D-17 | 14/14 |
| **06** · cliente, PB A | Precio y plan completos a un desconocido | Sin precio; *«Según cómo lo pienses pagar te conviene una cosa u otra: ¿lo veías en cuotas o al contado?»*; *«Si la decisión la toman entre dos, mejor vengan los dos»*; tres toques de seguimiento, ninguno con «¿pudiste ver…?»; el precio con su plan queda preparado en las alertas por si lo pide (T-32) | 14/14 tras corregir V13 |
| **08** · cliente, PB B o PB H | *«El PB H no integra el stock a la venta»* | *«El PB H no está a la venta: la misma tipología de 1 dormitorio la tenés en el PB D»* | **Bloqueada: 135 palabras** |

**Dos errores del chequeo, encontrados por las corridas:**

1. **V13 marcaba mal.** Pedía dirección y aviso de confirmación siempre que hubiera horarios
   *propuestos*, y la restricción 8 los exige cuando la visita queda *acordada*. Bloqueó la 06 y la
   08 por eso. Se corrigió (aplica en la etapa `listo_para_visita`) en el ejecutor y en el front, y
   se reverificaron las tres fichas guardadas **sin volver a llamar al modelo**: la 06 pasa.
2. **Los toques de seguimiento no los revisaba ningún chequeo**, y también le llegan al cliente.
   V6 (descuentos), V7 (promesas y urgencia) y V14 (vocabulario) ahora leen el borrador **y** el
   seguimiento. Reverificadas las tres: ninguna cambió de resultado.

**Lo que queda abierto, con su error textual:**

- **La 08 se pasa de largo**: *«❌ V10 Menos de 120 palabras en WhatsApp o Instagram — 135 palabras»*.
  Con dos unidades pedidas y una que no está a la venta, el formato v5 —presentación, contexto,
  respuesta, forma de pago, horario con decisores, firma— no entra. El candidato de corrección es de
  la pieza **formato**: si hay que responder por dos unidades o por una que no existe, se saca la
  línea de contexto del complejo. **No se pudo correr hoy**: queda como falla contada.
- **Las aperturas a colegas siguen clonadas.** La 03 abre otra vez con *«Hola! Francisco, de DOMINIA,
  por acá.»*, la misma frase de las corridas del 11/9. La regla de formato de la iteración 8 no
  alcanzó.
- **El toque de 7 días es vago.** *«Te puedo mostrar el avance de obra de Casona 3 y cómo viene el
  stock de 2 dormitorios»* no trae un hecho verificable, que es lo que pide la T-29. Y en la 08 dice
  que los de 1 dormitorio *«son pocos»*, que roza la urgencia que prohíbe la T-23 aunque no dispare V7.

## Iteración 9 · pieza: FORMATO · contrato v5 → v6 · 13/9 10:49

**Qué falló** (corrida del front de las 10:40, `corridas/vivo/2026-09-13_1040_C08-cliente-PBB-o-PBH_front-v5.md`):

```text
❌ V10 Menos de 120 palabras en WhatsApp o Instagram — 135 palabras · canal whatsapp
```

Con dos unidades pedidas —y una de ellas que no está a la venta— el formato v5 no entraba:
presentación, contexto del complejo, las dos unidades, una línea aparte de forma de pago, la pregunta,
el horario con los decisores y la firma.

**Qué se cambió** (solo la pieza *formato* de `prompts/system_prompt.md`, commit `ede450d`): cuando la
respuesta cubre más de una unidad o una que no está a la venta, **se saca la línea de contexto del
complejo**, cada unidad se resuelve en una sola línea y la forma de pago va dentro de la pregunta de
calificación, no en una línea aparte.

**Qué cambió en la salida** (misma consulta, 10:49, `corridas/vivo/2026-09-13_1049_C08-cliente-PBB-o-PBH_front-v6.md`):

| | v5 · 10:40 | v6 · 10:49 |
|---|---|---|
| Largo | 135 palabras · **bloqueada** | **119 palabras · 14/14, aprobada** |
| Contexto del complejo | *«Casona de los Arcos es un complejo cerrado de tres torres en Manantiales I…»* | Sacado |
| Las dos unidades | En dos oraciones | *«El PB H no está a la venta; lo más parecido es el PB D, 1 dormitorio también en planta baja, con jardín y cochera»* |
| Pregunta de calificación | *«¿lo veías en cuotas o al contado?»* | *«Contame si es para vivir o para invertir»* |

**El arreglo funcionó a medias, y eso también queda dicho.** El borrador entró en el límite, pero:

1. **Se perdió la pregunta de cómo paga.** La regla nueva decía que la forma de pago va *dentro* de
   la pregunta; el modelo la convirtió en afirmación (*«Las dos se toman en cuotas durante la obra»*)
   y preguntó el uso. Justo lo que la T-28 dice que no hay que hacer cuando la lista salió del botón
   de la web. **Ningún chequeo lo detecta**: V9 cuenta signos de pregunta, no cuál es la pregunta.
2. **119 palabras pasa el chequeo (menos de 120) pero no el presupuesto del formato (80 a 110).** Es
   la misma distancia entre el límite duro y el presupuesto que se registró en la iteración 4.

**Queda abierto**: un chequeo que verifique que, con la lista asignada por el botón, el borrador
pregunte por la forma de pago (T-28). Sin crédito de API ni otra corrida del front no se agregó.

### D-19 · Correcciones de una evaluación hecha desde otra sesión

El responsable pidió evaluar el repositorio desde la sesión del agente evaluador del parcial, que
aplicó la rúbrica a mano porque la API no tenía crédito, y trajo sus hallazgos a esta sesión. Se
verificaron uno por uno contra el repositorio antes de tocar nada, y los cuatro eran reales:

1. **El README decía «contrato en su versión 5» y «`system_prompt.md` v4»**, y el archivo ya estaba en
   la versión 6. Corregido: el README ya no nombra la versión, remite al encabezado del prompt.
2. **El README decía «los mismos trece campos en todas las corridas»**, y las de `corridas/vivo/`
   tienen catorce desde que se sumó `seguimiento`. Corregido: trece hasta la v4, catorce desde la
   iteración 6, idénticos dentro de cada generación.
3. **La iteración 9 no estaba en este archivo**, aunque el prompt decía que su historial estaba acá.
   Agregada arriba, con su corrida.
4. **`GOBIERNO.md` citaba chequeos por número de línea, y las líneas se habían corrido** cuando se
   agregaron V13 y V14. Ahora se citan por su código. Además, la tabla de modos de falla estaba
   cortada por líneas en blanco, y las fallas 12 a 14 quedaban fuera de la tabla. Arreglada.

Es la tercera vez que aparece el mismo error: un número escrito en un documento que otro documento
cambió. La regla ya estaba anotada desde D-15 y no alcanzó con anotarla. **Lo que funciona es no
escribir el número**: referenciar el archivo que lo tiene.

### D-20 · Chequeo V15: la pregunta de pago que el largo se llevó, y cuatro conteos más

Una segunda evaluación desde la sesión del agente evaluador marcó que la iteración 9 había dejado un
hueco sin chequeo y que seguían escritos números que ya eran viejos. Se verificó cada punto contra el
repositorio antes de corregir:

- **`conocimiento/playbook.md` decía «Versión 2»** y su contenido ya era la versión 3 (T-29 a T-33).
  Corregido el encabezado.
- **El README y el visor decían «28 técnicas»** y el playbook tiene 33. Y quedaban «catorce reglas»,
  «14 chequeos» y «8 iteraciones» en el README y en el visor, que se iban a quedar viejos apenas se
  sumara un chequeo. **Se sacaron todos los conteos**: los documentos nombran el archivo que tiene el
  dato. Es la cuarta vez que aparece este error; D-15 y D-19 lo habían anotado como regla y no
  alcanzó, porque la regla estaba escrita pero los conteos seguían en los documentos.

**El chequeo nuevo, V15**, en el ejecutor y en el front: si la consulta vino del botón de la web
(«Me interesa … de Casona III»), alguna pregunta del borrador tiene que ser sobre la forma de pago.
Es la T-28, que la iteración 9 perdió sin que nada lo detectara.

**Cómo se probó sin la API**: aplicándolo a todas las corridas guardadas que vinieron del botón.

| Corridas | V15 | Qué muestra |
|---|---|---|
| 05, 06 y 08 con el contrato v1, y 06 con la v3 (11/9, 16:57 a 17:22) | ✗ | Antes de la iteración 3 la T-28 no existía: el chequeo marca la ausencia real |
| 05 y 06 desde la iteración 3 (17:24 en adelante), y 06 y 08 del front con la v5 | ✓ | La pregunta aparece desde que el playbook la pide |
| **08 del front con la v6 (13/9 10:49)** | **✗ · BLOQUEADA** | *«Contame si es para vivir o para invertir»*: el hueco de la iteración 9 |
| Coherencia 3 con el contrato v1 | ✓ | **Falso negativo**: pasa por *«Y si el plan de pagos te cierra, ¿te queda mejor…?»*, que nombra el pago dentro de la pregunta del horario |

**Consecuencia honesta: la iteración 9 no resolvió la consulta 08.** Con V14 la 08 salía bloqueada
por largo; con V15 sale bloqueada por no preguntar cómo paga. El formato todavía no encontró cómo
responder por dos unidades, una de ellas inexistente, y preguntar lo que la T-28 exige en menos de
120 palabras. Queda abierta, y el próximo intento es de la pieza **formato**: la pregunta de pago
reemplaza a la aclaración de los decisores cuando no entran las dos.

**Y la flaqueza de V15 queda dicha**: busca palabras de pago dentro de cualquier pregunta, así que una
pregunta de horario que mencione «el plan de pagos» la engaña. Un chequeo por palabras sirve para
frenar, no para juzgar (lo mismo que se anotó sobre P3 del módulo 2).


### D-21 · Las horas de las corridas del front estaban en UTC

Las corridas del front del 13/9 se habían anotado a las 13:37, 13:39, 13:40 y 13:49 «hora de
Córdoba». **Eran horas UTC**: la página arma el identificador con la hora universal, y al pasarlas a
los archivos no se restaron las tres horas. Las reales son **10:37, 10:39, 10:40 y 10:49**. Así
escritas, las corridas figuraban *después* de los commits que las agregaban (el de las 10:47 subía
corridas «de las 13:37»), que es exactamente lo que un evaluador lee como historia de proceso falsa.
Se corrigieron los nombres de archivo, los encabezados y las referencias de este documento. La
corrida del 12/9 sí estaba bien convertida (16:24 UTC → 13:24).

## Iteración 10 · pieza: FORMATO · contrato v6 → v7 · 13/9 11:17

**Qué falló** (corrida del front de las 10:49, contrato v6): el borrador entró en el largo y perdió
la pregunta de cómo paga. El chequeo V15, agregado a las 11:14, la deja bloqueada:

```text
❌ V15 Si la consulta vino del botón de la web, el borrador pregunta cómo paga (T-28) — no pregunta cómo piensa pagar
```

**Qué se cambió** (solo la pieza *formato*, commit `3543c30`): un **orden de recorte** cuando no entra
todo. Primero la línea de contexto, después la aclaración de los decisores, al final la segunda
unidad. La pregunta de pago no se saca nunca y no se reemplaza por la del uso.

**Qué cambió en la salida** (misma consulta, 11:18, `corridas/vivo/2026-09-13_1118_C08-cliente-PBB-o-PBH_front.md`):

| | v5 · 10:40 | v6 · 10:49 | v7 · 11:18 |
|---|---|---|---|
| Largo | 135 palabras ❌ | 119 palabras | **113 palabras** |
| Pregunta | *«¿lo veías en cuotas o al contado?»* | *«Contame si es para vivir o para invertir»* ❌ | *«Según cómo lo pienses pagar te conviene una cosa u otra —tenemos terminado para escriturar ya y en obra con cuotas—, así que decime: ¿lo veías al contado o con crédito, o te sirve más el plan en cuotas?»* |
| Decisores | Pegados al horario | Pegados al horario | **Recortados**, como manda el orden nuevo |
| Chequeos | Bloqueada por V10 | Bloqueada por V15 | **15 de 15, aprobada** |

**La consulta 08 queda cerrada.** Hicieron falta tres iteraciones de la misma pieza, y la lección es
la que ya había dejado la iteración 4: con un límite de largo, **no alcanza con decir qué va en el
mensaje; hay que decir qué se saca primero**. Sin ese orden, el modelo recorta lo que le resulta más
fácil de recortar, que no es lo menos importante.

Lo que sigue flojo en esta misma corrida: el toque de 7 días (*«Te cuento cómo viene la obra de
Casona 3 y qué queda de planta baja con jardín»*) todavía no trae un hecho verificable.

## Uso con una consulta nueva · 13/9 11:03 · C10, colega, amoblado el domingo

El responsable cargó en el front una **consulta nueva** de una inmobiliaria colega, que no está en
`entradas/`: un cliente jugador de fútbol de Buenos Aires quiere ver el amoblado el domingo temprano.
Corrió con el contrato v6, antes de V15 y de la iteración 10
(`corridas/vivo/2026-09-13_1103_C10-inmob-amoblado-domingo_front.md`).

- **Lo que hizo bien**: devolvió el saludo primero (*«Todo bien por acá, gracias!»*), aceptó el
  domingo temprano sin condiciones (restricción 13), asignó Casona 2 y nombró el otro camino sin
  precios, explicó el 2º F como producto amoblado (restricción 7) y puso dirección y aviso de
  confirmación.
- **Salió BLOQUEADA por dos chequeos**, y los dos dicen algo distinto:
  - **V4 · «4 unidad(es)»**: propuso cuatro unidades y el máximo es tres. Falla real del modelo.
  - **V11 · primera línea sin el nombre del asesor**: acá chocan dos reglas del propio contrato. El
    formato pide *primero la persona* (devolver el saludo, T-17) y V11 exige el nombre en la primera
    línea. Con un colega que ya lo conoce, el borrador eligió la T-17. **La contradicción es del
    contrato, no del modelo**, y queda abierta.
- **Un error que ningún chequeo ve**: la consulta es del domingo 13/9 y pide «el domingo»; el
  borrador acepta «el domingo temprano» y el toque de seguimiento dice *«Confirmado para mañana a las
  9»*. Si «el domingo» es hoy, «mañana» es lunes. V12 solo verifica pares con fecha numérica.
- **Revisión humana: pendiente del responsable** —si el borrador se envió, qué se cambió y qué
  respondió el colega—. Es la primera corrida con una consulta que no estaba en el corpus.
