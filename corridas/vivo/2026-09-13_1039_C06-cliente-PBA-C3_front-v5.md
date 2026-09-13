# Corrida en vivo · C06-cliente-PBA-C3 · 13/09/2026 10:39

| Campo | Valor |
|---|---|
| Fecha de la corrida | 2026-09-13 10:39 (hora de Córdoba; el identificador `VIVO-202609131339` está en UTC) |
| Dónde corrió | Front del copiloto publicado, capacidad `sample`, a cuenta de la suscripción del responsable |
| Versión del contrato | **v5** (iteraciones 6 a 8) + playbook v3 + ficha con franjas de visita |
| Entrada | La misma consulta real de `entradas/consulta-06.md`, con la fecha cambiada a la del día |
| Cómo se obtuvo | Documento `corridas_vivo/VIVO-202609131339` de la base de datos de la página |
| Resultado en el front | BLOQUEADA: corregir antes de enviar |

## Entrada

```markdown
consulta_id: VIVO-202609131339
asesor: Francisco
canal: whatsapp
fecha: 2026-09-13

## Historial



## Consulta

Hola! Me interesa PB A (2 Dorm · 2 Baños) de Casona III.
```

## Salida

```json
{
  "alertas_para_el_asesor": [
    "Es primer contacto: no se conocen uso, capital, origen de fondos ni quién decide. Todo lo demás es inferencia.",
    "La lista quedó asignada por la unidad que eligió, no por su forma de pago: si contesta que califica a crédito o compra al contado, puede convenirle el terminado (T-13) y hay que rearmar la propuesta.",
    "El jardín de PB es espacio común de uso exclusivo, mantenido por el consorcio: decirlo así en la visita, nunca «jardín privado».",
    "Entrega de Casona 3: siempre «estimada 2029», nunca fecha cerrada.",
    "Si pide el precio, va una sola cifra (USD 247.582) con su plan: anticipo USD 99.033, 30 cuotas de USD 3.301 y USD 49.516 contra entrega, con la aclaración de USD o pesos ajustados por CAC."
  ],
  "borrador_mensaje": "Hola, buen día! Soy Francisco, asesor comercial de DOMINIA. Casona de los Arcos es un complejo cerrado de tres torres en Manantiales I, Córdoba, y Casona 3 es la torre que lo completa.\nEl PB A está disponible: 2 dormitorios, 2 baños, jardín de uso exclusivo y cochera incluida, en cuotas durante la obra.\nSegún cómo lo pienses pagar te conviene una cosa u otra: ¿lo veías en cuotas o al contado?\nPara verlo en persona, ¿te queda mejor el martes 15 a las 10 o el sábado 19 a las 11? Si la decisión la toman entre dos, mejor vengan los dos: así no repetimos la recorrida.\nFrancisco, Asesor Comercial de DOMINIA",
  "camino_del_comprador": {
    "etapa": "explorando",
    "evidencia": "«Me interesa PB A (2 Dorm · 2 Baños) de Casona III.»"
  },
  "canal": "whatsapp",
  "consulta_id": "VIVO-202609131339",
  "estrategia": {
    "objetivo_del_mensaje": "Confirmar que el PB A está disponible, definir cómo piensa pagar y cerrar día y hora de visita.",
    "que_no_decir_todavia": [
      "El precio, el anticipo y la cuota del PB A (solo si los pide)",
      "Cualquier referencia a Casona 2 o comparación de precios entre etapas",
      "Fecha de entrega cerrada: siempre «estimada 2029»",
      "Expensas, salvo que las pregunte",
      "Descuentos, márgenes o comisiones"
    ],
    "tecnicas": [
      {
        "codigo": "T-27",
        "como_se_aplica": "Primer mensaje sin precio: se confirma disponibilidad, diferencial (jardín de uso exclusivo, cochera) y forma de pago en términos generales."
      },
      {
        "codigo": "T-33",
        "como_se_aplica": "No se anuncia que el precio no se da: se pasa directo al próximo paso."
      },
      {
        "codigo": "T-28",
        "como_se_aplica": "La lista salió de la unidad elegida, así que la pregunta de calificación es cómo lo piensa pagar, dicha con su motivo."
      },
      {
        "codigo": "T-15",
        "como_se_aplica": "Dos horarios concretos (martes 15 a las 10 o sábado 19 a las 11), no una pregunta abierta."
      },
      {
        "codigo": "T-08",
        "como_se_aplica": "La mención de los decisores va pegada al horario, como aclaración y no como pregunta."
      },
      {
        "codigo": "T-14",
        "como_se_aplica": "El mensaje cierra con un próximo paso concreto: la visita."
      },
      {
        "codigo": "T-29",
        "como_se_aplica": "Quedan armados los tres toques de seguimiento por si no responde."
      }
    ]
  },
  "lista_asignada": {
    "lista": "casona_3_pozo",
    "motivo": "Eligió una unidad concreta de Casona 3 (PB A). La lista queda asignada por la unidad, no por lo que dijo de su forma de pago: por eso el borrador aplica T-28."
  },
  "perfil": {
    "evidencia": "No dice si es para vivir o invertir; solo nombra la unidad.",
    "tipo": "indefinido",
    "uso": "indefinido"
  },
  "proximo_paso": {
    "accion": "Coordinar visita al complejo con día y hora, y conocer la forma de pago que tiene en mente.",
    "propuesta_de_visita": "Martes 15/9 a las 10 o sábado 19/9 a las 11, en Costanera de La Cañada 4140, Manantiales I."
  },
  "resumen_consulta": "Primer contacto por WhatsApp: pide información sobre el PB A de Casona 3 (2 dormitorios, 2 baños), sin decir uso, plazo ni forma de pago.",
  "revisar_antes_de_enviar": [
    "Confirmar contra tu agenda los horarios propuestos (martes 15/9 10 h y sábado 19/9 11 h): son sugeridos.",
    "La consulta llegó un domingo: ajustar el saludo a la hora real de envío.",
    "Verificar en el tarifario que el PB A siga disponible antes de enviar.",
    "No adjuntar lista ni precios en este primer mensaje."
  ],
  "seguimiento": [
    {
      "aporte_de_valor": "Dato útil no dicho: la cochera está incluida y las expensas recién corren desde la posesión.",
      "cuando": "48h",
      "texto": "Hola! Te sumo dos datos del PB A: la cochera va incluida y las expensas recién se pagan desde la posesión, no durante el plan de obra. ¿Te sirve que coordinemos la visita?"
    },
    {
      "aporte_de_valor": "Novedad verificable: avance de obra y movimiento de stock en la tipología de 2 dormitorios.",
      "cuando": "7 dias",
      "texto": "Hola! Te puedo mostrar el avance de obra de Casona 3 y cómo viene el stock de 2 dormitorios con jardín. Si querés pasar a verlo, avisame y lo armamos."
    },
    {
      "aporte_de_valor": "Pregunta que cierra el ciclo y da permiso a decir que no.",
      "cuando": "21 dias",
      "texto": "Hola! ¿Seguís mirando o lo pausaste por ahora? Cualquiera de las dos me sirve para no escribirte de más. Francisco, DOMINIA."
    }
  ],
  "seis_datos": [
    {
      "dato": "uso",
      "estado": "falta",
      "valor": null
    },
    {
      "dato": "plazo",
      "estado": "inferido",
      "valor": "Compatible con esperar la obra (entrega estimada 2029), porque eligió una unidad de Casona 3; a confirmar."
    },
    {
      "dato": "capital_disponible",
      "estado": "falta",
      "valor": null
    },
    {
      "dato": "origen_fondos",
      "estado": "falta",
      "valor": null
    },
    {
      "dato": "quien_decide",
      "estado": "falta",
      "valor": null
    },
    {
      "dato": "alternativas",
      "estado": "falta",
      "valor": null
    }
  ],
  "unidades_propuestas": [
    {
      "dato_clave": "2 dorm, 2 baños, 69,8 m² cubiertos, jardín de uso exclusivo 29,25 m², cochera incluida. USD 247.582 · anticipo USD 99.033 + 30 cuotas de USD 3.301 + USD 49.516 contra entrega.",
      "edificio": "Casona 3",
      "por_que_esta": "Es exactamente la unidad que pidió y está disponible; en el primer mensaje se confirma disponibilidad y diferencial, sin precio (T-27).",
      "precio_lista_usd": 247582,
      "unidad": "PB A"
    }
  ]
}
```

### Borrador, tal como lo vería el asesor

> Hola, buen día! Soy Francisco, asesor comercial de DOMINIA. Casona de los Arcos es un complejo cerrado de tres torres en Manantiales I, Córdoba, y Casona 3 es la torre que lo completa.
> El PB A está disponible: 2 dormitorios, 2 baños, jardín de uso exclusivo y cochera incluida, en cuotas durante la obra.
> Según cómo lo pienses pagar te conviene una cosa u otra: ¿lo veías en cuotas o al contado?
> Para verlo en persona, ¿te queda mejor el martes 15 a las 10 o el sábado 19 a las 11? Si la decisión la toman entre dos, mejor vengan los dos: así no repetimos la recorrida.
> Francisco, Asesor Comercial de DOMINIA

### Seguimiento preparado, si no contesta

| Cuándo | Aporte de valor | Texto |
|---|---|---|
| 48h | Dato útil no dicho: la cochera está incluida y las expensas recién corren desde la posesión. | Hola! Te sumo dos datos del PB A: la cochera va incluida y las expensas recién se pagan desde la posesión, no durante el plan de obra. ¿Te sirve que coordinemos la visita? |
| 7 dias | Novedad verificable: avance de obra y movimiento de stock en la tipología de 2 dormitorios. | Hola! Te puedo mostrar el avance de obra de Casona 3 y cómo viene el stock de 2 dormitorios con jardín. Si querés pasar a verlo, avisame y lo armamos. |
| 21 dias | Pregunta que cierra el ciclo y da permiso a decir que no. | Hola! ¿Seguís mirando o lo pausaste por ahora? Cualquiera de las dos me sirve para no escribirte de más. Francisco, DOMINIA. |

## Verificación automática de reglas duras (tal como la corrió el front)

| | Regla | Detalle |
|---|---|---|
| ✅ V1 | Consultó el tarifario antes de responder | 2 llamada(s) |
| ✅ V2 | Lista única: unidades de un solo edificio y coherentes con la lista asignada | lista=casona_3_pozo; edificios propuestos=Casona 3 |
| ✅ V3 | Precios y disponibilidad idénticos al tarifario |  |
| ✅ V4 | Hasta 3 unidades propuestas | 1 unidad(es) |
| ✅ V5 | Todo monto en USD del borrador sale del tarifario de la lista asignada | 0 monto(s) |
| ✅ V6 | El borrador no menciona descuentos ni comisiones |  |
| ✅ V7 | El borrador no promete lo que no se puede cumplir ni mete urgencia artificial |  |
| ✅ V8 | Firma exacta del asesor | esperada: «Francisco, Asesor Comercial de DOMINIA» |
| ✅ V9 | Como máximo dos preguntas | 2 pregunta(s) |
| ✅ V10 | Menos de 120 palabras en WhatsApp o Instagram | 113 palabras · canal whatsapp |
| ✅ V11 | El asesor se presenta en la primera línea | primera línea: «Hola, buen día! Soy Francisco, asesor comercial de DOMINIA. Casona de los Arcos » |
| ✅ V12 | Días de la semana coherentes con las fechas propuestas | 2 fecha(s) verificada(s) |
| ❌ V13 | Si hay visita, el borrador lleva dirección y aviso de confirmación | falta la dirección y el aviso de confirmación |
| ✅ V14 | Sin vocabulario que la ficha desmiente (el jardín es de uso exclusivo) |  |

## Reverificación del 13/9 (sin volver a llamar al modelo)

- En el front salió **bloqueada por V13**: *«falta la dirección y el aviso de confirmación»*.
- **Era un falso positivo del chequeo**, no del modelo: V13 pedía dirección cuando había horarios *propuestos*, y la restricción 8 la exige cuando la visita queda *acordada*. Corregido el 13/9 (V13 aplica solo en la etapa `listo_para_visita`).
- Reverificada la misma ficha, sin volver a llamar al modelo: **aprobada**, 14 de 14.

## Consumo y costo

No aplica: corrió con la capacidad `sample` de la página, sin API.

## Revisión humana

- Revisó: sí, en el front
- ¿Se envió?: no
- **¿Contestó?**:
- **¿Se agendó visita?**:
- **¿Se hizo la visita?**:
