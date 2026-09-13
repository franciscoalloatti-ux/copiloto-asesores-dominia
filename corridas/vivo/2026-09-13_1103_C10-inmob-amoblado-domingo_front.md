# Corrida en vivo · C10-inmob-amoblado-domingo · 13/09/2026 11:03

| Campo | Valor |
|---|---|
| Fecha de la corrida | 2026-09-13 11:03 (hora de Córdoba; el identificador `VIVO-202609131403` está en UTC) |
| Dónde corrió | Front del copiloto publicado, capacidad `sample`, a cuenta de la suscripción del responsable |
| Versión del contrato | v6 (iteración 9), **anterior a V15 y a la iteración 10** |
| Entrada | Consulta nueva, cargada por el responsable en el front; no tiene archivo en `entradas/` |
| Cómo se obtuvo | Documento `corridas_vivo/VIVO-202609131403` de la base de datos de la página |
| Resultado en el front | BLOQUEADA: corregir antes de enviar |
| Con los chequeos vigentes (13/9, reverificada sin llamar al modelo) | BLOQUEADA (V4, V11) |

## Entrada

```markdown
consulta_id: VIVO-202609131403
asesor: Francisco
canal: inmobiliaria
fecha: 2026-09-13

## Historial



## Consulta

fran querido como andas todo bien escucha pero no te jode esta hora ese éxito este mostrar un departamento en el domingo porque me acaban de avisar vino un chico, un jugador de fútbol de Buenos Aires y el único día que tiene para verlo el domingo tempranito quiero mostrarle el 2:03 dormitorios que tengas vente, quería entrar en el amoblado Tenés los códigos para que podamos verlo el domingo en la mañana tempranito
```

## Salida

```json
{
  "alertas_para_el_asesor": [
    "El domingo no está en las franjas habituales de visita (lunes a viernes 10 a 13 y 16 a 19; sábados 10 a 13): la excepción la decidís vos.",
    "El colega no aclaró qué domingo: el mensaje asume el domingo 20/9 a las 9. Si se refería a hoy mismo (13/9), corregilo antes de enviar.",
    "No dijo cómo paga su cliente: la lista se asignó por defecto a terminados y se nombró el otro camino sin precios ni lista.",
    "Comisiones y condiciones de colaboración entre inmobiliarias no están en la ficha: las respondés vos.",
    "Verificá acceso al edificio y a las unidades ese día y horario (llaves, códigos, seguridad y si hay alguien ocupando el 2º F)."
  ],
  "borrador_mensaje": "Todo bien por acá, gracias! Vení tranquilo: el domingo temprano lo vemos, 9 de la mañana me queda bien y abro yo, así tu cliente aprovecha el viaje.\nLe muestro el amoblado, el 2º F, que se entrega equipado por Interiores B.AP, y al lado el mismo departamento sin amueblar, más un 2 dormitorios de planta baja con jardín de uso exclusivo. Todos con cochera.\nTe adjunto la lista de terminados, que es lo que se escritura ya; si tu cliente necesita cuotas durante la obra decime y te paso la de Casona 3, que además tiene tipologías que en terminado no existen.\nPara llevarte lo justo, ¿sabés si lo ve para vivir o para renta, y cómo lo pensaba pagar?\nTe espero en Costanera de La Cañada 4140, Manantiales I; te confirmo el día anterior y te mando la ubicación.\nFrancisco, Asesor Comercial de DOMINIA",
  "camino_del_comprador": {
    "etapa": "listo_para_visita",
    "evidencia": "«el único día que tiene para verlo el domingo tempranito»"
  },
  "canal": "inmobiliaria",
  "consulta_id": "VIVO-202609131403",
  "estrategia": {
    "objetivo_del_mensaje": "Confirmar la visita del domingo temprano sin condicionarla, avisar qué unidades se muestran y qué lista va adjunta, y sacar el perfil del cliente final para preparar la recorrida.",
    "que_no_decir_todavia": [
      "Precios de las unidades en el cuerpo del mensaje: van en la lista adjunta",
      "Comisiones o condiciones de colaboración entre inmobiliarias: las responde el asesor",
      "Cualquier precio o dato de Casona 3",
      "Comparar el USD/m² del 2º F con el resto"
    ],
    "tecnicas": [
      {
        "codigo": "T-17",
        "como_se_aplica": "Se le contesta primero el «cómo andás» en tres palabras y se retoma su urgencia antes de cualquier dato."
      },
      {
        "codigo": "T-26",
        "como_se_aplica": "Tono entre colegas, información ordenada y lista adjunta; honorarios y condiciones los acuerda el asesor aparte."
      },
      {
        "codigo": "T-13",
        "como_se_aplica": "Se ofrece ver también el 3º D, la misma unidad sin equipar, por si al cliente le conviene más."
      },
      {
        "codigo": "T-24",
        "como_se_aplica": "Se cierran día, hora y dirección, con aviso de confirmación el día anterior."
      },
      {
        "codigo": "T-16",
        "como_se_aplica": "Se deja el orden de la recorrida (terminados, amenities, amoblado, unidades) para la visita, no para el mensaje."
      },
      {
        "codigo": "T-02",
        "como_se_aplica": "Una sola pregunta de calificación sobre uso y forma de pago del cliente final, sin condicionar la visita."
      }
    ]
  },
  "lista_asignada": {
    "lista": "casona_2_terminados",
    "motivo": "Escribe un colega y no aclaró cómo paga su cliente ni que busque pozo o cuotas; por defecto se le da la lista de terminados, y además pidió expresamente el amoblado, que es el 2º F de Casona 2."
  },
  "perfil": {
    "evidencia": "Solo se sabe que es «un jugador de fútbol de Buenos Aires»; el colega no dice uso ni forma de pago.",
    "tipo": "indefinido",
    "uso": "indefinido"
  },
  "proximo_paso": {
    "accion": "Confirmar la visita del domingo a primera hora con el colega y su cliente, y adjuntar la lista de Casona 2",
    "propuesta_de_visita": "Domingo 20/9 a las 9:00 en Costanera de La Cañada 4140, Manantiales I (horario propuesto por el colega; queda sujeto a que Francisco lo confirme)"
  },
  "resumen_consulta": "Un corredor colega pide mostrar el domingo bien temprano un 2 o 3 dormitorios y el departamento amoblado a un cliente suyo, jugador de fútbol de Buenos Aires que solo tiene ese día.",
  "revisar_antes_de_enviar": [
    "Adjuntar vos la lista vigente de Casona 2 (Lista N°5, 01/10/2025): el copiloto no manda archivos.",
    "Confirmar el horario del domingo contra tu agenda y contra la disponibilidad de ingreso al complejo.",
    "Ajustar el nombre del colega en el saludo si querés personalizarlo.",
    "Chequear que 2º F, 3º D y PB B sigan disponibles el día de la visita."
  ],
  "seguimiento": [
    {
      "aporte_de_valor": "Confirmación de día, hora y ubicación, más qué se va a ver",
      "cuando": "dia_anterior_a_la_visita",
      "texto": "Confirmado para mañana a las 9 en Costanera de La Cañada 4140, Manantiales I. Te mando la ubicación. Vemos el amoblado, un 3 dormitorios y un 2 dormitorios con jardín. Cualquier cambio avisame."
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
      "valor": "Urgente para ver: viaja desde Buenos Aires y solo tiene el domingo temprano"
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
      "estado": "inferido",
      "valor": "El cliente final del colega; no se sabe si decide con alguien más"
    },
    {
      "dato": "alternativas",
      "estado": "falta",
      "valor": null
    }
  ],
  "unidades_propuestas": [
    {
      "dato_clave": "3 dormitorios, 2 baños, 97,05 m² cubiertos, cochera; se entrega amoblado y equipado por Interiores B.AP",
      "edificio": "Casona 2",
      "por_que_esta": "Es el amoblado que el colega pidió ver; encaja con alguien de otra ciudad que no quiere amueblar nada.",
      "precio_lista_usd": 349725,
      "unidad": "2º F"
    },
    {
      "dato_clave": "3 dormitorios, 2 baños, misma unidad que el 2º F (97,05 m²) pero sin equipar, cochera incluida",
      "edificio": "Casona 2",
      "por_que_esta": "Es la alternativa directa al amoblado para comparar en la misma visita si prefiere traer sus muebles.",
      "precio_lista_usd": 286507,
      "unidad": "3º D"
    },
    {
      "dato_clave": "2 dormitorios, 2 baños, 77,08 m² cubiertos y 32,5 m² de jardín de uso exclusivo, cochera",
      "edificio": "Casona 2",
      "por_que_esta": "Cubre el 2 dormitorios que pidió, con el mejor jardín de uso exclusivo del stock terminado.",
      "precio_lista_usd": 219250,
      "unidad": "PB B"
    },
    {
      "dato_clave": "3 dormitorios, 2 baños, 93,35 m² cubiertos, cochera incluida",
      "edificio": "Casona 2",
      "por_que_esta": "Opción de 3 dormitorios en piso alto; queda como reserva si el 3º D no encaja.",
      "precio_lista_usd": 275271,
      "unidad": "2º C"
    }
  ]
}
```

### Borrador, tal como lo vería el asesor

> Todo bien por acá, gracias! Vení tranquilo: el domingo temprano lo vemos, 9 de la mañana me queda bien y abro yo, así tu cliente aprovecha el viaje.
> Le muestro el amoblado, el 2º F, que se entrega equipado por Interiores B.AP, y al lado el mismo departamento sin amueblar, más un 2 dormitorios de planta baja con jardín de uso exclusivo. Todos con cochera.
> Te adjunto la lista de terminados, que es lo que se escritura ya; si tu cliente necesita cuotas durante la obra decime y te paso la de Casona 3, que además tiene tipologías que en terminado no existen.
> Para llevarte lo justo, ¿sabés si lo ve para vivir o para renta, y cómo lo pensaba pagar?
> Te espero en Costanera de La Cañada 4140, Manantiales I; te confirmo el día anterior y te mando la ubicación.
> Francisco, Asesor Comercial de DOMINIA

### Seguimiento preparado

| Cuándo | Aporte de valor | Texto |
|---|---|---|
| dia_anterior_a_la_visita | Confirmación de día, hora y ubicación, más qué se va a ver | Confirmado para mañana a las 9 en Costanera de La Cañada 4140, Manantiales I. Te mando la ubicación. Vemos el amoblado, un 3 dormitorios y un 2 dormitorios con jardín. Cualquier cambio avisame. |

## Verificación automática de reglas duras (tal como la corrió el front)

| | Regla | Detalle |
|---|---|---|
| ✅ V1 | Consultó el tarifario antes de responder | 2 llamada(s) |
| ✅ V2 | Lista única: unidades de un solo edificio y coherentes con la lista asignada | lista=casona_2_terminados; edificios propuestos=Casona 2 |
| ✅ V3 | Precios y disponibilidad idénticos al tarifario |  |
| ❌ V4 | Hasta 3 unidades propuestas | 4 unidad(es) |
| ✅ V5 | Todo monto en USD del borrador sale del tarifario de la lista asignada | 0 monto(s) |
| ✅ V6 | El borrador y el seguimiento no mencionan descuentos ni comisiones |  |
| ✅ V7 | El borrador no promete lo que no se puede cumplir ni mete urgencia artificial |  |
| ✅ V8 | Firma exacta del asesor | esperada: «Francisco, Asesor Comercial de DOMINIA» |
| ✅ V9 | Como máximo dos preguntas | 1 pregunta(s) |
| ✅ V10 | Menos de 120 palabras en WhatsApp o Instagram | 146 palabras · canal inmobiliaria |
| ❌ V11 | El asesor se presenta en la primera línea | primera línea: «Todo bien por acá, gracias! Vení tranquilo: el domingo temprano lo vemos, 9 de l» |
| ✅ V12 | Días de la semana coherentes con las fechas propuestas | 1 fecha(s) verificada(s) |
| ✅ V13 | Si la visita quedó acordada, el borrador lleva dirección y aviso de confirmación | dirección y confirmación |
| ✅ V14 | Sin vocabulario que la ficha desmiente (el jardín es de uso exclusivo) |  |

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
