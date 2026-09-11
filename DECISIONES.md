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
