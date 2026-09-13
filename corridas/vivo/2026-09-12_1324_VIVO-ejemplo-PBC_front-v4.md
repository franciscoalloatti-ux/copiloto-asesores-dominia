# Corrida en vivo · VIVO-202609121624 · 12/09/2026 13:24

| Campo | Valor |
|---|---|
| Fecha de la corrida | 2026-09-12 13:24 (hora de Córdoba; el identificador está en UTC) |
| Dónde corrió | Front del copiloto (`visor/index.html` publicado), capacidad `sample`, a cuenta de la suscripción del responsable |
| Versión del contrato | v4 + playbook v2 (anterior a las iteraciones 6 a 8, publicadas a las 14:01) |
| Tarifario | `herramientas/tarifario_vigente.csv` embebido en la página |
| Cómo se obtuvo | Documento `corridas_vivo/VIVO-202609121624` de la base de datos de la página, leído el 13/9 |
| Resultado | aprobada para revisión |

> **La entrada es la consulta de ejemplo que trae el front**, no la de un interesado real. Esta corrida
> prueba que el front funciona de punta a punta (contrato → herramienta → ficha → chequeos); no es
> evidencia de uso con un cliente.

## Entrada

```markdown
consulta_id: VIVO-202609121624
asesor: Francisco
canal: whatsapp
fecha: 2026-09-12

## Historial



## Consulta

Hola! Me interesa PB C (2 Dorm · 2 Baños) de Casona III. Es para vivir con mi señora, hoy alquilamos. Gracias!
```

## Llamadas a la herramienta

La página registra la cantidad de llamadas en el chequeo V1 (dos), pero la base de datos no guardó sus
argumentos. Las tres unidades propuestas coinciden con el tarifario (V3).

## Salida

```json
{
  "alertas_para_el_asesor": [
    "No se sabe si califica a crédito hipotecario: si califica, el terminado (Casona 2) podría convenirle más (T-13). Definirlo con su respuesta sobre forma de pago antes de avanzar con Casona 3.",
    "No se mencionó precio en el mensaje (T-27): si lo pide, dar solo la cifra de PB C del tarifario.",
    "Confirmar disponibilidad de agenda para el sábado 19/9 a las 10 u 11."
  ],
  "borrador_mensaje": "Hola, buenas tardes! Soy Francisco, asesor comercial de DOMINIA. Casona de los Arcos es un complejo cerrado de tres torres en Manantiales I, Córdoba, y Casona 3 es la torre que lo completa.\nEl PB C está disponible: 2 dormitorios, 2 baños, jardín de uso exclusivo (lo mantiene el consorcio), cochera y entrega estimada en 2029, con plan de pagos en cuotas durante la obra.\nPara armarles el plan que mejor les sirva, ¿cómo pensaban pagarlo, con anticipo y cuotas o de contado? Y para que lo vean con tu señora, ¿les queda mejor el sábado 19 a las 10 o a las 11?\nFrancisco, Asesor Comercial de DOMINIA",
  "camino_del_comprador": {
    "etapa": "calificado",
    "evidencia": "«Me interesa PB C (2 Dorm · 2 Baños) de Casona III. Es para vivir con mi señora, hoy alquilamos»"
  },
  "canal": "whatsapp",
  "consulta_id": "VIVO-202609121624",
  "estrategia": {
    "objetivo_del_mensaje": "Confirmar que PB C está disponible, dar su diferencial y avanzar a la visita con los dos decisores, definiendo antes cómo piensa pagarlo.",
    "que_no_decir_todavia": [
      "El precio de PB C ni el anticipo o la cuota (van cuando lo pida o en la visita)",
      "Cualquier comparación con Casona 2 o con el terminado",
      "Fecha de entrega cerrada: solo «estimada 2029»",
      "Expensas, salvo que las pregunte",
      "Márgenes, descuentos o negociación"
    ],
    "tecnicas": [
      {
        "codigo": "T-27",
        "como_se_aplica": "Primer mensaje sin precio: se confirma disponibilidad, diferencial y forma de pago en términos generales (cuotas durante la obra)."
      },
      {
        "codigo": "T-28",
        "como_se_aplica": "La lista salió de la unidad elegida en la web, así que la primera pregunta es cómo pensaban pagarlo."
      },
      {
        "codigo": "T-17",
        "como_se_aplica": "Se retoma que es para vivir con su señora y que hoy alquilan antes de dar datos de la unidad."
      },
      {
        "codigo": "T-18",
        "como_se_aplica": "Se aclara de entrada que el jardín es de uso exclusivo mantenido por el consorcio y que la entrega es estimada 2029."
      },
      {
        "codigo": "T-15",
        "como_se_aplica": "Cierre con dos horarios concretos para el sábado 19/9."
      },
      {
        "codigo": "T-08",
        "como_se_aplica": "Se invita a la visita con su señora, que es codecisora."
      }
    ]
  },
  "lista_asignada": {
    "lista": "casona_3_pozo",
    "motivo": "Eligió expresamente una unidad de Casona 3 (PB C). La lista queda asignada por la unidad que pidió, no por su forma de pago: por eso la primera pregunta del borrador es cómo piensa pagarlo (T-28)."
  },
  "perfil": {
    "evidencia": "«Es para vivir con mi señora, hoy alquilamos»",
    "tipo": "indefinido",
    "uso": "vivienda_propia"
  },
  "proximo_paso": {
    "accion": "Proponer visita al complejo con su señora y definir la forma de pago para preparar el plan",
    "propuesta_de_visita": "Sábado 19/9/2026 a las 10 o a las 11"
  },
  "resumen_consulta": "Pide información por la unidad PB C (2 dorm, 2 baños) de Casona 3; es para vivir con su pareja, hoy alquilan.",
  "revisar_antes_de_enviar": [
    "Verificar que PB C siga disponible al momento de enviar",
    "Ajustar el saludo si el mensaje sale en otro momento del día",
    "Chequear el nombre del interesado para personalizar el saludo",
    "Confirmar dirección y punto de encuentro para la visita (Costanera de La Cañada 4140, Manantiales I)"
  ],
  "seis_datos": [
    {
      "dato": "uso",
      "estado": "conocido",
      "valor": "Vivienda propia para él y su pareja"
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
      "estado": "inferido",
      "valor": "Él y su señora: la nombra como parte del proyecto de mudanza"
    },
    {
      "dato": "alternativas",
      "estado": "inferido",
      "valor": "Seguir alquilando: «hoy alquilamos»"
    }
  ],
  "unidades_propuestas": [
    {
      "dato_clave": "2 dorm, 2 baños, 69,8 m² cubiertos, jardín de uso exclusivo 29,15 m², cochera, entrega estimada 2029; 40% anticipo + 40% en 30 cuotas + 20% contra entrega",
      "edificio": "Casona 3",
      "por_que_esta": "Es la unidad que pidió y está disponible; la planta baja con jardín y 2 baños encaja con una pareja que se muda de un alquiler",
      "precio_lista_usd": 247582,
      "unidad": "PB C"
    },
    {
      "dato_clave": "Misma tipología y superficie que PB C, jardín de uso exclusivo 29,25 m², cochera",
      "edificio": "Casona 3",
      "por_que_esta": "Alternativa idéntica en otra orientación, útil si en la visita la ubicación dentro de la planta no lo convence (no mencionarla todavía en el mensaje)",
      "precio_lista_usd": 247582,
      "unidad": "PB A"
    },
    {
      "dato_clave": "Misma planta que PB C pero en altura, sin jardín, con balcón de 7,6 m², cochera",
      "edificio": "Casona 3",
      "por_que_esta": "Opción en altura de la misma tipología, por si prefieren vista y no jardín",
      "precio_lista_usd": 250058,
      "unidad": "1º C"
    }
  ]
}
```

### Borrador, tal como lo vería el asesor

> Hola, buenas tardes! Soy Francisco, asesor comercial de DOMINIA. Casona de los Arcos es un complejo cerrado de tres torres en Manantiales I, Córdoba, y Casona 3 es la torre que lo completa.
> El PB C está disponible: 2 dormitorios, 2 baños, jardín de uso exclusivo (lo mantiene el consorcio), cochera y entrega estimada en 2029, con plan de pagos en cuotas durante la obra.
> Para armarles el plan que mejor les sirva, ¿cómo pensaban pagarlo, con anticipo y cuotas o de contado? Y para que lo vean con tu señora, ¿les queda mejor el sábado 19 a las 10 o a las 11?
> Francisco, Asesor Comercial de DOMINIA

## Verificación automática de reglas duras

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
| ✅ V10 | Menos de 120 palabras en WhatsApp o Instagram | 109 palabras · canal whatsapp |
| ✅ V11 | El asesor se presenta en la primera línea | primera línea: «Hola, buenas tardes! Soy Francisco, asesor comercial de DOMINIA. Casona de los A» |
| ✅ V12 | Días de la semana coherentes con las fechas propuestas | 1 fecha(s) verificada(s) |

## Consumo y costo

No aplica: corrió con la capacidad `sample` de la página, sin API. No hay conteo de tokens disponible.

## Revisión humana

- Revisó: sí, en el front
- ¿Se envió?: no (consulta de ejemplo)
