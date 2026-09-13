# Corrida en vivo · C08-cliente-PBB-o-PBH · 13/09/2026 13:40

| Campo | Valor |
|---|---|
| Fecha de la corrida | 2026-09-13 13:40 (hora de Córdoba) |
| Dónde corrió | Front del copiloto publicado, capacidad `sample`, a cuenta de la suscripción del responsable |
| Versión del contrato | **v5** (iteraciones 6 a 8) + playbook v3 + ficha con franjas de visita |
| Entrada | La misma consulta real de `entradas/consulta-08.md`, con la fecha cambiada a la del día |
| Cómo se obtuvo | Documento `corridas_vivo/VIVO-202609131340` de la base de datos de la página |
| Resultado en el front | BLOQUEADA: corregir antes de enviar |

## Entrada

```markdown
consulta_id: VIVO-202609131340
asesor: Francisco
canal: whatsapp
fecha: 2026-09-13

## Historial



## Consulta

Hola! Me interesa PB B (2 Dorm · 2 Baños) de Casona III.
Hola! Me interesa PB H (1 Dorm · 1 Baño) de Casona III.
Cualquier de los dos
```

## Salida

```json
{
  "alertas_para_el_asesor": [
    "PB H figura como no disponible («No está a la venta»): no se ofrece; el borrador propone PB D como reemplazo.",
    "Consulta cargada desde el visor: la lista Casona 3 quedó asignada por la unidad elegida, no por la forma de pago. Si dice que paga al contado o con crédito, puede convenirle otro camino (T-13): revisar antes de avanzar.",
    "Los seis datos están todos en falta: es un primer contacto frío.",
    "Pide indistintamente un 2 dormitorios y un 1 dormitorio: la diferencia de presupuesto es grande, conviene calificar en la visita."
  ],
  "borrador_mensaje": "Hola, buenas tardes! Soy Francisco, asesor comercial de DOMINIA. Casona de los Arcos es un complejo cerrado de tres torres en Manantiales I; Casona 3 es la torre que lo completa y está en obra.\nEl PB B (2 dormitorios, 2 baños, jardín de uso exclusivo y cochera) está disponible. El PB H no está a la venta: la misma tipología de 1 dormitorio la tenés en el PB D, también en planta baja, con jardín y cochera.\nCasona 3 se compra con un anticipo y cuotas durante la obra. Según cómo lo pienses pagar te preparo lo que corresponde: ¿lo veías en cuotas o al contado?\nY para verlo, ¿el sábado a las 10 o a las 11? Si la decisión la toman entre dos, mejor vengan los dos.\nFrancisco, Asesor Comercial de DOMINIA",
  "camino_del_comprador": {
    "etapa": "explorando",
    "evidencia": "«Me interesa PB B… Me interesa PB H… Cualquier de los dos»"
  },
  "canal": "whatsapp",
  "consulta_id": "VIVO-202609131340",
  "estrategia": {
    "objetivo_del_mensaje": "Confirmar qué está disponible (y qué no), aclarar que Casona 3 se paga con plan durante la obra, y llevar la conversación a la visita con día y hora.",
    "que_no_decir_todavia": [
      "Precios y plan de pagos detallados (van cuando los pida o en la visita)",
      "Cualquier referencia a Casona 2 o a la comparación de precios entre terminado y pozo",
      "Expensas, salvo que las pregunte",
      "Fecha de entrega cerrada: solo «estimada 2029»"
    ],
    "tecnicas": [
      {
        "codigo": "T-27",
        "como_se_aplica": "Primer mensaje sin precio: se confirma disponibilidad, el diferencial (jardín de uso exclusivo, cochera) y la forma de pago en términos generales."
      },
      {
        "codigo": "T-33",
        "como_se_aplica": "No se anuncia que no se da el precio: se pasa directo al próximo paso."
      },
      {
        "codigo": "T-28",
        "como_se_aplica": "La lista salió del botón: la primera pregunta es cómo lo pensaba pagar, dicha con su motivo («así te preparo lo que corresponde»)."
      },
      {
        "codigo": "T-18",
        "como_se_aplica": "Se dice de entrada que el PB H no está a la venta, antes de que lo descubra."
      },
      {
        "codigo": "T-15",
        "como_se_aplica": "Dos horarios concretos (sábado 19/9 a las 10 o a las 11) en lugar de pregunta abierta."
      },
      {
        "codigo": "T-08",
        "como_se_aplica": "La mención de los decisores va pegada al horario, como aclaración y no como pregunta."
      },
      {
        "codigo": "T-29",
        "como_se_aplica": "Quedan armados los tres toques por si no contesta."
      }
    ]
  },
  "lista_asignada": {
    "lista": "casona_3_pozo",
    "motivo": "Eligió desde el visor dos unidades de Casona III; la lista queda asignada por el botón, no por la forma de pago declarada (por eso el borrador aplica T-28)."
  },
  "perfil": {
    "evidencia": "No dice para qué lo quiere ni cómo lo paga; consultar por un 2 dormitorios y un 1 dormitorio indistintamente no permite inferir uso.",
    "tipo": "indefinido",
    "uso": "indefinido"
  },
  "proximo_paso": {
    "accion": "Visita al complejo con dos horarios a elección y pregunta de calificación sobre forma de pago",
    "propuesta_de_visita": "sábado 19/9/2026 a las 10 o a las 11"
  },
  "resumen_consulta": "Escribe por dos unidades de Casona 3 desde el visor: PB B (2 dorm/2 baños) y PB H (1 dorm/1 baño), y aclara que le sirve cualquiera de las dos.",
  "revisar_antes_de_enviar": [
    "Confirmar contra tu agenda el sábado 19/9 a las 10 y a las 11 (franja sábados 10 a 13).",
    "Verificar en el tarifario que PB B y PB D sigan disponibles al momento de enviar.",
    "Ajustar el saludo a la hora real en que enviás el mensaje.",
    "No agregar precios en este mensaje; si los pide, van con anticipo, cuotas y saldo contra entrega."
  ],
  "seguimiento": [
    {
      "aporte_de_valor": "Dato útil que no se dijo: cochera incluida y expensas recién desde la posesión",
      "cuando": "48h",
      "texto": "Francisco, de DOMINIA. Un dato del PB B y del PB D: las dos incluyen cochera, y las expensas se pagan recién desde la posesión, no durante el plan. ¿Te sirve el sábado?"
    },
    {
      "aporte_de_valor": "Novedad verificable: avance de obra y movimiento de stock en 1 dormitorio",
      "cuando": "7 dias",
      "texto": "Te cuento cómo viene la obra de Casona 3 y cómo se mueven los de 1 dormitorio, que son pocos. Si querés verlo en persona, coordinamos un día de esta semana."
    },
    {
      "aporte_de_valor": "Pregunta que cierra el ciclo y da permiso a decir que no",
      "cuando": "21 dias",
      "texto": "Francisco, de DOMINIA. ¿Seguís mirando o lo pausaste por ahora? Cualquiera de las dos me sirve para saber si te escribo más adelante."
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
      "estado": "falta",
      "valor": null
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
      "dato_clave": "2 dorm, 2 baños, 77,08 m² cubiertos, 32,5 m² de jardín de uso exclusivo, cochera incluida; anticipo USD 105.023, 30 cuotas de USD 3.501 y saldo contra entrega USD 52.511",
      "edificio": "Casona 3",
      "por_que_esta": "Es una de las dos unidades que pidió expresamente y está disponible.",
      "precio_lista_usd": 262557,
      "unidad": "PB B"
    },
    {
      "dato_clave": "1 dorm, 46,62 m² cubiertos, 14,4 m² de jardín de uso exclusivo, cochera incluida; anticipo USD 66.383, 30 cuotas de USD 2.213 y saldo contra entrega USD 33.192",
      "edificio": "Casona 3",
      "por_que_esta": "Reemplaza al PB H, que no está a la venta: misma tipología de 1 dormitorio, en planta baja y con jardín de uso exclusivo.",
      "precio_lista_usd": 165958,
      "unidad": "PB D"
    },
    {
      "dato_clave": "1 dorm en altura, 46,62 m² cubiertos, balcón 2,7 m², cochera incluida; anticipo USD 65.911, 30 cuotas de USD 2.197 y saldo contra entrega USD 32.955",
      "edificio": "Casona 3",
      "por_que_esta": "Alternativa de 1 dormitorio en altura, tipología que en terminado no existe; queda como segunda opción si prefiere piso alto a jardín.",
      "precio_lista_usd": 164777,
      "unidad": "1º D"
    }
  ]
}
```

### Borrador, tal como lo vería el asesor

> Hola, buenas tardes! Soy Francisco, asesor comercial de DOMINIA. Casona de los Arcos es un complejo cerrado de tres torres en Manantiales I; Casona 3 es la torre que lo completa y está en obra.
> El PB B (2 dormitorios, 2 baños, jardín de uso exclusivo y cochera) está disponible. El PB H no está a la venta: la misma tipología de 1 dormitorio la tenés en el PB D, también en planta baja, con jardín y cochera.
> Casona 3 se compra con un anticipo y cuotas durante la obra. Según cómo lo pienses pagar te preparo lo que corresponde: ¿lo veías en cuotas o al contado?
> Y para verlo, ¿el sábado a las 10 o a las 11? Si la decisión la toman entre dos, mejor vengan los dos.
> Francisco, Asesor Comercial de DOMINIA

### Seguimiento preparado, si no contesta

| Cuándo | Aporte de valor | Texto |
|---|---|---|
| 48h | Dato útil que no se dijo: cochera incluida y expensas recién desde la posesión | Francisco, de DOMINIA. Un dato del PB B y del PB D: las dos incluyen cochera, y las expensas se pagan recién desde la posesión, no durante el plan. ¿Te sirve el sábado? |
| 7 dias | Novedad verificable: avance de obra y movimiento de stock en 1 dormitorio | Te cuento cómo viene la obra de Casona 3 y cómo se mueven los de 1 dormitorio, que son pocos. Si querés verlo en persona, coordinamos un día de esta semana. |
| 21 dias | Pregunta que cierra el ciclo y da permiso a decir que no | Francisco, de DOMINIA. ¿Seguís mirando o lo pausaste por ahora? Cualquiera de las dos me sirve para saber si te escribo más adelante. |

## Verificación automática de reglas duras (tal como la corrió el front)

| | Regla | Detalle |
|---|---|---|
| ✅ V1 | Consultó el tarifario antes de responder | 2 llamada(s) |
| ✅ V2 | Lista única: unidades de un solo edificio y coherentes con la lista asignada | lista=casona_3_pozo; edificios propuestos=Casona 3 |
| ✅ V3 | Precios y disponibilidad idénticos al tarifario |  |
| ✅ V4 | Hasta 3 unidades propuestas | 3 unidad(es) |
| ✅ V5 | Todo monto en USD del borrador sale del tarifario de la lista asignada | 0 monto(s) |
| ✅ V6 | El borrador no menciona descuentos ni comisiones |  |
| ✅ V7 | El borrador no promete lo que no se puede cumplir ni mete urgencia artificial |  |
| ✅ V8 | Firma exacta del asesor | esperada: «Francisco, Asesor Comercial de DOMINIA» |
| ✅ V9 | Como máximo dos preguntas | 2 pregunta(s) |
| ❌ V10 | Menos de 120 palabras en WhatsApp o Instagram | 135 palabras · canal whatsapp |
| ✅ V11 | El asesor se presenta en la primera línea | primera línea: «Hola, buenas tardes! Soy Francisco, asesor comercial de DOMINIA. Casona de los A» |
| ✅ V12 | Días de la semana coherentes con las fechas propuestas | 1 fecha(s) verificada(s) |
| ❌ V13 | Si hay visita, el borrador lleva dirección y aviso de confirmación | falta la dirección y el aviso de confirmación |
| ✅ V14 | Sin vocabulario que la ficha desmiente (el jardín es de uso exclusivo) |  |

## Reverificación del 13/9 (sin volver a llamar al modelo)

- En el front salió **bloqueada por V10 y V13**.
- V13 era el mismo falso positivo que en la C06, corregido el 13/9.
- **V10 es una falla real y queda abierta**: *«135 palabras · canal whatsapp»*. Reverificada con los chequeos corregidos: **sigue bloqueada** por V10.

## Consumo y costo

No aplica: corrió con la capacidad `sample` de la página, sin API.

## Revisión humana

- Revisó: sí, en el front
- ¿Se envió?: no
- **¿Contestó?**:
- **¿Se agendó visita?**:
- **¿Se hizo la visita?**:
