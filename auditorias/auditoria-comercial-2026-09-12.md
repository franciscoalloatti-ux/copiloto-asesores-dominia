# Auditoría comercial del Copiloto de Asesores DOMINIA

**Qué se auditó:** el contrato vigente (`prompts/system_prompt.md` v4 + `prompts/user_prompt.md` v2 +
`conocimiento/playbook.md` v2 + `conocimiento/proyecto.md`), las **siete corridas del contrato
vigente** (`corridas/2026-09-11_1731…1745`, consultas C01 a C06), las dos corridas de coherencia
(`corridas/coherencia/`, contrato v1), las corridas v1 de C07/C08/C09 —las únicas que existen para
esos casos—, el plan de octubre (`corridas/plan_mensual/2026-09-11_1744_plan-2026-10_opus-5.md`) y
el envío mensual a colegas (`corridas/paquete_colegas/2026-10/mensaje.md`). Se comparó cada borrador
con la sección «Lo que pasó en la realidad» de `entradas/`.

**Estado general.** El sistema ya no tiene fallas de *contención* (lista única, precios del
tarifario, nada de descuentos, nada de promesas): los doce chequeos automáticos pasan en las siete
corridas. Lo que falta es **profundidad comercial**. El copiloto hoy resuelve muy bien **un solo
mensaje** de una conversación de venta que tiene entre cuatro y diez. Está construido como un
*responder* excelente y no como un *vendedor*: no tiene seguimiento, no tiene post-visita, no
tiene implicancia, no pregunta quién decide, y su calificación se redujo a una sola pregunta
—«¿cómo pensabas pagarlo?»— que es la más fría de las seis.

**Dato duro del uso del playbook.** De las 28 técnicas, en las siete corridas del contrato vigente
solo se citan 14. Nunca aparecen **T-04** (qué te llevó a mirar ahora), **T-05/T-06** (SPIN /
implicancia), **T-07** (contra qué se compite), **T-08** (quién decide), **T-17** (responder a la
persona antes que a la consulta) ni **T-22** (cierre condicional). Las cinco más citadas son T-26,
T-18, T-15, T-02 y T-14. Es decir: el copiloto **informa, avisa el contra y propone horario**, pero
no **indaga**. Eso es exactamente lo que separa una tasa de visitas del 15 % de una del 35 %.

---

# IMPACTO ALTO

## H-01 · No existe el seguimiento del que no contesta. Es el agujero más caro del sistema

**Qué falla.** No es un defecto de un borrador: es una **pieza faltante del contrato**. La sección
`## 3 · Tarea` de `prompts/system_prompt.md` tiene nueve pasos y termina en:

> 9. **Listá las alertas** para el asesor y lo que tiene que verificar antes de enviar.

El esquema (`sistema/esquema_ficha.json`) tampoco tiene dónde ponerlo: `proximo_paso` es
`{accion, propuesta_de_visita}` y `additionalProperties: false`. El resultado se ve en las corridas:
el borrador de C05 (17:43) cierra con

> «Y para verlo en persona, ¿te queda mejor el miércoles 24 a las 10 o el sábado 27 a las 11?»

y las seis alertas que siguen no dicen **nada** de qué hacer si el interesado no responde. Los tres
leads de PB A (C06, COH-PBA-2, COH-PBA-3) entraron a las 02:19, 07:53 y 13:24 desde el botón de la
web: son leads fríos de madrugada, la población donde la tasa de respuesta al primer mensaje es más
baja y donde el segundo y el tercer toque valen más que el primero. Hoy, si no contestan, el sistema
los pierde en silencio.

**Respaldo.** Es la **regla 13** de `conocimiento/fuentes_manuales.md`, ya verificada por el
proyecto: *«Seguimiento sistemático del que no agenda. Contactos periódicos que aporten valor, no
insistencia»*, con fuente MREA (secuencias 8x8 y 33 toques) y Forte («seguir a los tibios y fríos»,
`cliente-comprador-ou-interessado`). También Villarroya vía inmonews: *«Una sola reprogramación
antes de pasar a seguimiento largo»*. Es decir: **las fuentes lo sostienen y el playbook no lo
tiene**. Hace falta una técnica nueva.

**Texto exacto para pegar.**

1) En `conocimiento/playbook.md`, sección nueva antes de «Marca y colegas»:

```markdown
### Seguimiento

- **T-29 · El que no contesta no se pierde: entra en secuencia.** Si el interesado no responde, el
  copiloto deja preparados **tres toques** con espaciado creciente y **cada uno con un aporte de
  valor distinto**, nunca «¿pudiste ver mi mensaje?»: (1) a las 48 h, un dato útil que no se dijo
  antes (el contra, la cochera incluida, que las expensas corren desde la posesión); (2) a los 7
  días, algo nuevo y verificable (avance de obra, que se liberó o se vendió una unidad de esa
  tipología, la jornada de puertas abiertas); (3) a los 21 días, la pregunta de cierre de ciclo:
  «¿seguís mirando o lo pausaste por ahora?», que da permiso a decir que no. Después del tercer
  toque sin respuesta, el lead pasa a la base fría del plan mensual y no se lo vuelve a escribir
  individualmente. Los tres mensajes los **envía el asesor**, no el sistema. *(MREA, secuencias 8x8
  y 33 toques, vía reseñas; Forte, blog del autor: seguir a tibios y fríos; Villarroya, artículo del
  autor: si las excusas se repiten, seguimiento largo)*
- **T-30 · Bajar la intensidad, no subirla.** Cada toque es más corto que el anterior y ninguno
  repite la propuesta de horario más de dos veces en total. La señal de huida se respeta: quien no
  contestó tres veces no recibe un cuarto mensaje individual. *(Villarroya: leer las señales de
  huida, no insistir)*
```

2) En `prompts/system_prompt.md`, `## 3 · Tarea`, agregar como paso 10:

```markdown
10. **Dejá armado el seguimiento** (T-29): si este mensaje puede quedar sin respuesta, escribí los
    tres toques —a las 48 h, a los 7 días y a los 21 días— cada uno con su aporte de valor y su
    texto listo para copiar, de menos de 40 palabras. Si la consulta ya tiene visita confirmada, en
    lugar de la secuencia va **un solo** mensaje: la confirmación del día anterior.
```

3) En `sistema/esquema_ficha.json`, agregar a `required` el campo `seguimiento` y a `properties`:

```json
"seguimiento": {
  "type": "array",
  "items": {
    "type": "object",
    "additionalProperties": false,
    "required": ["cuando", "aporte_de_valor", "texto"],
    "properties": {
      "cuando": {"type": "string", "enum": ["48h", "7 dias", "21 dias", "dia_anterior_a_la_visita"]},
      "aporte_de_valor": {"type": "string"},
      "texto": {"type": "string"}
    }
  }
}
```

**Qué mirar en la próxima corrida.** Que las siete fichas traigan `seguimiento` con tres entradas
(o una sola, `dia_anterior_a_la_visita`, en C01 y C03, que ya tienen visita). Que **ningún** texto
de seguimiento contenga «¿pudiste ver…?», «te reitero» ni «sigo a la espera». Que el toque de 7 días
mencione un hecho verificable de la ficha o del tarifario y no un adjetivo.

---

## H-02 · El interesado que ya visitó no tiene ningún camino: la restricción 8 lo empuja de vuelta a la visita

**Qué falla.** La etapa `post_visita_negociacion` existe en el playbook («Ya visitó; pide descuento,
condiciones o tiempo») y en el enum del esquema, pero **ninguna técnica del playbook es de
post-visita** y la restricción 8 del contrato lo bloquea:

> 8. **El borrador:** — termina con un próximo paso concreto: si la visita ya está propuesta, **su
>    confirmación** (ver restricción 13); si no, la visita con **dos horarios a elección**, o una
>    pregunta de calificación si todavía falta lo esencial;

Para alguien que ya recorrió el complejo, las tres únicas salidas que ofrece el contrato son
absurdas: no hay visita que proponer, no hay visita que confirmar y las preguntas de calificación ya
están respondidas. El copiloto va a improvisar, y con el techo de 110 palabras va a improvisar mal.
Tampoco hay un archivo en `entradas/` que ejercite esta etapa: **la etapa está declarada y nunca se
probó**.

**Respaldo.** Villarroya, la vía de Rackham que el propio autor recomienda, citada textual en
`fuentes_manuales.md`: *«usa un único cierre como consecuencia natural de haber resuelto todas las
objeciones y resumido los factores de decisión clave»*, con aplicación DOMINIA ya escrita en la
fuente: *«Antes de proponer la visita o la reserva, contestar todas las dudas planteadas y resumir
en una línea lo que el interesado dijo que valora»*. Ese resumen-de-factores es justamente la
técnica post-visita que falta. Se apoya además en el principio rector del playbook (avance, no
cierre): después de la visita, **el avance siguiente no es otra visita, es la reunión de plan de
pagos y modelo de boleto**, que la propia T-20 ya nombra como material de la visita.

**Texto exacto para pegar.**

1) En `conocimiento/playbook.md`, en «Cierre hacia la visita», después de T-16:

```markdown
- **T-31 · Después de la visita, el avance es la reunión de plan y boleto.** Con quien ya visitó, el
  mensaje hace tres cosas y en este orden: (1) **resume en una línea lo que él dijo que valora**,
  con sus palabras («te quedaste con la planta baja por el jardín y por no tener escaleras»); (2)
  responde la duda que quedó abierta en la visita, o dice cuándo la responde; (3) propone el paso
  siguiente concreto, que **no es otra visita**: sentarse a ver el plan de pagos de esa unidad y el
  modelo de boleto, en la oficina de Vélez Sarsfield 522 o por videollamada, con **los decisores**.
  Nunca se cierra un post-visita con «cualquier cosa avisame». *(Villarroya: cierre único como
  consecuencia natural de resolver objeciones y resumir los factores de decisión; Migliorisi, cap. 6:
  «no se trata solo de vender e irse»)*
```

2) En `prompts/system_prompt.md`, restricción 8, primer guion, reemplazar por:

```markdown
   - termina con un próximo paso concreto: si la etapa es `post_visita_negociacion`, la reunión de
     plan de pagos y modelo de boleto con dos horarios y con los decisores (T-31); si la visita ya
     está propuesta, **su confirmación** (ver restricción 13); si no, la visita con **dos horarios a
     elección**, o una pregunta de calificación si todavía falta lo esencial;
```

3) Crear `entradas/consulta-10.md` con un caso real de post-visita (el asesor tiene varios en el
teléfono): sin un caso de entrada, esta rama se sigue sin probar.

**Qué mirar en la próxima corrida.** Que en el caso post-visita `proximo_paso.accion` diga
«reunión de plan de pagos y boleto» y no «visita», que el borrador **arranque** con el resumen de lo
que la persona valoró, y que `propuesta_de_visita` no proponga recorrer el complejo otra vez.

---

## H-03 · La implicancia por escrito está prohibida de hecho, y con ella se cae el único argumento que mueve al que alquila

**Qué falla.** El playbook manda la implicancia a la visita:

> **T-05 · SPIN.** […] Por escrito se trabajan los dos primeros; la implicancia se hace en la visita.

Consecuencia medida: **en los siete borradores del contrato vigente no hay una sola pregunta de
implicancia**, y T-06 y T-07 no se citan nunca. El borrador de C05 (17:43) pregunta:

> «Antes de pasarte números, ¿cómo pensabas pagarlo: contado, crédito o en cuotas?»

y el de C06 (17:45):

> «Para orientarte bien, ¿cómo pensabas pagarlo?»

Las dos son preguntas de **formulario financiero**. Ninguna le da a la persona una razón para
contestar. Y el playbook dice, en T-07, que el competidor real «casi nunca es otro emprendimiento:
es seguir alquilando o dejar la plata quieta» — pero nada en el mensaje hace visible esa
comparación, ni siquiera como pregunta. El copiloto conoce el argumento y tiene prohibido usarlo.

**Respaldo.** Forte, verificado en `fuentes_manuales.md`: *«Precalificación motivacional (qué busca
y por qué; técnica de "pasado y futuro"…) y financiera (cuánto y cómo puede pagar). Tiene que ser
conversación, no interrogatorio»*, y la aplicación que la propia fuente propone: *«Hacer 1 o 2
preguntas abiertas por mensaje… Por ejemplo: "¿Qué es lo que más te importa del próximo depto?"»*.
El orden de Forte es **motivacional primero, financiera después**; el contrato hoy hace lo inverso.
Villarroya adapta SPIN a la venta inmobiliaria: la implicancia no está vedada por escrito en ninguna
fuente; la veda es una decisión interna de la Academia Casona que **cuesta visitas**.

**Texto exacto para pegar.** En `conocimiento/playbook.md`, reemplazar el texto de T-05 y T-06 por:

```markdown
- **T-05 · SPIN.** Situación → Problema → Implicancia → Necesidad-beneficio. Por escrito se trabajan
  la situación y el problema siempre, y **una** implicancia cuando ya hay un dato propio de la
  persona sobre el que apoyarla (que alquila, que se le vence el contrato, que tiene la plata
  quieta, que le nació un hijo). La implicancia larga —números, cuentas, comparaciones— se hace en
  la visita. *(Rackham, vía Academia Casona; Villarroya adapta SPIN a la venta inmobiliaria)*
- **T-06 · La implicancia como pregunta.** Se devuelve como pregunta, nunca como afirmación, y
  **ocupa el lugar de la pregunta de calificación de ese mensaje, no se suma a ella**. Por escrito
  la forma segura es abierta y sin números: «¿hasta cuándo tenías pensado seguir alquilando?»,
  «¿esa plata la tenés esperando algo puntual?». La cuenta (alquiler × 36 meses) se hace **en la
  visita**, nunca escrita. Nunca se da un precio antes de tener el número contra el que se lo quiere
  comparar. *(Academia Casona; Forte, blog del autor: precalificación motivacional antes que
  financiera)*
```

**Qué mirar en la próxima corrida.** Que al menos en las consultas de cliente final donde la persona
aportó un dato propio, `estrategia.tecnicas` incluya T-06 y el borrador tenga una pregunta abierta
de motivo o de plazo. Que el total de signos de pregunta siga siendo ≤ 2 (chequeo V9 en verde): si
sube a 3, la implicancia se sumó en vez de reemplazar, y hay que volver atrás.

---

## H-04 · La calificación arranca por la pregunta más fría de las seis, y nunca pregunta quién decide

**Qué falla, primera parte: el orden.** T-28 obliga a que la primera pregunta sea la del dinero:

> **T-28 · Si la lista salió del botón, la primera pregunta es cómo paga.** […] la primera pregunta
> es la T-03 («¿cómo pensabas pagarlo?»), no el uso.

Como los tres leads de PB A y el de 1º E llegaron todos del botón de la web, T-28 se aplica a
**todos** los clientes finales del corpus. Resultado: el primer mensaje de DOMINIA a un desconocido
es, en la práctica, «¿con qué plata contás?». La razón técnica de T-28 es correcta (sin saber cómo
paga, el terminado puede convenirle más, T-13); el problema es la **redacción**, no la decisión.
«Para orientarte bien, ¿cómo pensabas pagarlo?» no le dice a la persona **qué gana** contestando.

**Qué falla, segunda parte: quién decide.** T-08 dice «Se pregunta temprano; la visita se arma con
todos los decisores». En los siete borradores vigentes, `quien_decide` está en `falta` o `inferido`
y **ningún borrador lo pregunta**. Es la causa más común y más cara de visita fallida: viene uno de
los dos, y hay que repetir la visita entera. Y no se puede resolver con una pregunta más, porque el
techo son dos.

**Respaldo.** T-01 del propio playbook manda dar el motivo de la pregunta («para no mandarte
información que no te sirve»), y ni C05 ni C06 lo hacen con la pregunta de pago. Forte:
«precalificar conversando, no interrogando», y guiar con competencia. Para el decisor, T-08 y
Villarroya (concertar con hora, lugar, objetivo y **modalidad**).

**Texto exacto para pegar.**

1) En `conocimiento/playbook.md`, reemplazar la primera oración de T-28 y agregar la fórmula:

```markdown
- **T-28 · Si la lista salió del botón, la primera pregunta es cómo paga, y va con su motivo.** […]
  la primera pregunta es la T-03, **dicha con lo que la persona gana al contestarla**: «Según cómo
  lo pienses pagar te conviene una cosa u otra —tenemos terminado para escriturar ya y en obra con
  cuotas—, así que decime: ¿lo veías al contado o con crédito, o te sirve más el plan en cuotas?».
  Nunca «¿cómo pensabas pagarlo?» a secas: pedida sin motivo, es la pregunta que más conversaciones
  corta. *(Academia Casona, T-01: la pregunta va con el motivo dicho)*
```

2) En `prompts/system_prompt.md`, `## 5 · Formato`, punto 4 del borrador, agregar al final:

```markdown
     Cuando el próximo paso es la visita, la línea del horario lleva **pegada** la mención de los
     decisores, como aclaración y no como pregunta (no suma un signo de interrogación): «¿te queda
     mejor el sábado a las 10 o a las 11? Si la decisión la toman entre dos, mejor vengan los dos:
     así no hay que repetir la recorrida» (T-08).
```

**Qué mirar en la próxima corrida.** Que ningún borrador contenga la cadena literal «¿cómo pensabas
pagarlo?» sin una cláusula de motivo delante. Que **todos** los borradores que proponen o confirman
visita traigan la aclaración de decisores. Que V9 siga contando 2 preguntas o menos.

---

## H-05 · Con las inmobiliarias colegas, el copiloto elige la lista por defecto y no ofrece el otro camino: se pierde el 77 % del stock

**Qué falla.** La restricción 12 dice: «si no lo aclara, `casona_2_terminados`». En las cuatro
consultas de colegas del corpus **ninguna aclaró**, así que las cuatro fueron a Casona 2. C04
(17:42):

> «Sí, hoy tengo tres unidades de dos dormitorios disponibles en Casona 2, terminadas y con cochera:
> PB B y PB C con dos baños y jardín de uso exclusivo, y 1º G en altura.»

El tarifario tiene **8 unidades en Casona 2 y 27 en Casona 3**; de 2 dormitorios hay 4 en la
terminada y 15 en la de obra. El default manda al colega la lista chica en el 100 % de los casos, y
la corrección queda escondida en una alerta que el cliente final nunca ve:

> «Si responde que su cliente busca cuotas o en obra, recién ahí se pasa la de Casona 3.»

Peor en C01 (17:39), donde la alerta dice explícitamente:

> «Si el cliente final busca 1 dormitorio en altura, esa tipología solo existe en Casona 3: no se
> menciona en este mensaje»

En terminado hay **un solo** 1 dormitorio (PB F, planta baja). Si el cliente de la colega quiere 1
dormitorio en altura, el mensaje es un callejón sin salida, y la restricción 1 **no obliga a eso**:
dice textualmente que «podés decir que hay "dos caminos distintos" sin dar precios de ninguno». El
copiloto se está autoimponiendo una restricción más dura que la que tiene, y le cuesta operaciones.

**Respaldo.** Código de Ética CPI Córdoba art. 1 c) incs. 1, 2 y 4, resumido en la regla 19 de
`fuentes_manuales.md`: *«Con inmobiliarias colegas: cordialidad, darles toda la información útil»*.
Woscoboinik (cap. 5 y epílogo, según índice): tratar al colega como profesional, con información
completa para que pueda llevar interesados. Y el propio envío mensual a colegas ya hace lo correcto:
*«a cada cliente mostrale solo la lista que le corresponde según cómo va a pagar»*. Es una
incoherencia interna entre el módulo mensual y el módulo de consultas.

**Texto exacto para pegar.** En `prompts/system_prompt.md`, restricción 12, después de «Nunca las
dos», insertar:

```markdown
    Cuando la lista se asigna por defecto (el colega no dijo cómo paga su cliente), el borrador
    **nombra el otro camino sin precios y sin lista**, en una sola línea: «Te mando la de terminados,
    que es lo que se escritura ya; si tu cliente necesita cuotas durante la obra decímelo y te paso
    la de Casona 3, que además tiene tipologías que en terminado no existen (1 dormitorio en altura
    y 2 dormitorios con 2 baños en altura).» Eso no es mezclar listas —no lleva ningún precio de la
    otra— y evita que el colega descarte el proyecto por falta de tipología.
```

**Qué mirar en la próxima corrida.** Que las cuatro consultas de colegas traigan esa línea. Que el
chequeo V2 siga en verde (un solo edificio en `unidades_propuestas`) y V5 no encuentre montos de la
otra lista: **la mención sin precio no debe romper ningún chequeo**. Si V2 o V5 se ponen en rojo, el
modelo se pasó de la línea y hay que endurecer la redacción.

---

## H-06 · El precio se da sin su plan de pagos, y el plan es el argumento

**Qué falla.** T-27 está bien resuelta (ver «lo que ya funciona»), pero el contrato no dice **cómo**
se da el precio cuando la persona lo pide. El resultado es que los tres números que hacen digerible
un departamento de USD 241.706 quedan escondidos en una alerta interna, en C05 (17:43):

> «Si lo pide, la cifra del tarifario es USD 241.706 para el 1º E (anticipo USD 96.682, 30 cuotas de
> USD 3.223, USD 48.341 contra entrega).»

El tarifario tiene las columnas `anticipo_usd`, `cuotas`, `cuota_mensual_usd` y
`saldo_contra_entrega_usd` y **ningún borrador vigente las usa**. Un lead que lee «USD 241.706» se
va; el mismo lead que lee «30 cuotas de USD 3.223» compara con el alquiler que paga. Es el mismo
número, y solo uno de los dos vende.

Segundo defecto, de tono: «Antes de pasarte números, ¿cómo pensabas pagarlo?» (C05, 17:43) **anuncia
que se está reteniendo el precio**. Eso invita a «mandame el precio y listo» y convierte a T-27 en
un obstáculo visible. La retención tiene que ser invisible: se da la mecánica, se calla la cifra.

**Respaldo.** Woscoboinik, cap. 4 (la tasación como fundamento del precio): ante «está caro» se
explica en qué se funda el precio. Villarroya: resumir los factores de decisión antes de pedir el
compromiso. Regla 11 de `fuentes_manuales.md`: el ajuste por CAC se explica con su mecánica por
chat y el cálculo personalizado se entrega formalmente. Nada de esto es un descuento ni una promesa:
son las condiciones del tarifario vigente.

**Texto exacto para pegar.** En `conocimiento/playbook.md`, agregar después de T-27:

```markdown
- **T-32 · El precio nunca viaja solo: viaja con su plan.** Cuando corresponde dar el precio de una
  unidad de Casona 3 (porque lo pidió), en el mismo mensaje van, tal cual salen del tarifario, el
  **anticipo**, la **cantidad y el monto de la cuota** y el **saldo contra entrega**, y la aclaración
  de que la cuota puede ser en dólares o en pesos ajustados por CAC. En Casona 2, el precio va con
  «contado o crédito hipotecario con tu banco» y con la mención de que la cochera está incluida. El
  precio sin plan es un número contra el que la persona no tiene nada que comparar, y cierra la
  conversación. *(Woscoboinik, cap. 4: el precio se funda, no se justifica; regla 11 de
  fuentes_manuales: la mecánica del ajuste se adelanta por chat)*
- **T-33 · No se anuncia que no se da el precio.** Se dan la unidad, su diferencial y la forma de
  pago general, y se pasa al próximo paso. Frases como «antes de pasarte números» o «con eso te paso
  el valor» convierten el silencio del precio en una condición y provocan el pedido inmediato del
  número. Si lo pide igual, se da: una sola cifra, la de esa unidad, con su plan (T-32). *(Forte:
  guiar, no dejarse guiar; Villarroya: el objetivo es el avance)*
```

**Qué mirar en la próxima corrida.** Que ningún borrador de cliente final contenga «antes de pasarte
números» ni «con eso te paso el valor». Que en la corrida de C08 —donde la persona ya pidió dos
unidades y hay que cotizar— el borrador traiga anticipo, cuotas y saldo, y que V5 los valide contra
el tarifario.

---

## H-07 · El copiloto suena a formulario bien educado, no a Francisco

**Qué falla.** Los cuatro borradores para colegas empiezan **con la misma frase, palabra por
palabra**:

> «Hola! Francisco, de DOMINIA, por acá.»

Y los de cliente final con la misma estructura de cinco bloques. El contrato prohíbe una fórmula
concreta —«Sin fórmulas de apertura repetidas ("Hola! Todo bien por acá, gracias por escribir")»—
y el modelo la reemplazó por una fórmula propia, igual de repetida. Comparado con lo que el asesor
humano realmente contestó (C01, «Lo que pasó en la realidad»):

> 10:33 · Asesor: «Hola [nombre]» / «Muy bien! Vos?» / «Dale obvio!»

Tres burbujas, cero fricción, respuesta en 15 minutos. El copiloto responde a «hola wasooooooo»
(C03) con un bloque de cinco líneas que empieza presentándose ante alguien que lo tiene agendado.
Además: **tres de los cuatro colegas preguntaron «cómo estás»** («hola fran! como estas?», «hola
fran. cómo va? espero que muy bien», «Fran cómo estás !!!!!?») y solo uno de los cuatro borradores
lo contesta («Todo en orden.», C04 17:42). Un mensaje que no devuelve el saludo se lee como
plantilla, y el colega lo trata como plantilla.

**Respaldo.** Migliorisi, cap. 5, verificado en `fuentes_manuales.md`: *«Autenticidad frente a
guiones clonados: si todos usan el mismo léxico, el público se satura»*. Forte / T-17: *«Responder
a la persona antes que a la consulta»* — técnica que **no se cita en ninguna de las siete corridas
vigentes**, aunque sí aparecía en las corridas v1 de coherencia. Es una regresión introducida por la
pieza «formato» de la iteración 4.

**Texto exacto para pegar.** En `prompts/system_prompt.md`, `## 5 · Formato`, reemplazar el párrafo
final («Sin fórmulas de apertura repetidas…») por:

```markdown
  **Primero la persona, después la consulta (T-17).** Si el interesado o el colega preguntó cómo
  estás, se le contesta, en tres o cuatro palabras y antes que nada. Si dijo algo de sí mismo (que
  se muda, que alquila, que es para un hijo), la primera línea lo retoma con sus palabras.

  **Nada de aperturas clonadas.** La apertura cambia según quién escribe y cómo escribe: no se
  repite la misma frase de saludo entre dos borradores distintos, y con un colega que ya tiene al
  asesor agendado no se hace presentación institucional, alcanza el nombre. Se copia el registro del
  otro: si escribió corto e informal, se contesta corto e informal. Sin emojis, salvo que el
  interesado los use.

  **Con un colega, el borrador puede venir partido en dos mensajes**, separados por una línea con
  `---`: el primero, el saludo y la respuesta directa; el segundo, el detalle y el próximo paso. Así
  se parece a cómo se usa WhatsApp de verdad. Con un cliente final, siempre un solo mensaje.
```

**Qué mirar en la próxima corrida.** Que las cuatro aperturas de colegas sean **cuatro frases
distintas**. Que en C01, C02 y C04 la primera línea devuelva el saludo. Que la apertura de C03
(«hola wasooooooo») no contenga «asesor comercial de DOMINIA». Comparar cada borrador contra la
sección «Lo que pasó en la realidad»: si el borrador es más largo y más formal que lo que el asesor
mandó de verdad y que funcionó, todavía suena a formulario.

---

# IMPACTO MEDIO

## H-08 · T-24 se cita y no se cumple: la confirmación del día anterior no está en ningún borrador

**Qué falla.** T-24 dice: «Al agendar: día, hora, dirección y qué se va a ver, **con aviso de que se
confirma el día anterior**». En las siete corridas vigentes T-24 se cita dos veces (C01 y C03) y la
frase de confirmación **no aparece en ningún borrador**: en C01 queda relegada a
`revisar_antes_de_enviar` («Agregar dirección y aviso de confirmación el día anterior cuando quede el
horario cerrado (T-24)»), o sea, tarea manual para el asesor. Es la técnica más barata contra el
ausentismo y está sin ejecutar en el 100 % de los casos.

**Respaldo.** Villarroya vía inmonews, citado en `fuentes_manuales.md`: *«Al concertar se fija hora,
lugar, objetivo y modalidad, y se avisa que habrá una confirmación previa»*, con las tres salidas de
la confirmación. Harkins y Hollihan: *«La calidad y el profesionalismo se demuestran en actos
pequeños»* → «confirmar la visita, mandar la ubicación, llegar antes».

**Texto exacto para pegar.** En `prompts/system_prompt.md`, restricción 8, agregar un guion:

```markdown
   - cuando queda día y hora acordados (propuestos por el interesado o elegidos entre los dos que se
     ofrecen), incluye **siempre** una línea final antes de la firma con la dirección y el aviso de
     confirmación: «Te espero en Costanera de La Cañada 4140, Manantiales I; te confirmo el día
     anterior y te mando la ubicación.» (T-24);
```

Y agregar a `sistema/copiloto.py` el chequeo V13: si `proximo_paso.propuesta_de_visita` no es
`null`, el borrador tiene que contener «Costanera de La Cañada 4140» y alguna de las cadenas
«confirmo el día anterior» / «te confirmo».

**Qué mirar.** V13 en verde en C01, C02, C03, C04, C05 y C06. Que la ubicación aparezca como
compromiso («te mando la ubicación»), no como dato suelto.

---

## H-09 · Los dos horarios son inventados, y eso obliga al asesor a reescribir cada borrador

**Qué falla.** Los seis borradores que proponen horario lo hacen sin saber la agenda, y las seis
fichas incluyen la misma tarea manual: «Confirmar tu disponibilidad para sábado 22 a las 10 o lunes
24 a las 17» (C02), «Chequeá que los horarios propuestos te sirven» (C04), etc. Un copiloto que en
el 100 % de los casos obliga a corregir la línea más importante del mensaje se deja de usar. Además
propone horarios que el corpus contradice: los colegas visitan **por la siesta** («mañana por la
siesta», «hoy a las 12 30») y el plan de octubre programa la jornada de colegas en «franja
mediodía/siesta», pero los borradores ofrecen sistemáticamente 10 y 11 de la mañana.

**Respaldo.** Villarroya (concertar con hora, lugar, objetivo y modalidad) y Forte («la preparación
lo es todo»). El dato de las franjas es del propio corpus, no de un manual: es un dato de ficha que
falta.

**Texto exacto para pegar.** En `conocimiento/proyecto.md`, después de «Condiciones comerciales»:

```markdown
## Franjas de visita

- **Visitas al complejo:** Costanera de La Cañada 4140, Manantiales I. Se coordinan con el asesor.
- **Franjas habituales:** de lunes a viernes, de 10 a 13 y de 16 a 19; sábados de 10 a 13.
- **Las inmobiliarias colegas visitan casi siempre en la franja del mediodía y la siesta** (12 a
  15): cuando el que escribe es un colega, los dos horarios que se ofrecen salen de esa franja.
- Toda propuesta de horario es **sugerida**: el asesor la confirma contra su agenda antes de enviar.
- La reunión de plan de pagos y boleto (post-visita) es en la oficina de DOMINIA, Av. Vélez
  Sarsfield 522, o por videollamada.
```

*(Nota para el responsable: estas franjas son un supuesto de la auditoría deducido del corpus.
Confirmarlas con Francisco antes de dejarlas en la ficha, porque una vez escritas el copiloto las
va a usar como hechos.)*

**Qué mirar.** Que en las cuatro consultas de colegas los dos horarios caigan entre las 12 y las 15.
Que la línea «Confirmar tu disponibilidad» siga en `revisar_antes_de_enviar` pero deje de ser una
corrección de fondo.

---

## H-10 · Deriva de vocabulario entre corridas idénticas: «jardín privado» donde la ficha dice «de uso exclusivo»

**Qué falla.** Las dos corridas de coherencia sobre la **misma consulta palabra por palabra**
(`COH-PBA-2` y `COH-PBA-3`) devolvieron:

> «jardín privado de 29,25 m²» (COH-PBA-2)
> «29,25 m² de jardín privado» (COH-PBA-3)

y C08 (17:01) también: «PB B (2 dorm, 2 baños, con jardín privado)». La ficha del proyecto es
explícita en contra:

> «es un **espacio común de uso exclusivo**. […] No es un jardín "privado" en sentido legal: se dice
> "de uso exclusivo"»

Bajo el contrato vigente C06 (17:45) ya lo dice bien («jardín de uso exclusivo»), o sea que el
contrato v4 mejoró — pero **ningún chequeo lo garantiza**, y es exactamente el tipo de afirmación
escrita que, según la regla 8 de `fuentes_manuales.md` (Ley 9445 art. 16 y el fallo *Ahumada c/
Oliver Group*), integra la oferta y obliga a DOMINIA.

**Respaldo.** Ley 9445, art. 16 incs. m), n) y q) («publicidad clara, precisa y veraz sobre el
estado de hecho y jurídico del inmueble»); Código de Ética art. 1 b) inc. 5. T-18 y T-21.

**Texto exacto para pegar.** En `prompts/system_prompt.md`, agregar a las restricciones:

```markdown
14. **Palabras que no se escriben.** «jardín privado» (se dice «jardín de uso exclusivo»), «piscina
    olímpica» o «semiolímpica» (es «canal de nado de 25 metros»), «patio privado», «entrega en
    2029» a secas (es «entrega estimada en 2029»), «apto crédito» dicho de Casona 3 (el crédito
    hipotecario es para Casona 2), «cuota fija» (la cuota en pesos ajusta por CAC) y «reserva sin
    compromiso». Cada una de estas palabras es una afirmación escrita que obliga a DOMINIA.
```

Y el chequeo V14 en `sistema/copiloto.py`: lista negra de esas cadenas sobre `borrador_mensaje`.

**Qué mirar.** V14 en verde en las nueve consultas y en las dos de coherencia. Y que las dos
corridas de coherencia sobre la misma consulta produzcan el **mismo vocabulario** para el mismo
atributo, aunque cambie la redacción.

---

## H-11 · El envío mensual a colegas termina sin próximo paso, justo lo que T-14 prohíbe

**Qué falla.** `corridas/paquete_colegas/2026-10/mensaje.md` cierra así:

> «Si querés mostrar, avisame el día y la franja y coordino. Los honorarios los hablamos aparte.»

Eso es literalmente el ejemplo que T-14 da como error: «"Cualquier cosa me escribís" es un lead que
se cae». Es el mensaje de mayor alcance del sistema —va a **todas** las inmobiliarias colegas, una
vez por mes— y es el único que no tiene cierre. Además, el plan de octubre ya programó una **jornada
para colegas en el complejo, en franja mediodía/siesta**, y el mensaje no la menciona: se está
desperdiciando el único evento con fecha del mes.

**Respaldo.** T-14 y T-15 del playbook; Forte, «guiar, no dejarse guiar»; Código de Ética art. 1
c) («darles toda la información útil»).

**Texto exacto para pegar.** En `sistema/paquete_colegas.py`, en la plantilla del mensaje,
reemplazar el penúltimo párrafo por:

```
Dos cosas concretas. Primero: el [FECHA DE LA JORNADA] hacemos una recorrida para colegas en el
complejo, entre las 12 y las 15 —se ven los terminados, los amenities, el 2° F amoblado y la obra de
Casona 3—; decime si venís y te reservo el lugar. Segundo: si te quedó algún cliente de los que
trajiste sin definir, pasame el nombre y la tipología y te digo qué hay hoy para él.

¿Te queda mejor que coordinemos por acá o te llamo?
```

**Qué mirar.** Que el mensaje de noviembre traiga una fecha concreta de jornada y una pregunta de
cierre. Y medir lo único que importa: cuántos colegas contestan el envío de octubre contra el de
septiembre.

---

## H-12 · No se registra el resultado, así que ninguna de estas mejoras se va a poder medir

**Qué falla.** Las siete corridas terminan con el mismo bloque vacío:

> - Revisó:
> - Cambios al borrador:
> - ¿Se envió?:
> - Respuesta del interesado:

No hay un campo para lo único que define si el copiloto sirve: **si se agendó la visita**. Sin eso,
la próxima auditoría va a volver a ser cualitativa.

**Respaldo.** Harkins y Hollihan, verificado en `fuentes_manuales.md`: *«Pocas métricas "top-line",
simples y claras… Tres números para el equipo comercial: consultas respondidas, visitas agendadas y
visitas realizadas»*. Keller/MREA: leads → citas → contratos.

**Texto exacto para pegar.** En `sistema/copiloto.py`, en el bloque «Revisión humana»:

```markdown
- Revisó:
- Cambios al borrador (copiar el texto que se envió de verdad):
- ¿Se envió?: sí / no / se reescribió entero
- Respuesta del interesado:
- **¿Contestó?**: sí / no
- **¿Se agendó visita?**: sí / no / todavía no
- **¿Se hizo la visita?**: sí / no / reprogramada
- Toques de seguimiento enviados: 48 h ☐ · 7 días ☐ · 21 días ☐
```

**Qué mirar.** Al mes: consultas respondidas, visitas agendadas, visitas realizadas, y qué porcentaje
de borradores se envió sin cambios. Ese último número es la salud del copiloto.

---

## H-13 · C09 (canje): se maneja el riesgo, se pierde la oportunidad

**Qué falla.** El borrador de C09 responde impecablemente al riesgo:

> «Lo de tomar trabajos de carpintería a cuenta no te lo puedo confirmar por acá: lo converso con
> DOMINIA y te aviso.»

Correcto y no hay que tocarlo. Pero después el mensaje sigue como si fuera un lead cualquiera:
«¿pensás en 2 o en 3 dormitorios, y es para vivir o para invertir?». Es un **proveedor conocido, con
obras en curso, que se ofrece a aportar valor a la obra**: la ficha dice que DOMINIA «ha aceptado
canjes» y que «se evalúan caso por caso». El próximo paso natural no es una visita comercial: es la
**reunión a tres con DOMINIA**, que es donde el canje se define. El copiloto propone la visita
estándar («¿te queda mejor el jueves a las 10 o el sábado a las 11?») y deja pasar el único lead del
corpus con una vía de cierre propia.

**Respaldo.** T-10 (intereses, no posiciones: detrás del canje hay una restricción de efectivo que
se resuelve con estructura, no con precio) y T-13 (recomendar lo que le conviene). Ficha del
proyecto, «Canjes».

**Texto exacto para pegar.** En `conocimiento/proyecto.md`, en el punto «Canjes», agregar:

```markdown
  Si el interesado propone un canje, el próximo paso del mensaje **no es la visita sola**: es la
  visita **y** una reunión con el asesor y DOMINIA para evaluarlo, propuesta como una sola cosa
  («vamos primero a ver la unidad y de ahí, si te sirve, armamos una reunión con la desarrollista
  para ver lo del canje»). El copiloto no le pone valor, no dice cuánto se toma y no lo confirma.
```

**Qué mirar.** Que el borrador de C09 proponga la reunión con DOMINIA como parte del mismo paso, sin
sumar una tercera pregunta y sin poner ningún número al canje.

---

# IMPACTO BAJO

## H-14 · El diferencial más vendible casi no se usa

La ficha dice de los vidrios DVH: «Es el diferencial más vendible y el menos usado». En los siete
borradores vigentes **no aparece ni una vez** (sí aparece el jardín, cinco veces). El plan de
octubre le dedica un carrusel entero, pero el copiloto no lo escribe. **Texto para pegar** en el
playbook, dentro de T-18 o como técnica corta:

```markdown
- **T-34 · Un diferencial concreto por mensaje, elegido para esa persona.** El mensaje lleva un solo
  atributo, el que le sirve a quien escribe: DVH en dormitorios a quien viene por ruido, descanso o
  costo de climatización; jardín de uso exclusivo a quien pide planta baja o tiene chicos o perro;
  cochera incluida siempre que se dé un precio; canal de nado de 25 metros a quien pregunta por
  amenities. Nunca la lista completa de terminaciones. *(Migliorisi, cap. 5: un dato útil en la
  primera línea; Forte: comunicar los beneficios para ese público)*
```

**Qué mirar:** que al menos dos de las siete corridas nombren el DVH, y que ninguna enumere más de
dos terminaciones.

## H-15 · C07 (alquiler mensual): la puerta se cierra bien, pero no se deja abierta

El borrador dice, correctamente, «no tenemos alquileres ni alojamiento por mes». Después ofrece
asesorar en compra, lo cual está bien. Lo que falta es lo barato: el plan de octubre ya detectó el
problema de origen («Ajuste del texto del botón de WhatsApp y del encabezado de la web para aclarar
que es venta de unidades, no alquiler»). Mientras eso no se corrija, el copiloto debería dejar una
alerta fija para marketing en cada consulta que llegue con la intención equivocada — hoy la alerta
existe («conviene revisar de dónde llegó el contacto») pero es genérica. **Qué mirar:** que la
alerta nombre el botón concreto de la web.

## H-16 · Casona 1 no se usa nunca como prueba

T-12 (la respuesta a «¿y si se para la obra?») está bien escrita y solo se citó una vez, como
respaldo eventual. No hay caso en `entradas/` que la ejercite: **la respuesta a la objeción central
del comprador en pozo nunca se probó**. Igual pasa con T-19 (fideicomiso), T-20 (garantías), T-09,
T-10, T-11 y T-22. **Qué mirar:** agregar tres entradas reales de objeción (garantías, fideicomiso,
descuento) antes de la próxima auditoría; sin ellas, la mitad del playbook es teoría.

---

# Lo que ya está bien resuelto y no hay que tocar

1. **T-27, el silencio del precio en el primer mensaje al cliente.** Ejecutado limpio en C05 y C06:
   confirma disponibilidad, da el diferencial y la forma de pago general («se paga en cuotas durante
   la obra, en dólares o en pesos ajustados por CAC») sin la cifra. Es la mejora comercial más
   importante que ya tiene el sistema. No tocar (salvo el detalle de tono de H-06/T-33).
2. **La restricción 13.** C03: el colega dijo «hoy a las 12 30» y el borrador contesta «Dale, te
   confirmo: hoy martes 1/9 a las 12.30». Sin condiciones, sin contraoferta. Es la corrección de la
   iteración 1 y funcionó.
3. **T-18, los contras dichos de entrada.** «Te lo digo de entrada: es una unidad en obra, no para
   mudarse ya» (COH-PBA-2); «En 3 dormitorios no tengo planta baja» (C02); «Ojo que PB E y 1º G son
   de un baño» (C04 17:31). Esto genera confianza y ahorra visitas inútiles. Es lo mejor del
   sistema.
4. **El manejo de lo que no existe.** C07 (alquiler) y C08 (PB H, que la web ofrece y DOMINIA no
   vende): «El PB H no integra el stock a la venta, pero tenemos otros 1 dormitorio en planta baja».
   Impecable.
5. **El canje de C09**: «no te lo puedo confirmar por acá: lo converso con DOMINIA y te aviso». Es
   la aplicación textual de Migliorisi cap. 6.
6. **Las alertas al asesor.** Son concretas, accionables y honestas, incluidas las que exponen los
   límites del sistema («el audio de 0:16 no está transcripto: puede contener compromisos ya
   asumidos»). No convertirlas en checklist genérica.
7. **La disciplina de precios.** V3 y V5 en verde en las siete corridas, cero precios inventados,
   cero mezcla de listas, cero descuentos. Esa es la base sobre la que se puede construir todo lo
   demás; ningún cambio de esta auditoría debe ponerla en riesgo.
8. **El envío mensual a colegas** manda las dos listas juntas y **está bien** en este único caso,
   porque va acompañado de la instrucción correcta: «a cada cliente mostrale solo la lista que le
   corresponde según cómo va a pagar». Esa frase es lo que lo hace legítimo: no borrarla nunca, y no
   reutilizar ese mensaje con un cliente final.

---

# Lo que sería un error agregar

1. **Comparar Casona 2 y Casona 3 en un mensaje**, aunque sea «solo para mostrar la conveniencia».
   El pozo está 19 % **más caro**: la comparación gana la discusión y pierde la venta, y además rompe
   la restricción 1.
2. **Ofrecer el margen del 3 % / 5 % por escrito**, ni siquiera insinuado («podemos ver algo»,
   «hay lugar para conversar el precio»). Restricción 4, T-11 y Forte (no negociar en el primer
   contacto). Lo que sí corresponde es la pregunta que busca el interés detrás del pedido.
3. **Urgencia**: «quedan 8 unidades, decidí ahora», «el precio sube el mes que viene». T-23 y
   Villarroya («el cierre mágico»); en pozo, además, las fuentes legales lo listan como señal de
   alerta de estafa. El dato de stock se da como dato.
4. **Garantías**: nombrar el seguro, la fecha cierta del boleto o su inscripción. T-20: DOMINIA no
   las confirmó. Tampoco «rentabilidad», «revalorización» ni «precio final».
5. **Calcular la cuota en pesos o estimar el CAC.** Se dice la mecánica, nunca el número.
6. **Un seguimiento que se envíe solo.** El nivel de delegación es L2: el copiloto **prepara** los
   tres toques, el asesor los manda. Un bot que escribe al interesado rompe el rol declarado en la
   sección 1 del contrato («nunca le escribís al interesado») y es lo único de esta auditoría que
   podría dañar la marca.
7. **Más preguntas por mensaje.** Todo lo que propongo arriba **reemplaza** preguntas, no las suma.
   El techo de dos y el de 110 palabras son el motivo por el que estos borradores se pueden enviar
   sin editar.
8. **Pedir DNI, recibo de sueldo o ingresos exactos** para «calificar mejor». Restricción 9.
9. **Adjuntar la lista a un cliente final** «porque ya la pidió dos veces». Es la regla más
   importante del sistema.
10. **Emojis, adjetivos y superlativos** («el mejor complejo», «una oportunidad única»): la visita
    los desmiente y el Código de Ética los prohíbe (art. 1 b) inc. 5).

---

# Resumen de verificación para la próxima corrida

| # | Qué mirar | Verde si |
|---|---|---|
| 1 | Campo `seguimiento` en las 7 fichas | 3 toques, ninguno con «¿pudiste ver?» |
| 2 | Caso post-visita (entrada nueva) | `proximo_paso` = reunión de plan y boleto, no visita |
| 3 | T-06 en clientes con dato propio | 1 pregunta abierta de motivo o plazo, V9 ≤ 2 |
| 4 | Cadena «¿cómo pensabas pagarlo?» | Nunca sin cláusula de motivo delante |
| 5 | Mención de decisores | En los 6 borradores con visita, y sin sumar «?» |
| 6 | Colegas: línea del otro camino | En los 4, con V2 y V5 en verde |
| 7 | Precio con plan (anticipo/cuota/saldo) | En toda cotización de Casona 3 |
| 8 | «antes de pasarte números» | Cero apariciones |
| 9 | Aperturas de los 4 colegas | 4 frases distintas; saludo devuelto en 3 |
| 10 | V13 (dirección + confirmación día anterior) | Verde en las 6 con visita |
| 11 | V14 (lista negra: «jardín privado», etc.) | Verde en las 9 + coherencia |
| 12 | Horarios a colegas | Entre las 12 y las 15 |
| 13 | Coherencia COH-PBA-2 vs. COH-PBA-3 | Mismo vocabulario para el mismo atributo |
| 14 | DVH | Nombrado en ≥ 2 corridas |
| 15 | Bloque «Revisión humana» | Con «¿se agendó visita?» completable |

**Nota de implementación.** Cinco de estos cambios tocan `sistema/esquema_ficha.json` (campo
`seguimiento`) y `sistema/copiloto.py` (chequeos V13 y V14, bloque de revisión humana). Como el
esquema tiene `additionalProperties: false`, agregar el campo **sin** actualizar el esquema hace
fallar la validación por API en las 7 corridas. El orden correcto es: esquema → prompt → playbook →
corrida. Y todo esto se puede escribir sin gastar crédito: la corrida de verificación es lo único
que lo consume (~USD 0,15 por consulta, ~USD 1,50 la tanda completa de once).
