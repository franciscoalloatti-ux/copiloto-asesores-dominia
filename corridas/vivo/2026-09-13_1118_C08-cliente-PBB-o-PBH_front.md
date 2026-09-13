# Corrida en vivo · C08-cliente-PBB-o-PBH · 13/09/2026 11:18

| Campo | Valor |
|---|---|
| Fecha de la corrida | 2026-09-13 11:18 (hora de Córdoba; el identificador `VIVO-202609131418` está en UTC) |
| Dónde corrió | Front del copiloto publicado, capacidad `sample`, a cuenta de la suscripción del responsable |
| Versión del contrato | **v7** (iteración 10, pieza formato) + playbook v3 + chequeo V15 |
| Entrada | La misma consulta real de `entradas/consulta-08.md`, con la fecha del día |
| Cómo se obtuvo | Documento `corridas_vivo/VIVO-202609131418` de la base de datos de la página |
| Resultado en el front | aprobada para revisión |
| Con los chequeos vigentes (13/9, reverificada sin llamar al modelo) | aprobada para revisión |

## Entrada

```markdown
consulta_id: VIVO-202609131418
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
    "PB H no está a la venta: no ofrecerla bajo ningún concepto",
    "La lista Casona 3 quedó asignada por la unidad que eligió en el visor, no por su forma de pago: si contesta que va con crédito o contado, puede convenirle el terminado (T-13)",
    "No se dieron precios: si los pide, se da una sola cifra con su plan completo (anticipo, 30 cuotas y saldo contra entrega)",
    "Entrega de Casona 3: 2029 estimada, nunca fecha cerrada"
  ],
  "borrador_mensaje": "Hola, buen día! Soy Francisco, asesor comercial de DOMINIA.\nLa PB B de Casona 3, 2 dormitorios con 2 baños, jardín de uso exclusivo y cochera, está disponible. La PB H no está a la venta; lo más parecido en 1 dormitorio es la PB D, también en planta baja, con jardín y cochera.\nSegún cómo lo pienses pagar te conviene una cosa u otra —tenemos terminado para escriturar ya y en obra con cuotas—, así que decime: ¿lo veías al contado o con crédito, o te sirve más el plan en cuotas?\nPara verlas, ¿te queda mejor el martes 15 a las 10 o a las 17?\nFrancisco, Asesor Comercial de DOMINIA",
  "camino_del_comprador": {
    "etapa": "explorando",
    "evidencia": "«Me interesa PB B (2 Dorm · 2 Baños) de Casona III… Cualquier de los dos»"
  },
  "canal": "whatsapp",
  "consulta_id": "VIVO-202609131418",
  "estrategia": {
    "objetivo_del_mensaje": "Confirmar qué está disponible, decir de frente que PB H no se vende y ofrecer el reemplazo, definir la forma de pago y cerrar la visita",
    "que_no_decir_todavia": [
      "Precios de PB B ni de PB D (solo si los pide, una cifra con su plan, T-32)",
      "Cualquier precio o comparación con Casona 2",
      "Fecha de entrega cerrada: es 2029 estimada",
      "Expensas, salvo que pregunte"
    ],
    "tecnicas": [
      {
        "codigo": "T-18",
        "como_se_aplica": "Se avisa de entrada que la PB H no está a la venta, sin adornar"
      },
      {
        "codigo": "T-27",
        "como_se_aplica": "Primer mensaje sin precio: disponibilidad, diferencial y forma de pago en términos generales"
      },
      {
        "codigo": "T-28",
        "como_se_aplica": "La pregunta de cómo paga va con su motivo, porque la lista quedó asignada por la unidad del visor"
      },
      {
        "codigo": "T-15",
        "como_se_aplica": "Dos horarios concretos para la visita, no una pregunta abierta"
      },
      {
        "codigo": "T-33",
        "como_se_aplica": "No se anuncia que no se da el precio; se pasa directo al próximo paso"
      }
    ]
  },
  "lista_asignada": {
    "lista": "casona_3_pozo",
    "motivo": "Las dos unidades que eligió son de Casona 3; la lista queda asignada por la unidad elegida en el visor, no por su forma de pago, así que el borrador hace la pregunta de pago (T-28)."
  },
  "perfil": {
    "evidencia": "No dice para qué la quiere ni cómo la pagaría; solo eligió unidades desde el visor",
    "tipo": "indefinido",
    "uso": "indefinido"
  },
  "proximo_paso": {
    "accion": "Visita al complejo con dos horarios a elección y pregunta de forma de pago",
    "propuesta_de_visita": "Martes 15/9 a las 10 o a las 17 (a confirmar contra agenda del asesor)"
  },
  "resumen_consulta": "Pregunta por PB B (2 dorm) y PB H (1 dorm) de Casona 3 y dice que le sirve cualquiera de las dos; PB H no está a la venta.",
  "revisar_antes_de_enviar": [
    "Confirmar los horarios propuestos (martes 15/9, 10 o 17 h) contra tu agenda; el mensaje se envía el lunes si preferís no escribir domingo",
    "Verificar en el tarifario que PB B y PB D sigan disponibles al momento de enviar",
    "Ajustar el saludo a la hora real de envío"
  ],
  "seguimiento": [
    {
      "aporte_de_valor": "Dato útil no dicho: cochera incluida y expensas recién desde la posesión",
      "cuando": "48h",
      "texto": "Hola! Un dato que suma: las dos incluyen cochera y las expensas recién se pagan desde la posesión, durante el plan no corren. ¿Te sirve que coordinemos la visita esta semana?"
    },
    {
      "aporte_de_valor": "Novedad verificable: avance de obra y estado de stock de esa tipología",
      "cuando": "7 dias",
      "texto": "Hola! Te cuento cómo viene la obra de Casona 3 y qué queda de planta baja con jardín, que es lo que mirabas. ¿Querés que te pase el detalle?"
    },
    {
      "aporte_de_valor": "Pregunta que cierra el ciclo y da permiso a decir que no",
      "cuando": "21 dias",
      "texto": "Hola! Última consulta y no te molesto más: ¿seguís mirando o lo pausaste por ahora?"
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
      "estado": "inferido",
      "valor": "Duda entre 1 y 2 dormitorios de Casona 3 («cualquiera de los dos»): todavía no tiene definida la tipología"
    }
  ],
  "unidades_propuestas": [
    {
      "dato_clave": "77,08 m² cubiertos, 32,5 m² de jardín de uso exclusivo, 2 baños, cochera incluida; 40% anticipo + 30 cuotas + 20% contra entrega",
      "edificio": "Casona 3",
      "por_que_esta": "Es una de las dos unidades que pidió y está disponible; 2 dormitorios con 2 baños en PB con jardín",
      "precio_lista_usd": 262557,
      "unidad": "PB B"
    },
    {
      "dato_clave": "46,62 m² cubiertos, 14,4 m² de jardín de uso exclusivo, cochera incluida; mismo plan de pago",
      "edificio": "Casona 3",
      "por_que_esta": "Reemplazo más parecido a la PB H que pidió (1 dormitorio en planta baja con jardín), ya que PB H no está a la venta",
      "precio_lista_usd": 165958,
      "unidad": "PB D"
    }
  ]
}
```

### Borrador, tal como lo vería el asesor

> Hola, buen día! Soy Francisco, asesor comercial de DOMINIA.
> La PB B de Casona 3, 2 dormitorios con 2 baños, jardín de uso exclusivo y cochera, está disponible. La PB H no está a la venta; lo más parecido en 1 dormitorio es la PB D, también en planta baja, con jardín y cochera.
> Según cómo lo pienses pagar te conviene una cosa u otra —tenemos terminado para escriturar ya y en obra con cuotas—, así que decime: ¿lo veías al contado o con crédito, o te sirve más el plan en cuotas?
> Para verlas, ¿te queda mejor el martes 15 a las 10 o a las 17?
> Francisco, Asesor Comercial de DOMINIA

### Seguimiento preparado

| Cuándo | Aporte de valor | Texto |
|---|---|---|
| 48h | Dato útil no dicho: cochera incluida y expensas recién desde la posesión | Hola! Un dato que suma: las dos incluyen cochera y las expensas recién se pagan desde la posesión, durante el plan no corren. ¿Te sirve que coordinemos la visita esta semana? |
| 7 dias | Novedad verificable: avance de obra y estado de stock de esa tipología | Hola! Te cuento cómo viene la obra de Casona 3 y qué queda de planta baja con jardín, que es lo que mirabas. ¿Querés que te pase el detalle? |
| 21 dias | Pregunta que cierra el ciclo y da permiso a decir que no | Hola! Última consulta y no te molesto más: ¿seguís mirando o lo pausaste por ahora? |

## Verificación automática de reglas duras (tal como la corrió el front)

| | Regla | Detalle |
|---|---|---|
| ✅ V1 | Consultó el tarifario antes de responder | 3 llamada(s) |
| ✅ V2 | Lista única: unidades de un solo edificio y coherentes con la lista asignada | lista=casona_3_pozo; edificios propuestos=Casona 3 |
| ✅ V3 | Precios y disponibilidad idénticos al tarifario |  |
| ✅ V4 | Hasta 3 unidades propuestas | 2 unidad(es) |
| ✅ V5 | Todo monto en USD del borrador sale del tarifario de la lista asignada | 0 monto(s) |
| ✅ V6 | El borrador y el seguimiento no mencionan descuentos ni comisiones |  |
| ✅ V7 | El borrador no promete lo que no se puede cumplir ni mete urgencia artificial |  |
| ✅ V8 | Firma exacta del asesor | esperada: «Francisco, Asesor Comercial de DOMINIA» |
| ✅ V9 | Como máximo dos preguntas | 2 pregunta(s) |
| ✅ V10 | Menos de 120 palabras en WhatsApp o Instagram | 113 palabras · canal whatsapp |
| ✅ V11 | El asesor se presenta en la primera línea | primera línea: «Hola, buen día! Soy Francisco, asesor comercial de DOMINIA.» |
| ✅ V12 | Días de la semana coherentes con las fechas propuestas | 1 fecha(s) verificada(s) |
| ✅ V13 | Si la visita quedó acordada, el borrador lleva dirección y aviso de confirmación | la visita todavía no está acordada |
| ✅ V14 | Sin vocabulario que la ficha desmiente (el jardín es de uso exclusivo) |  |
| ✅ V15 | Si la consulta vino del botón de la web, el borrador pregunta cómo paga (T-28) | pregunta por la forma de pago |

## Consumo y costo

No aplica: corrió con la capacidad `sample` de la página, sin API.

## Revisión humana

- Revisó: sí, en el front
- Cambios al borrador (pegar el texto que se envió de verdad):
- ¿Se envió?:
- Respuesta del interesado:
- **¿Contestó?**:
- **¿Se agendó visita?**:
- **¿Se hizo la visita?**:
