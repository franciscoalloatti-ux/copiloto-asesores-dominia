# Corrida en vivo · C03-inmob-mostrar-hoy · 13/09/2026 10:37

| Campo | Valor |
|---|---|
| Fecha de la corrida | 2026-09-13 10:37 (hora de Córdoba; el identificador `VIVO-202609131337` está en UTC) |
| Dónde corrió | Front del copiloto publicado, capacidad `sample`, a cuenta de la suscripción del responsable |
| Versión del contrato | **v5** (iteraciones 6 a 8) + playbook v3 + ficha con franjas de visita |
| Entrada | La misma consulta real de `entradas/consulta-03.md`, con la fecha cambiada a la del día |
| Cómo se obtuvo | Documento `corridas_vivo/VIVO-202609131337` de la base de datos de la página |
| Resultado en el front | aprobada para revisión |
| Con los chequeos vigentes (13/9, reverificada sin llamar al modelo) | aprobada para revisión |

## Entrada

```markdown
consulta_id: VIVO-202609131337
asesor: Francisco
canal: inmobiliaria
fecha: 2026-09-13

## Historial



## Consulta

hola wasooooooo
si quiero mostrar casonas hoy a las 12 30
```

## Salida

```json
{
  "alertas_para_el_asesor": [
    "La visita es HOY domingo 13/9 a las 12:30; los domingos no están en las franjas habituales (lun a vie 10-13 y 16-19, sábados 10-13). Si no podés, reprogramalo vos: el borrador no pone condiciones.",
    "El colega no dijo nada del cliente final: la lista de terminados va por defecto, no por su forma de pago.",
    "Comisiones y condiciones de colaboración no están en la ficha: si las pregunta, las respondés vos.",
    "Como la visita es el mismo día, la línea de confirmación se adaptó (no aplica 'te confirmo el día anterior')."
  ],
  "borrador_mensaje": "Hola! Francisco, de DOMINIA, por acá.\nDale, hoy 12:30 queda confirmado, te espero.\nTe adjunto la lista de Casona 2, la terminada, que es lo que se escritura ya; si tu cliente necesita cuotas durante la obra decime y te paso la de Casona 3, que además tiene tipologías que en terminado no existen.\nPara llevarte lo justo, ¿qué está buscando tu cliente: cantidad de dormitorios y si es para vivir o invertir?\nTe espero en Costanera de La Cañada 4140, Manantiales I; te mando la ubicación ahora y te confirmo apenas salgas.\nFrancisco, Asesor Comercial de DOMINIA",
  "camino_del_comprador": {
    "etapa": "listo_para_visita",
    "evidencia": "si quiero mostrar casonas hoy a las 12 30"
  },
  "canal": "inmobiliaria",
  "consulta_id": "VIVO-202609131337",
  "estrategia": {
    "objetivo_del_mensaje": "Confirmar la visita de hoy a las 12:30 sin condiciones, avisar que va adjunta la lista de terminados y pedir en paralelo el perfil del cliente final para preparar la recorrida.",
    "que_no_decir_todavia": [
      "Precios de Casona 3 ni comparación entre terminado y pozo",
      "Comisiones o condiciones de colaboración: las responde el asesor",
      "Cualquier fecha de entrega cerrada de Casona 3"
    ],
    "tecnicas": [
      {
        "codigo": "T-26",
        "como_se_aplica": "Tono entre colegas, información completa y ordenada: se adjunta la lista de Casona 2 para que pueda llevar a su cliente."
      },
      {
        "codigo": "T-13",
        "como_se_aplica": "Se le ofrece el otro camino (cuotas durante la obra, tipologías que en terminado no existen) por si le sirve más a su cliente, sin precios."
      },
      {
        "codigo": "T-24",
        "como_se_aplica": "Se cierra con dirección exacta y aviso de confirmación/ubicación."
      },
      {
        "codigo": "T-14",
        "como_se_aplica": "El mensaje termina con un próximo paso concreto: la visita confirmada de hoy 12:30."
      }
    ]
  },
  "lista_asignada": {
    "lista": "casona_2_terminados",
    "motivo": "Escribe un colega y no aclara que su cliente busque pozo, obra o cuotas: por regla de colegas, se le da por defecto la lista de terminados, nombrando el otro camino en una línea sin precios."
  },
  "perfil": {
    "evidencia": "El colega no dice nada del cliente final ni de su forma de pago",
    "tipo": "indefinido",
    "uso": "indefinido"
  },
  "proximo_paso": {
    "accion": "Confirmar la visita propuesta por el colega para hoy domingo 13/9 a las 12:30 en Costanera de La Cañada 4140",
    "propuesta_de_visita": "domingo 13/9/2026, 12:30 (propuesto por el colega, a confirmar contra agenda del asesor)"
  },
  "resumen_consulta": "Un colega escribe informalmente para mostrar Casona de los Arcos hoy domingo 13/9 a las 12:30, sin datos del cliente final ni forma de pago.",
  "revisar_antes_de_enviar": [
    "Adjuntar vos la lista de Casona 2 (Lista N°5, 01/10/2025): el copiloto no manda archivos.",
    "Verificar tu disponibilidad real para hoy 12:30 antes de enviar.",
    "Confirmar que las 8 unidades de Casona 2 sigan disponibles en el tarifario vigente.",
    "Mandar la ubicación por el mismo canal."
  ],
  "seguimiento": [
    {
      "aporte_de_valor": "Confirmación del encuentro con ubicación (la visita es hoy mismo: el toque va apenas confirmada, no el día anterior)",
      "cuando": "dia_anterior_a_la_visita",
      "texto": "Confirmado 12:30 en Costanera de La Cañada 4140, Manantiales I. Te mando la ubicación. Cualquier cambio avisame y lo acomodamos."
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
  "unidades_propuestas": []
}
```

### Borrador, tal como lo vería el asesor

> Hola! Francisco, de DOMINIA, por acá.
> Dale, hoy 12:30 queda confirmado, te espero.
> Te adjunto la lista de Casona 2, la terminada, que es lo que se escritura ya; si tu cliente necesita cuotas durante la obra decime y te paso la de Casona 3, que además tiene tipologías que en terminado no existen.
> Para llevarte lo justo, ¿qué está buscando tu cliente: cantidad de dormitorios y si es para vivir o invertir?
> Te espero en Costanera de La Cañada 4140, Manantiales I; te mando la ubicación ahora y te confirmo apenas salgas.
> Francisco, Asesor Comercial de DOMINIA

### Seguimiento preparado, si no contesta

| Cuándo | Aporte de valor | Texto |
|---|---|---|
| dia_anterior_a_la_visita | Confirmación del encuentro con ubicación (la visita es hoy mismo: el toque va apenas confirmada, no el día anterior) | Confirmado 12:30 en Costanera de La Cañada 4140, Manantiales I. Te mando la ubicación. Cualquier cambio avisame y lo acomodamos. |

## Verificación automática de reglas duras (tal como la corrió el front)

| | Regla | Detalle |
|---|---|---|
| ✅ V1 | Consultó el tarifario antes de responder | 2 llamada(s) |
| ✅ V2 | Lista única: unidades de un solo edificio y coherentes con la lista asignada | lista=casona_2_terminados; edificios propuestos=— |
| ✅ V3 | Precios y disponibilidad idénticos al tarifario |  |
| ✅ V4 | Hasta 3 unidades propuestas | 0 unidad(es) |
| ✅ V5 | Todo monto en USD del borrador sale del tarifario de la lista asignada | 0 monto(s) |
| ✅ V6 | El borrador no menciona descuentos ni comisiones |  |
| ✅ V7 | El borrador no promete lo que no se puede cumplir ni mete urgencia artificial |  |
| ✅ V8 | Firma exacta del asesor | esperada: «Francisco, Asesor Comercial de DOMINIA» |
| ✅ V9 | Como máximo dos preguntas | 1 pregunta(s) |
| ✅ V10 | Menos de 120 palabras en WhatsApp o Instagram | 98 palabras · canal inmobiliaria |
| ✅ V11 | El asesor se presenta en la primera línea | primera línea: «Hola! Francisco, de DOMINIA, por acá.» |
| ✅ V12 | Días de la semana coherentes con las fechas propuestas | 1 fecha(s) verificada(s) |
| ✅ V13 | Si hay visita, el borrador lleva dirección y aviso de confirmación | dirección y confirmación |
| ✅ V14 | Sin vocabulario que la ficha desmiente (el jardín es de uso exclusivo) |  |

## Reverificación del 13/9 (sin volver a llamar al modelo)

- **Aprobada** con los chequeos corregidos del 13/9: igual resultado que en el front (14 de 14).

## Consumo y costo

No aplica: corrió con la capacidad `sample` de la página, sin API.

## Revisión humana

- Revisó: sí, en el front
- ¿Se envió?: no
- **¿Contestó?**:
- **¿Se agendó visita?**:
- **¿Se hizo la visita?**:
