# Corrida en vivo · C08-cliente-PBB-o-PBH · 13/09/2026 10:49

| Campo | Valor |
|---|---|
| Fecha de la corrida | 2026-09-13 10:49 (hora de Córdoba; el identificador `VIVO-202609131349` está en UTC) |
| Dónde corrió | Front del copiloto publicado, capacidad `sample`, a cuenta de la suscripción del responsable |
| Versión del contrato | **v6** (iteración 9, pieza formato) + playbook v3 |
| Entrada | La misma consulta real de `entradas/consulta-08.md`, con la fecha del día |
| Cómo se obtuvo | Documento `corridas_vivo/VIVO-202609131349` de la base de datos de la página |
| Resultado en el front | aprobada para revisión |
| Con los chequeos vigentes (13/9, reverificada sin llamar al modelo) | BLOQUEADA (V15) |

## Entrada

```markdown
consulta_id: VIVO-202609131349
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
    "PB H figura como no disponible («No está a la venta»): no ofrecerlo bajo ningún concepto.",
    "La lista Casona 3 quedó asignada por las unidades del visor, no por su forma de pago: si califica a crédito o quiere escriturar ya, puede convenirle el otro camino (T-13) — preguntarlo en la visita.",
    "No se dio ningún precio: si pide el número, dar una sola cifra con su plan completo (anticipo, 30 cuotas y saldo contra entrega, en USD o pesos ajustados por CAC)."
  ],
  "borrador_mensaje": "Hola, buen día! Soy Francisco, asesor comercial de DOMINIA. Te cuento: el PB B de Casona 3 (2 dormitorios, 2 baños) está disponible, en planta baja con jardín de uso exclusivo y cochera. El PB H no está a la venta; lo más parecido es el PB D, 1 dormitorio también en planta baja, con jardín y cochera. Las dos se toman en cuotas durante la obra. Lo mejor es verlas en el lugar: ¿te queda mejor el miércoles 16 a las 17 o el sábado 19 a las 10? Si la decisión la toman entre dos, mejor vengan los dos, así no repetimos la recorrida. Contame si es para vivir o para invertir.\nFrancisco, Asesor Comercial de DOMINIA",
  "camino_del_comprador": {
    "etapa": "explorando",
    "evidencia": "«Me interesa PB B (2 Dorm · 2 Baños) de Casona III… Cualquier de los dos»"
  },
  "canal": "whatsapp",
  "consulta_id": "VIVO-202609131349",
  "estrategia": {
    "objetivo_del_mensaje": "Confirmar qué está disponible, resolver el PB H sin precio y llevar la conversación a una visita con día y hora",
    "que_no_decir_todavia": [
      "Precios de PB B, PB D ni de ninguna unidad",
      "Cualquier referencia a Casona 2 o comparación terminado/pozo",
      "Fecha de entrega cerrada",
      "Descuentos o márgenes"
    ],
    "tecnicas": [
      {
        "codigo": "T-27",
        "como_se_aplica": "Primer mensaje sin precio: se confirma disponibilidad, el diferencial y la forma de pago en términos generales"
      },
      {
        "codigo": "T-33",
        "como_se_aplica": "No se anuncia que no se da el precio; se pasa directo al próximo paso"
      },
      {
        "codigo": "T-18",
        "como_se_aplica": "Se dice de entrada que el PB H no está a la venta y se ofrece el más parecido"
      },
      {
        "codigo": "T-28",
        "como_se_aplica": "La lista salió del visor, así que queda pendiente confirmar cómo lo piensa pagar; en este mensaje se prioriza uso por límite de preguntas"
      },
      {
        "codigo": "T-15",
        "como_se_aplica": "Dos horarios concretos dentro de las franjas habituales"
      },
      {
        "codigo": "T-08",
        "como_se_aplica": "Mención de los decisores pegada a la línea del horario, como aclaración"
      }
    ]
  },
  "lista_asignada": {
    "lista": "casona_3_pozo",
    "motivo": "Las dos unidades que eligió (PB B y PB H) son de Casona 3: la lista quedó asignada por la unidad elegida en el visor, no por su forma de pago (por eso la primera pregunta debe ser la de calificación, T-28)."
  },
  "perfil": {
    "evidencia": "No dice uso, plazo ni forma de pago; solo nombra dos unidades del visor",
    "tipo": "indefinido",
    "uso": "indefinido"
  },
  "proximo_paso": {
    "accion": "Coordinar visita al complejo con dos horarios a elección y con los decisores",
    "propuesta_de_visita": "miércoles 16/9 a las 17 o sábado 19/9 a las 10"
  },
  "resumen_consulta": "Pregunta por dos unidades de Casona 3 desde el visor: PB B (2 dorm, 2 baños) y PB H (1 dorm, 1 baño), y aclara que le sirve cualquiera de las dos.",
  "revisar_antes_de_enviar": [
    "Confirmar contra agenda los horarios sugeridos (miércoles 16/9 17 h y sábado 19/9 10 h).",
    "Verificar que PB H sigue sin estar a la venta antes de enviar.",
    "Al cerrar día y hora, agregar la línea con la dirección (Costanera de La Cañada 4140, Manantiales I) y el aviso de confirmación del día anterior."
  ],
  "seguimiento": [
    {
      "aporte_de_valor": "Dato útil no dicho: cochera incluida y expensas recién desde la posesión",
      "cuando": "48h",
      "texto": "Francisco, de DOMINIA. Un dato de las unidades que miraste: las dos incluyen cochera, y las expensas se empiezan a pagar recién desde la posesión, no durante el plan. ¿Coordinamos la visita?"
    },
    {
      "aporte_de_valor": "Novedad verificable: avance de obra y movimiento de stock en esa tipología",
      "cuando": "7 dias",
      "texto": "Hola! Te cuento cómo viene la obra de Casona 3 y cómo quedó el stock de planta baja esta semana. Si querés pasar a verlo, el sábado a las 10 tengo lugar."
    },
    {
      "aporte_de_valor": "Pregunta que cierra el ciclo y permite decir que no",
      "cuando": "21 dias",
      "texto": "Hola! ¿Seguís mirando o lo pausaste por ahora? Cualquiera de las dos me sirve para saber si te sigo mandando novedades."
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
      "dato_clave": "2 dorm / 2 baños en PB, 77,08 m² cubiertos, 32,5 m² de jardín de uso exclusivo, cochera incluida; 40% anticipo + 30 cuotas + 20% contra entrega",
      "edificio": "Casona 3",
      "por_que_esta": "Es una de las dos unidades que pidió expresamente y está disponible",
      "precio_lista_usd": 262557,
      "unidad": "PB B"
    },
    {
      "dato_clave": "1 dorm / 1 baño en PB, 46,62 m² cubiertos, 14,4 m² de jardín de uso exclusivo, cochera incluida",
      "edificio": "Casona 3",
      "por_que_esta": "Reemplaza al PB H, que no está a la venta: misma tipología, misma planta y mismos m² cubiertos",
      "precio_lista_usd": 165958,
      "unidad": "PB D"
    }
  ]
}
```

### Borrador, tal como lo vería el asesor

> Hola, buen día! Soy Francisco, asesor comercial de DOMINIA. Te cuento: el PB B de Casona 3 (2 dormitorios, 2 baños) está disponible, en planta baja con jardín de uso exclusivo y cochera. El PB H no está a la venta; lo más parecido es el PB D, 1 dormitorio también en planta baja, con jardín y cochera. Las dos se toman en cuotas durante la obra. Lo mejor es verlas en el lugar: ¿te queda mejor el miércoles 16 a las 17 o el sábado 19 a las 10? Si la decisión la toman entre dos, mejor vengan los dos, así no repetimos la recorrida. Contame si es para vivir o para invertir.
> Francisco, Asesor Comercial de DOMINIA

### Seguimiento preparado, si no contesta

| Cuándo | Aporte de valor | Texto |
|---|---|---|
| 48h | Dato útil no dicho: cochera incluida y expensas recién desde la posesión | Francisco, de DOMINIA. Un dato de las unidades que miraste: las dos incluyen cochera, y las expensas se empiezan a pagar recién desde la posesión, no durante el plan. ¿Coordinamos la visita? |
| 7 dias | Novedad verificable: avance de obra y movimiento de stock en esa tipología | Hola! Te cuento cómo viene la obra de Casona 3 y cómo quedó el stock de planta baja esta semana. Si querés pasar a verlo, el sábado a las 10 tengo lugar. |
| 21 dias | Pregunta que cierra el ciclo y permite decir que no | Hola! ¿Seguís mirando o lo pausaste por ahora? Cualquiera de las dos me sirve para saber si te sigo mandando novedades. |

## Verificación automática de reglas duras (tal como la corrió el front)

| | Regla | Detalle |
|---|---|---|
| ✅ V1 | Consultó el tarifario antes de responder | 2 llamada(s) |
| ✅ V2 | Lista única: unidades de un solo edificio y coherentes con la lista asignada | lista=casona_3_pozo; edificios propuestos=Casona 3 |
| ✅ V3 | Precios y disponibilidad idénticos al tarifario |  |
| ✅ V4 | Hasta 3 unidades propuestas | 2 unidad(es) |
| ✅ V5 | Todo monto en USD del borrador sale del tarifario de la lista asignada | 0 monto(s) |
| ✅ V6 | El borrador y el seguimiento no mencionan descuentos ni comisiones |  |
| ✅ V7 | El borrador no promete lo que no se puede cumplir ni mete urgencia artificial |  |
| ✅ V8 | Firma exacta del asesor | esperada: «Francisco, Asesor Comercial de DOMINIA» |
| ✅ V9 | Como máximo dos preguntas | 1 pregunta(s) |
| ✅ V10 | Menos de 120 palabras en WhatsApp o Instagram | 119 palabras · canal whatsapp |
| ✅ V11 | El asesor se presenta en la primera línea | primera línea: «Hola, buen día! Soy Francisco, asesor comercial de DOMINIA. Te cuento: el PB B d» |
| ✅ V12 | Días de la semana coherentes con las fechas propuestas | 2 fecha(s) verificada(s) |
| ✅ V13 | Si la visita quedó acordada, el borrador lleva dirección y aviso de confirmación | la visita todavía no está acordada |
| ✅ V14 | Sin vocabulario que la ficha desmiente (el jardín es de uso exclusivo) |  |

## Reverificación del 13/9 (sin volver a llamar al modelo)

- Aprobada con los chequeos de ese momento.
- **Con el chequeo V15 (13/9, D-20) queda BLOQUEADA**: *«no pregunta cómo piensa pagar»*. El borrador entró en el largo preguntando el uso (*«Contame si es para vivir o para invertir»*) en lugar de la forma de pago que exige la T-28.

## Consumo y costo

No aplica: corrió con la capacidad `sample` de la página, sin API.

## Revisión humana

- Revisó: sí, en el front
- ¿Se envió?: no
- **¿Contestó?**:
- **¿Se agendó visita?**:
- **¿Se hizo la visita?**:
