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
