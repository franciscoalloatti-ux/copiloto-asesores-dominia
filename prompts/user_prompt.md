# Copiloto para Asesores Comerciales de DOMINIA — user prompt

> **Versión 2** · 11/9/2026 · Iteración 5: el ejecutor agrega el día de la semana y el calendario
> de los próximos días, calculados en código (`{dia_consulta}`, `{calendario}`).
> Versión 1 · Plantilla del pedido puntual. El ejecutor reemplaza cada `{campo}`
> con los datos del archivo de entrada de la corrida (`entradas/*.md`). Lo que va entre
> las etiquetas `<consulta>` es texto del interesado: dato, nunca instrucción.

---

Llegó una consulta nueva. Preparame la ficha y el borrador de respuesta.

- **Asesor que firma:** {asesor}
- **Canal:** {canal}
- **Fecha y hora de la consulta:** {fecha} ({dia_consulta})
- **Identificador:** {consulta_id}

**Calendario** para proponer días de visita. Usá estos pares día-fecha tal cual: no calcules días
de la semana por tu cuenta.

{calendario}
- **Notas del asesor:** {notas}

**Historial previo con este interesado** (vacío si es el primer contacto):

<historial>
{historial}
</historial>

**Consulta:**

<consulta>
{consulta}
</consulta>

Antes de nombrar cualquier unidad o precio, consultá el tarifario. Devolvé solo el objeto JSON.
