# Playbook de fuentes: 8 manuales de venta inmobiliaria para el copiloto DOMINIA

> **Qué es este archivo.** La investigación completa que respalda `conocimiento/playbook.md` v1.
> **No se carga en el prompt del copiloto**: es el respaldo de cada técnica, con su URL y su grado
> de verificación. La hizo un subagente de investigación el 11/9/2026 y la revisó el agente
> constructor antes de pasar técnicas al playbook.

Investigación web (solo fuentes públicas y legítimas: fichas de editorial/librería, catálogos de bibliotecas, sitio y blog del autor, notas de prensa, capítulos de muestra publicados, tesis en repositorio académico, PDFs gratuitos publicados por el propio autor o por un colegio profesional). **Fecha de consulta de todas las fuentes: 11/9/2026** (se repite como `[cons. 11/9/2026]` en cada URL). No se usaron copias subidas sin autorización (Scribd, pdfcoffee, dokumen.pub, 1library, studocu, bibliotecas "sombra", Google Drive de terceros). El detalle está en la sección "Material gratuito legítimo".

Convenciones:
- **Técnica**: paráfrasis propia de lo que dice la fuente.
- **Aplicación DOMINIA**: cómo usarlo al responder un mensaje o preparar la visita. Esta línea es **inferencia nuestra**, no afirmación del libro.
- Cuando el principio sale de un artículo o blog del autor y no del texto del libro, se aclara con **[autor, no libro]**. Cuando sale solo del índice, con **[solo índice]**.

## Tabla resumen

| # | Título tal como lo pasó el usuario | Obra real | Estado | Confianza |
|---|---|---|---|---|
| 1 | 📓 La "Biblia" del Real Estate (Estructura y Escala) | Candidata: *The Millionaire Real Estate Agent* (Keller, Jenks, Papasan) | **No identificado** (parece un cuaderno de NotebookLM) | Media-baja para el candidato |
| 2 | 📈 Marca Personal y Cierre de Alto Impacto | Candidatas: Serhant (*Sell It Like Serhant* / *Brand It Like Serhant*) o Pallordet (*Agente Inmobiliario Exitoso*) | **No identificado** | Baja |
| 3 | El cierre de la venta inmobiliaria | Miguel Villarroya Martín (Finis Terrae, 2016) | Identificado | Alta |
| 4 | Everybody Wins de Dave Liniger | Phil Harkins y Keith Hollihan (Wiley, 2004/05); Liniger escribe **solo el prólogo** | Identificado (con la autoría corregida) | Alta |
| 5 | Comunicar para vender | Massimo Forte (Sabedoria Alternativa, Portugal, 2017; en portugués) | Probable | Media-alta |
| 6 | El camino del Real Estate Argentino | Diego F. Migliorisi, *El camino del real estate: Argentina 1956-2025* (autoedición, 2025, e-book gratuito, ISBN 978-631-01-0422-5) | Identificado; texto leído | Alta |
| 7 | Marketing para Inmobiliarios: Corredores y Tasadores | Gerardo Woscoboinik (Lectorum-Ugerman 2010; 2.ª ed. Ugerman 2021/22) | Identificado | Alta |
| 8 | Fideicomisos al costo | Damián Tabakman (dir.) y otros (Bienes Raíces Ediciones, 2011) | Identificado | Alta |

---

## 1. 📓 La "Biblia" del Real Estate (Estructura y Escala)

**Ficha**
- Estado: **no identificado.** El emoji y el subtítulo entre paréntesis indican que es el nombre de un cuaderno de NotebookLM, no el título de un libro. No se sabe qué fuentes cargó el usuario en ese cuaderno.
- **Candidato principal (confianza media-baja, ~50%)**: *The Millionaire Real Estate Agent* (MREA), de Gary Keller con Dave Jenks y Jay Papasan. McGraw-Hill, 2004, ISBN 9780071444040. Edición en castellano: *El Agente de Bienes Raíces Millonario*, Bard Press, 2025, ISBN 9781959472278 / 1959472283. Por qué lo creemos: el blog argentino DeInmobiliarios lo llama literalmente "la biblia" del real estate, y el libro se organiza en cuatro modelos (económico, de generación de prospectos, de presupuesto y organizacional), lo que coincide con "Estructura y Escala".
  - https://www.deinmobiliarios.com/blog/que-libros-debe-leer-un-inmobiliario [cons. 11/9/2026]
  - https://www.casadellibro.com/libro-the-millionaire-real-estate-agent/9780071444040/11208826 [cons. 11/9/2026]
  - https://books.google.com.ar/books/about/El_Agente_de_Bienes_Ra%C3%ADces_Millonario.html?id=vk9rEQAAQBAJ [cons. 11/9/2026]
- **Candidato alternativo (confianza baja)**: *La Biblia del Real Estate: Lenguaje Millonario*, de Armando y Jesús Cruz (autoedición en Amazon). El título coincide, pero trata de mentalidad de inversor e inversión inmobiliaria en EE.UU., no de venta ni de estructura comercial. https://us.amazon.com/Biblia-del-Real-Estate-Millonario/dp/B0H6KX27R9 [cons. 11/9/2026]

**Principios del candidato MREA.** Valen para MREA, **no** para el cuaderno del usuario. Hay que confirmar con él antes de citarlos como "la Biblia".

| Técnica | Aplicación DOMINIA | Fuente |
|---|---|---|
| Generar prospectos es la actividad principal del agente. Todo lo demás es secundario. | Ninguna consulta queda sin respuesta: cada mensaje que entra es un lead que costó conseguir. | https://outfront.kw.com/training/back-to-business-basics-economic-model/ (KW Outfront, 15/1/2020, cita MREA pp. 129-132) [cons. 11/9/2026] |
| Modelo económico: la cadena es leads, luego citas, luego contratos, luego cierres. Hay que medir la tasa de conversión de cada tramo. | El copiloto mide su éxito en consultas convertidas en visitas agendadas, no en mensajes enviados. | misma URL [cons. 11/9/2026] |
| Precalificar motivación y urgencia antes de dar la cita. | Antes de ofrecer horario de visita, averiguar para qué busca (vivienda o inversión), cuándo, y si el plan en obra le sirve. | misma URL [cons. 11/9/2026] |
| Base de contactos dividida en "conocidos" y "no conocidos", con secuencias de contacto sistemático (8x8 para contactos nuevos, 33 toques al año para la base). | El interesado que no agenda visita entra en una secuencia de seguimiento con aportes de valor (avance de obra, cambios del plan), no en el olvido. | https://www.easyagentpro.com/blog/millionaire-real-estate-agent-book-review-cliffnotes-part-1/ (reseña, ene-2015) [cons. 11/9/2026]; https://loriballen.com/the-mrea-models-the-millionaire-real-estate-agent/ [cons. 11/9/2026] |
| Apalancamiento = quién lo hace, cómo lo hace y con qué lo hace (personas, sistemas, herramientas). | El copiloto es la parte de "sistemas y herramientas": borradores de respuesta para que el asesor se concentre en la visita. | https://www.easyagentpro.com/blog/millionaire-real-estate-agent-book-review-cliffnotes-part-1/ [cons. 11/9/2026] |
| Modelo organizacional: se escala sumando roles de apoyo (administrativo, atención de leads, asistente de visitas). | Separar quién responde el primer mensaje de quién hace la visita, con un traspaso documentado. | https://loriballen.com/the-mrea-models-the-millionaire-real-estate-agent/ [cons. 11/9/2026] |

**Qué no se pudo verificar**
- Qué fuentes contiene el cuaderno "La Biblia del Real Estate (Estructura y Escala)". Puede ser MREA, otro libro o una mezcla.
- El texto de MREA no se consultó directamente. Los principios salen de material de Keller Williams (Outfront) y de reseñas de terceros. Las cifras del 8x8 y los 33 toques vienen de reseñas.
- La traducción al castellano aparece en Scribd: **solo en copias no autorizadas; no usado**. No se encontró una muestra gratuita oficial.

---

## 2. 📈 Marca Personal y Cierre de Alto Impacto

**Ficha**
- Estado: **no identificado.** No existe un libro con ese título ni con esa combinación de palabras. Es casi seguro un nombre de cuaderno.
- Candidatos, todos con **confianza baja**:
  - Ryan Serhant, *Sell It Like Serhant* (2018; venta y seguimiento) y *Brand It Like Serhant* (Hachette, 2024, ISBN 9780306923128; marca personal en tres fases: identidad, contenido constante y difusión de logros). https://www.hachettebookgroup.com/titles/ryan-serhant/brand-it-like-serhant/9780306923142/ [cons. 11/9/2026]; https://www.goodreads.com/book/show/38901678-sell-it-like-serhant [cons. 11/9/2026]
  - Guillermo Santiago Pallordet (martillero y corredor, egresado de la UNL), *Agente Inmobiliario Exitoso: Guía Completa para Convertirte en el Mejor Vendedor* (Kindle). Según su ficha trata mentalidad, marca personal, captación y cierre. https://www.amazon.com/Agente-Inmobiliario-Exitoso-Convertirte-Profesional-ebook/dp/B0DK22TT6K [cons. 11/9/2026; la página devolvió error, datos tomados del resultado de búsqueda]

**Principios: ninguno.** No se atribuye ninguna técnica a este título hasta que el usuario diga qué fuentes cargó en el cuaderno.

**Qué no se pudo verificar**
- La obra o las obras reales.
- En el caso de Serhant hay contradicciones entre resúmenes de terceros sobre sus marcos (por ejemplo, qué significan "las 3 F"). Hay dos fechas de edición de *Brand It Like Serhant* (feb-2024 y abr-2024). Por eso no se usaron.

---

## 3. "El cierre de la venta inmobiliaria"

**Ficha**
- Título exacto: *El cierre de la venta inmobiliaria: La venta personal inmobiliaria*.
- Autor: Miguel (José) Villarroya Martín. Es arquitecto técnico, agente inmobiliario y formador en España, y adapta el método SPIN Selling de Neil Rackham al sector inmobiliario español.
- Editorial: Finis Terrae Ediciones, 2016. 234 pp. ISBN papel 9788416896127; ISBN e-book 9788416896585 (Google Books lo fecha en 2017).
- Ediciones posteriores: *El cierre eficaz de la venta inmobiliaria*, 2.ª ed. corregida y aumentada, Punto Rojo Libros, 2023, 364 pp., ISBN 9788419238450. Hay una 3.ª edición que no se revisó.
- Estado: **identificado**, confianza **alta**. Contexto: España. Según Google Books, el libro sigue lo exigido por el Certificado de Profesionalidad español.
- Fuentes de ficha: https://latam.casadellibro.com/libro-el-cierre-de-la-venta-inmobiliaria/9788416896127/6389978 [cons. 11/9/2026]; https://books.google.com.ar/books?id=WM6vDgAAQBAJ [cons. 11/9/2026]; https://www.casadellibro.com/libro-el-cierre-eficaz-de-la-venta-inmobiliaria-2-ed-corregida-y-aumentada-2023/9788419238450/13623345 [cons. 11/9/2026]

**Principios**

| Técnica | Aplicación DOMINIA | Fuente |
|---|---|---|
| Hay dos caminos al cierre. El clásico dispara varias técnicas después de presentar la oferta. El de Rackham, que el autor recomienda, usa un único cierre como consecuencia natural de haber resuelto todas las objeciones y resumido los factores de decisión clave. | Antes de proponer la visita o la reserva, contestar todas las dudas planteadas y resumir en una línea lo que el interesado dijo que valora ("ubicación + plan en cuotas + 2 dormitorios"). | https://www.inmonews.es/las-dos-vias-al-cierre-de-la-venta-personal-inmobiliaria/ (artículo del autor basado en el libro) [cons. 11/9/2026] |
| Crítica al "cierre mágico": las fórmulas verbales memorizadas y la presión funcionan en ventas chicas, pero son peligrosas en ventas grandes como un inmueble. | No usar frases de cierre enlatadas ni ultimátums ("últimas 2 unidades, respondeme hoy") en WhatsApp. | https://www.inmonews.es/el-cierre-magico-de-la-venta/ (el autor dice que es extracto del libro) [cons. 11/9/2026] |
| En la venta personal, que el comprador acepte un paso es un **avance**, un compromiso concreto. En venta grande el cierre llega después de varias entrevistas. | La meta de la conversación escrita no es vender el departamento. Es obtener un avance: la visita agendada con día y hora. | https://www.inmonews.es/las-dos-vias-al-cierre-de-la-venta-personal-inmobiliaria/ [cons. 11/9/2026] |
| Catálogo de técnicas: condicional, de prueba o anticipado, indirecto, supuesto, resumen de ventajas. El autor las presenta con cautela y ubica al cierre de Rackham como el más seguro. | Si hay que proponer algo, preferir un cierre condicional suave ("si el plan de pagos te cierra, ¿vemos la unidad el jueves o el sábado?") antes que un cierre supuesto. | https://books.google.com.ar/books?id=WM6vDgAAQBAJ [cons. 11/9/2026]; https://ventasgrandes.com/2024/05/20/el-cierre-eficaz-de-la-venta-inmobiliaria/ [cons. 11/9/2026] |
| El vendedor tiene "miedo al cierre" y debe aprender a leer las señales de compra del cliente y las de huida. | Tomar como señal de compra que pregunte por plan de pago, fecha de posesión o cochera, y proponer visita. Si el interesado se enfría, bajar la intensidad: no insistir. | https://ventasgrandes.com/2024/05/20/el-cierre-eficaz-de-la-venta-inmobiliaria/ [cons. 11/9/2026] |
| Concertar y confirmar la entrevista. Al concertar se fija hora, lugar, objetivo y modalidad, y se avisa que habrá una confirmación previa. Al confirmar (por teléfono o mensaje) hay tres salidas: confirma, reprograma con un motivo creíble, o se abandona si las excusas se repiten. | Plantilla de agenda: día, hora, dirección con ubicación y qué se va a ver. Aviso de "te confirmo el día anterior". Mensaje de confirmación el día previo. Una sola reprogramación antes de pasar a seguimiento largo. | https://www.inmonews.es/concertacion-de-entrevistas-de-venta-inmobiliarias/ (11/4/2024) **[autor, no libro]** [cons. 11/9/2026] |

**Qué no se pudo verificar**
- El índice completo y el texto del libro. Los principios salen de la descripción editorial y de artículos del autor.
- Si "concertación y confirmación" figura en *este* libro o en otro del mismo autor sobre venta personal.
- Hay un visor en FlipHTML5 con 14 páginas del libro (https://fliphtml5.com/lner/smap/basic). No se pudo comprobar quién lo subió (la página devolvió 403), así que **no se usó**. Google Books tiene la ficha, pero la vista previa no se pudo leer. Punto Rojo no ofrece fragmento gratuito.

---

## 4. "Everybody Wins" de Dave Liniger (fundador de RE/MAX)

**Ficha**
- Título exacto: *Everybody Wins: The Story and Lessons Behind RE/MAX*.
- **Autores: Phil Harkins y Keith Hollihan.** Dave Liniger, cofundador de RE/MAX, **escribe solo el prólogo**. La atribución del usuario es inexacta.
- Editorial: John Wiley & Sons. Publicado en diciembre de 2004, con copyright 2005 de Linkage, Inc. ISBN tapa dura 0-471-71024-5 (9780471710240); Google Books registra 9780471719205. 304 pp. En inglés, sin edición en castellano verificada.
- Estado: **identificado**, confianza **alta**. Es un libro de estrategia, cultura y liderazgo organizacional, **no un manual de técnica de venta**.
- Fuentes: https://books.google.com.ar/books/about/Everybody_Wins.html?id=JvBmOAAqeN8C [cons. 11/9/2026]; https://www.goodreads.com/en/book/show/925513.Everybody_Wins [cons. 11/9/2026]. Muestra de lectura publicada por la tienda e-bookshelf, con prólogo y prefacio (30 pp.): https://content.e-bookshelf.de/media/reading/L-584694-5c60476270.pdf [cons. 11/9/2026]
- Cita (prefacio, muestra): "the agent's success is ultimately predicated on the home buyer's satisfaction".

**Principios** (todos del prólogo y el prefacio de la muestra, salvo que se indique otra cosa)

| Técnica | Aplicación DOMINIA | Fuente |
|---|---|---|
| Principio "everybody wins": ganan el cliente, el agente, los dueños y los empleados. El éxito del agente se apoya en la satisfacción del comprador. | Contestar para que el interesado quede bien atendido aunque hoy no compre. Nada de respuestas que "ganen" la conversación a costa de la confianza. | muestra e-bookshelf (prefacio) [cons. 11/9/2026] |
| La calidad y el profesionalismo se demuestran en actos pequeños, no en gestos grandes. Todas las descripciones de puesto terminan con una cláusula abierta de "otras tareas": en esa cultura, cualquiera hace lo que haga falta. | Los detalles son parte de la venta: confirmar la visita, mandar la ubicación, llegar antes, responder lo que se prometió responder. | muestra e-bookshelf (prefacio) [cons. 11/9/2026] |
| Foco implacable en la marca como motor de crecimiento. "Un solo leño hace un mal fuego": la marca común potencia a todos. | Tono, datos y promesas idénticos en WhatsApp, Instagram, portales y con inmobiliarias colegas. La marca DOMINIA pesa más que el estilo de cada asesor. | muestra e-bookshelf (prefacio) + índice (cap. 4) en Google Books [cons. 11/9/2026] |
| Pocas métricas "top-line", simples y claras, compartidas como consigna de todos. Demasiadas métricas dispersan. | Tres números para el equipo comercial: consultas respondidas, visitas agendadas y visitas realizadas. | muestra e-bookshelf (prefacio) [cons. 11/9/2026] |
| Cultura de aprendizaje y entrenamiento continuo: el desarrollo de las personas es condición de calidad y de crecimiento. | Registrar las objeciones y preguntas frecuentes que el copiloto detecta para alimentar la capacitación del equipo. | muestra e-bookshelf (prefacio) [cons. 11/9/2026] |
| Libertad del agente para promocionarse y construir su negocio, con el soporte de la red. | Cada asesor puede firmar con su nombre y construir su marca personal dentro del marco de la marca DOMINIA. | muestra e-bookshelf (prefacio) [cons. 11/9/2026] |

**Qué no se pudo verificar**
- El contenido de los capítulos 1 a 8 (solo se vieron los títulos del índice y la muestra de prólogo y prefacio).
- Técnicas de venta al comprador: el libro no parece tenerlas.

---

## 5. "Comunicar para vender"

**Ficha**
- Obra más probable: *Comunicar para Vender*, de **Massimo Forte**. Es italiano, radicado en Lisboa, formador inmobiliario, practitioner en PNL y profesor invitado en INDEG-ISCTE.
- Editorial: Sabedoria Alternativa (Portugal). 1.ª ed. abril de 2017 según Goodreads, 312 pp. 5.ª edición con ISBN 978-989-99316-7-1. **Idioma: portugués.** No se encontró edición en castellano; del mismo autor sí hay en castellano *Atraer para vender*.
- Estructura: 4 partes. Las fuentes discrepan entre 15 y 16 capítulos. Temas: autoconocimiento, conocer al cliente y comunicar para vender, aplicando PNL a la mediación inmobiliaria.
- Estado: **probable**, confianza **media-alta**. Es el único libro con ese título exacto ligado al rubro inmobiliario. No se encontró otra obra en castellano con ese título.
- Fuentes: https://massimoforte.com/produto/livro-comunicar-para-vender/ [cons. 11/9/2026]; https://www.goodreads.com/book/show/55779799-comunicar-para-vender [cons. 11/9/2026]; https://www.imovirtual.com/noticias/novidades/comunicar-para-vender-massimo-forte-lanca-novo-livro/ [cons. 11/9/2026]; https://massimoforte.com/sobre/ [cons. 11/9/2026]

**Principios**

| Técnica | Aplicación DOMINIA | Fuente |
|---|---|---|
| La venta inmobiliaria es un negocio "de personas para personas". Para comunicar hay que conocerse, empatizar con el cliente y atraerlo, no perseguirlo. | Responder a la persona antes que a la consulta: nombrarla, retomar lo que escribió y recién después dar el dato. | https://massimoforte.com/produto/livro-comunicar-para-vender/ (descripción del libro) [cons. 11/9/2026] |
| Congruencia entre el mensaje verbal y el no verbal. | Por escrito, el tono tiene que coincidir con lo que se promete (profesional y cálido, sin exageraciones). En la visita, la conducta del asesor tiene que sostener lo que dijo el chat. | misma URL (temas del libro) [cons. 11/9/2026] |
| Precalificación motivacional (qué busca y por qué; técnica de "pasado y futuro": qué le gustaba de su casa anterior y cómo sería la ideal) y financiera (cuánto y cómo puede pagar). Tiene que ser conversación, no interrogatorio. Sin conocer el "mapa del mundo" del cliente no se lo puede satisfacer. | Hacer 1 o 2 preguntas abiertas por mensaje, no un formulario. Por ejemplo: "¿Qué es lo que más te importa del próximo depto?" y después "¿Te sirve un plan en cuotas durante la obra?". | https://massimoforte.com/blog/comunicar-para-vender-contributo-do-vitor-neves/ (post de 17/5/2017 del invitado Vítor Neves en el blog del autor, bajo el título del libro) **[autor, no libro]** [cons. 11/9/2026] |
| Negociar (precio, condiciones) en el primer contacto, por teléfono o en la primera visita, pone al vendedor en desventaja, porque todavía no hay rapport ni confianza. | No negociar descuentos ni condiciones por WhatsApp en el primer intercambio. Ante "¿cuál es el mejor precio?", responder con el plan vigente y proponer verse. | https://massimoforte.com/blog/as-chaves-da-negociacao-imobiliaria/ (1/11/2017) **[autor, no libro]** [cons. 11/9/2026] |
| Usar guiones ensayados para guiar al interesado hacia un compromiso y precalificar cuatro factores: urgencia, deseo, necesidad y capacidad financiera. Guiar con competencia en vez de dejarse llevar. | El copiloto propone el siguiente paso en cada respuesta (una pregunta o un horario), para que la conversación no quede en manos del interesado. | https://massimoforte.com/blog/quer-guiar-ou-ser-guiado/ (21/4/2021) **[autor, no libro]** [cons. 11/9/2026] |
| Clasificar interesados en calientes (listos para comprar), tibios (interés real sin urgencia) y fríos (curiosos). "Hacer seguimiento" a un contacto no es lo mismo que "acompañar" a un cliente comprometido. | Etiquetar cada conversación en caliente, tibio o frío. Los calientes van a agenda de visita esta semana; los fríos, a seguimiento periódico. | https://massimoforte.com/blog/cliente-comprador-ou-interessado/ (1/11/2016) **[autor, no libro]** [cons. 11/9/2026] |
| La preparación lo es todo: conocer la propiedad a fondo (historia, entorno, defectos), llegar antes, prepararla y observar las señales del comprador durante la visita. | Antes de cada visita, ficha de la unidad (m², orientación, avance de obra, plan de pago vigente) y respuesta preparada para las objeciones previsibles. | https://massimoforte.com/blog/a-preparacao-e-tudo/ (28/7/2021) **[autor, no libro]** [cons. 11/9/2026] |
| Comunicación persuasiva pero sincera: la descripción no puede engañar. Informar las faltas (el ejemplo del autor es "no tiene ascensor") atrae al cliente correcto y respeta su tiempo. Fotos de calidad, recorrido virtual y descripción creativa según el público. | Decir de entrada lo que la unidad no tiene o lo que falta definir. Mandar material visual de calidad. | https://massimoforte.com/blog/quais-melhores-estrategias-para-atrair-e-fidelizar-clientes-compradores/ (9/11/2022) **[autor, no libro]** [cons. 11/9/2026] |

**Qué no se pudo verificar**
- Que el usuario se refiera a este libro. Al estar en portugués hay que confirmarlo.
- El texto del libro: salvo las dos primeras filas, los principios vienen del blog del autor o de un invitado.
- El número exacto de capítulos (15 o 16) y el año de la 5.ª edición: el sitio del autor dice 2018 y Imovirtual fecha el lanzamiento en 2023.
- No se encontró muestra gratuita de *Comunicar para Vender*. El autor ofrece gratis 20 páginas de **otro** libro suyo (*O Poder da Prospeção*), pero solo con registro: no se usó, porque registrarse implica crear una cuenta con datos personales.

---

## 6. "El camino del Real Estate Argentino"

**Ficha**
- Título exacto (página de créditos): *El camino del real estate: Argentina 1956-2025*. El sitio de LRV Latam lo presenta como "El Camino del Real Estate Argentino 2025".
- Autor: **Diego Fernando Migliorisi**, abogado y corredor inmobiliario (CABA). Algunas notas de prensa escriben "Migliorski" por error.
- Edición: 1.ª ed. compendiada, Ciudad Autónoma de Buenos Aires, edición del autor, 2025. Libro digital (descarga y online), 109 pp. **ISBN 978-631-01-0422-5**. CDD 330.82.
- Capítulos:
  1. Nuestra historia. La cultura del esfuerzo
  2. Las 16 crisis del mercado
  3. Auges y recuperaciones del mercado
  4. Del Cárdex a la Revolución Tecnológica
  5. El camino al éxito de la profesión, empresas de servicios o empresas tecnológicas
  6. El valor de la palabra
  7. Defensa de la propiedad privada
  8. El camino del real estate en la Argentina
- Estado: **identificado**, confianza **alta**. **Texto leído**: el autor lo publica gratis en PDF desde la página del libro, y el archivo trae su propia página de créditos con ISBN. Es sobre todo historia y opinión sectorial; los capítulos 5 y 6 sí traen principios comerciales.
- Fuentes: PDF oficial https://lrvlatam.com/wp-content/uploads/2025/08/el-camino-del-real-estate-Por-Diego-MIgliorisi.pdf (enlazado como "Descargar e-book" desde https://lrvlatam.com/el-camino-del-real-estate) [cons. 11/9/2026]; https://diegomigliorisi.com/el-camino-del-real-estate-en-argentina-2025/ [cons. 11/9/2026]
- Cita (cap. 6): "no se trata solo de vender e irse".

**Principios** (citamos el PDF oficial como "PDF" y damos el capítulo)

| Técnica | Aplicación DOMINIA | Fuente |
|---|---|---|
| Imparcialidad y verdad: el asesor transmite una realidad objetiva, con información clara, sobre el inmueble y sobre su contexto actual y futuro. No oculta información relevante y le muestra al cliente todo lo que necesita para decidir con libertad. El ejemplo del autor: avisarle al comprador de un riesgo de inundación que el dueño minimizaba. | Si una unidad tiene un contra (orientación, vista que puede taparse, plazo de obra), decirlo antes de que lo descubra el interesado. | PDF, cap. 6 "El valor de la palabra" [cons. 11/9/2026] |
| No adornar las respuestas para convencer si el propio asesor no está convencido. Acompañar decisiones que muchas veces comprometen los ahorros de toda una vida. | El copiloto no redacta respuestas "vendedoras" sobre dudas que no tienen respuesta firme. Prefiere "lo confirmo con obra y te aviso". | PDF, cap. 6 [cons. 11/9/2026] |
| Preguntas clave de asesoramiento: para qué compra, qué potencial de revalorización hay, si puede perder luz por construcciones futuras, si la situación jurídica, notarial y arquitectónica está en orden, **qué garantías hay si compra en pozo y cuáles son los riesgos y beneficios**. | El copiloto tiene que tener preparada la respuesta validada de DOMINIA a "¿qué garantías tengo si compro en pozo?", porque el autor la pone entre las preguntas centrales de cualquier comprador. | PDF, cap. 6 [cons. 11/9/2026] |
| Chequear la información dos y tres veces aunque venga de fuentes confiables, porque hay falsificaciones de documentos, imágenes y voces. Discreción y privacidad en las operaciones. | No difundir datos de compradores ni de operaciones cerradas en redes. Verificar la identidad y los datos de pago por canales oficiales, nunca solo por un mensaje. | PDF, cap. 6 [cons. 11/9/2026] |
| El primer contacto llega desde lo digital (portales, buscadores, redes, mensajería). En redes: visibilidad, información de valor con fundamento técnico y jurídico, y avisos que vayan al punto y conecten emocionalmente en los primeros segundos. | La primera respuesta es la "primera impresión": clara, concreta y con un dato útil en la primera línea. | PDF, cap. 5 [cons. 11/9/2026] |
| Autenticidad frente a guiones clonados: si todos usan el mismo léxico, el público se satura. Todo lo que se publica queda registrado para siempre, así que prudencia antes que impulso. | Plantillas del copiloto con variación y voz propia, sin frases de manual. Nunca publicar ni escribir algo que no se sostendría dentro de un año. | PDF, cap. 5 [cons. 11/9/2026] |
| La mensajería (SMS y luego WhatsApp) sirve para coordinar horarios, confirmar reuniones y mandar fotos, videos y ubicaciones en tiempo real. | Usar WhatsApp para lo que el autor describe: coordinar y confirmar la visita y mandar ubicación y material visual. | PDF, cap. 4 [cons. 11/9/2026] |
| Lección histórica: con el Rodrigazo (1975) los boletos con precios fijos en pesos se volvieron impagables para unos, y las constructoras que vendieron en cuotas fijas en pesos no pudieron cubrir los costos, con obras que quedaron sin terminar. En otra etapa, la suba del costo de construcción hizo que el pozo compitiera directamente con el terminado. | Sirve para explicar sin dramatizar por qué el precio está en dólares o ajusta por CAC. Y para no apoyar todo el argumento en "el pozo es más barato" cuando no lo es. | PDF, cap. 2 y cap. 3 [cons. 11/9/2026] |

**Qué no se pudo verificar**
- Qué quiere decir la "compendiada" de la 1.ª edición: puede existir una versión extendida.
- Si es el 10.º o el 11.º libro del autor: las fuentes se contradicen.
- El sitio LRV Latam no tiene una relación formal con el autor visible más allá de alojar el libro. El PDF, igual, lleva el ISBN y los créditos del propio autor.

---

## 7. "Marketing para Inmobiliarios: Corredores y Tasadores"

**Ficha**
- Título exacto: *Marketing para inmobiliarios: corredores y tasadores*. La 2.ª edición figura como *Marketing para Inmobiliarios 2da Edición: Corredores y Tasadores* o "Edición actualizada".
- Autor: **Gerardo Woscoboinik**. Magíster en Comunicación Organizacional; desde 1999 dicta Principios de Marketing en la carrera de martilleros, corredores y tasadores (Univ. de Morón, UTN).
- Ediciones:
  - 1.ª ed. Lectorum-Ugerman, Buenos Aires, 2010 (e-book de 148 pp., ISBN 9789871547050).
  - 2.ª ed./actualizada, Ugerman Editor, 2021 según Google Books (ISBN 9789879468852) y 2022 en papel (ISBN 9789879468845, 174 pp.).
- Índice de la 2.ª ed.: 1) El marketing inmobiliario; 2) Filosofía y gestión empresaria; 3) Marcando el rumbo; 4) Fijando el precio: la tasación; 5) Las transformaciones en el mercado inmobiliario; 6) La estrategia de imagen y comunicación; Epílogo: ¿Quién es el corredor inmobiliario?
- Estado: **identificado**, confianza **alta**. Es argentino y está pensado para corredores matriculados.
- Fuentes: https://books.google.com.ar/books/about/Marketing_para_Inmobiliarios_2da_Edici%C3%B3.html?id=mz3rEAAAQBAJ [cons. 11/9/2026]; https://biblioteca.usam.edu.sv/bib/67837 [cons. 11/9/2026]; https://www.buscalibre.es/libro-marketing-para-inmobiliarios-corredores-y-tasadores/9789879468845/p/54357473 [cons. 11/9/2026]; https://www.buscalibre.com.ar/libro-marketing-para-inmobiliarios/9789871547050/p/3253018 [cons. 11/9/2026]; https://www.yenny-elateneo.com/productos/marketing-para-inmobiliarios-edicion-actualizada/ [cons. 11/9/2026]

**Principios [solo índice].** No se accedió a ningún fragmento del texto. Cada fila solo afirma que el libro trata el tema; el cómo no está verificado.

| Tema del libro (verificable) | Aplicación DOMINIA | Fuente |
|---|---|---|
| El marketing inmobiliario como disciplina propia del corredor, con ejemplos de corredores de CABA y del interior. | Cada respuesta a una consulta es una pieza de marketing de DOMINIA, no un trámite. | Google Books y Buscalibre (descripción e índice) [cons. 11/9/2026] |
| Fijar el precio es parte del marketing: la tasación como fundamento del precio (cap. 4). | Ante "está caro", explicar en qué se funda el precio (ubicación, m², plan en obra frente al terminado) en vez de ofrecer descuento. | Google Books (índice) [cons. 11/9/2026] |
| La estrategia de imagen y comunicación (cap. 6). | Imagen y mensajes coherentes en todos los canales (fotos, firma, tono, datos). | Google Books (índice) [cons. 11/9/2026] |
| Las transformaciones del mercado y el rol profesional del corredor (cap. 5 y epílogo). | Tratar a las inmobiliarias colegas como profesionales: información completa y ordenada para que puedan llevar interesados a visitar. | Google Books (índice) [cons. 11/9/2026] |

**Qué no se pudo verificar**
- El texto y las técnicas concretas del libro: Google Books no ofrece vista previa y Amazon y Mercado Libre bloquearon el acceso.
- La fecha exacta de la 2.ª edición: 2021 o 2022 según la fuente.

---

## 8. "Fideicomisos al costo"

**Ficha**
- Título exacto: *Fideicomisos al costo: el modelo de negocios inmobiliarios más exitoso de los últimos años en la Argentina*.
- Autor/director: **Damián Tabakman**, arquitecto, consultor y actual presidente de CEDU. Colaboran María T. Acquarone, Mario Gómez y Gervasio Ruiz de Gopegui. Incluye capítulos testimoniales ("Experiencias concretas: Los referentes del mercado") de Roberto Aisenson, Miguel Ángel Camps y Gustavo Llambías, entre otros.
- Editorial: Bienes Raíces Ediciones (BRE), Buenos Aires, 2011, 1.ª ed. 318 pp. ISBN 9789871630073.
- Contenido según los catálogos: cómo se estructuran y financian los fideicomisos, los riesgos de cada actor, la rentabilidad esperada y la retribución del desarrollista, la mirada crítica del sector y el contexto legal (Ley 24.441).
- **Ojo**: el marco legal del libro es la Ley 24.441. Desde 2015 el fideicomiso se rige por el Código Civil y Comercial (arts. 1666 y siguientes).
- Estado: **identificado**, confianza **alta**.
- Fuentes de ficha: https://cpau.opac.com.ar/pergamo/documento.php?ui=1&recno=15754&id=CPAU.1.15754 [cons. 11/9/2026]; https://biblioteca.colegio-escribanos.org.ar/cgi-bin/koha/opac-detail.pl?biblionumber=28729 [cons. 11/9/2026]
- Fuente secundaria con citas textuales del libro: tesina de Verónica S. Scalzotto, "Fideicomiso inmobiliario al costo", UFLO, nov-2018, que cita los capítulos de Aisenson (pp. 238-243), Camps (pp. 245-252) y Llambías (pp. 253-260). https://repositorio.uflo.edu.ar/server/api/core/bitstreams/32be9b87-6d93-4b1b-933d-4de77eead371/content [cons. 11/9/2026]
- Cita (cap. de M. A. Camps, según la tesina UFLO): "El fideicomiso no es una palabra mágica".

**Principios**

| Técnica | Aplicación DOMINIA | Fuente |
|---|---|---|
| Quien suscribe un fideicomiso al costo le da un mandato al fiduciario para ejecutar un plan de negocio que debe conocer y compartir. Es muy distinto de comprar con boleto. | Si DOMINIA vende al costo, explicar en la reunión qué firma el interesado (adhesión a un fideicomiso, no un boleto por precio fijo), sin minimizarlo. | tesina UFLO, cita del cap. de G. Llambías [cons. 11/9/2026] |
| El fideicomiso no resuelve los problemas por sí solo. El conflicto está latente y aparece cuando el mercado no acompaña. Ante un problema de obra hay que convocar e informar enseguida a los fiduciantes. | No presentar la figura como garantía. En la posventa, comunicar rápido y de forma proactiva cualquier atraso o novedad. | tesina UFLO, cita del cap. de M. A. Camps [cons. 11/9/2026] |
| Buena práctica: firmar el fideicomiso con el 100% suscripto y el costo cierto. Primero hay una estimación y la certeza se da recién al firmar. Todo depende de la calidad del presupuesto. | No dar por escrito cifras finales que todavía son estimaciones. Si el costo o la cuota son estimados, decirlo. | tesina UFLO, cita del cap. de M. A. Camps [cons. 11/9/2026] |
| Vender por el producto y la necesidad genuina (tipología, forma de renta), no solo porque el costo es bajo frente al precio. Un anticipo importante compromete al fiduciante con el proyecto. | Argumentar con la unidad y el estilo de vida, no solo con "es más barato que el terminado". | tesina UFLO, cita del cap. de M. A. Camps [cons. 11/9/2026] |
| El fideicomiso, al ser una estructura legislada con roles definidos, aporta transparencia y "congela" la voluntad inicial de las partes en el contrato. | Explicar con claridad quién es fiduciario, quién desarrollista y quién constructor, y dónde está escrito cada rol. | tesina UFLO, cita del cap. de G. Llambías [cons. 11/9/2026] |
| Al costo o sistema tradicional. En el al costo los inversores cubren su parte del costo (tierra y obra) y absorben los aumentos; en el precio fijo el desarrollista asume el riesgo de costo y de mercado. Riesgos típicos del al costo: presupuestos defectuosos, mala gestión y errores de obra. Además, los honorarios del desarrollista atados a la inversión pueden desalinear incentivos. | El copiloto nunca afirma "precio final" en un esquema al costo. Tiene que saber qué esquema usa cada proyecto DOMINIA y responder según ese esquema. | https://www.reporteinmobiliario.com/article1662-fideicomisos-al-costo-versus-sistema-tradicional.html (D. Tabakman, 2/7/2010) **[autor, no libro]** [cons. 11/9/2026] |
| En el al costo "no se vende una unidad sino derechos" (paráfrasis de Tabakman en prensa): es un producto de inversión. Los retrasos en los pagos tienen penalidades. | Usar la palabra correcta: "adhesión o cesión de derechos sobre una unidad futura", no "te vendo el depto". Informar desde el principio que la mora tiene costo. | https://www.cronista.com/impresa-general/las-claves-para-comprar-al-costo/ (C. Quiroga, 26/10/2010) **[autor, no libro]** [cons. 11/9/2026] |

**Qué no se pudo verificar**
- El índice completo y el texto de los capítulos de Tabakman, Acquarone, Gómez y Ruiz de Gopegui. Los principios del libro vienen de citas textuales en una tesis universitaria. Los dos últimos son artículos del autor.
- Si hay ediciones posteriores actualizadas al Código Civil y Comercial.

---

## Reglas para mensajes escritos (qué mostrar y qué no por WhatsApp/portal)

Aclaración: **ninguna fuente consultada habla específicamente de WhatsApp**. Las reglas juntan lo que las fuentes dicen sobre el primer contacto, la comunicación escrita, la publicidad y la precalificación. Donde la regla es una extensión nuestra, se marca *(inferencia)*.

1. **El objetivo del mensaje es un avance, es decir, la visita agendada. No es el cierre.** Fuentes: Villarroya, https://www.inmonews.es/las-dos-vias-al-cierre-de-la-venta-personal-inmobiliaria/ [cons. 11/9/2026]; MREA (leads, luego citas), https://outfront.kw.com/training/back-to-business-basics-economic-model/ [cons. 11/9/2026]
2. **No negociar precio ni condiciones en el primer contacto escrito.** Todavía no hay rapport y se negocia en desventaja: responder con el plan vigente e invitar a verse. Fuente: https://massimoforte.com/blog/as-chaves-da-negociacao-imobiliaria/ [cons. 11/9/2026]
3. **Precalificar conversando, no interrogando.** Pocas preguntas, una o dos por mensaje, sobre motivación, urgencia, necesidad y capacidad de pago. Fuentes: https://massimoforte.com/blog/quer-guiar-ou-ser-guiado/ [cons. 11/9/2026]; https://massimoforte.com/blog/comunicar-para-vender-contributo-do-vitor-neves/ [cons. 11/9/2026]
4. **Cada respuesta termina con un próximo paso concreto** (una pregunta o dos opciones de horario), para guiar la conversación. Fuente: https://massimoforte.com/blog/quer-guiar-ou-ser-guiado/ [cons. 11/9/2026]
5. **Al agendar: día, hora, dirección, qué se va a ver, y aviso de que se confirmará antes. Confirmar el día previo.** Si cancela con un motivo creíble, reprogramar. Si las excusas se repiten, pasar a seguimiento largo. Fuente: https://www.inmonews.es/concertacion-de-entrevistas-de-venta-inmobiliarias/ [cons. 11/9/2026]
6. **Sin presión ni urgencia artificial.** Nada de fórmulas de cierre enlatadas ni de "últimas unidades, decidí hoy". Las fuentes legales la señalan como alerta de estafa. Fuentes: https://www.inmonews.es/el-cierre-magico-de-la-venta/ [cons. 11/9/2026]; https://cpsabogados.com.ar/fideicomiso-departamento-en-pozo-15-senales-de-alerta-para-evitar-una-estafa/ [cons. 11/9/2026]
7. **Sinceridad en la descripción: decir lo que falta o lo que no tiene.** Atrae al cliente correcto y ahorra visitas inútiles. Fuente: https://massimoforte.com/blog/quais-melhores-estrategias-para-atrair-e-fidelizar-clientes-compradores/ [cons. 11/9/2026]
8. **Lo que se escribe o publica puede integrar la oferta.** Según doctrina y jurisprudencia (incluido un fallo de la Cámara de Córdoba de 2016, *Ahumada c/ Oliver Group*), la publicidad obliga al desarrollista y el deber de información vale antes, durante y después del contrato. Por eso no escribir m², terminaciones, amenities, fechas ni precios que no estén en la documentación vigente. Fuente: https://aldiaargentina.microjuris.com/2020/04/14/la-relacion-de-consumo-en-los-contratos-de-fideicomiso/ (F. Netri, 2020) [cons. 11/9/2026]
9. **Un render no reemplaza la memoria descriptiva.** Mostrar solo renders, sin especificaciones técnicas, es una de las señales de alerta. Se pueden mandar imágenes, aclarando que son ilustrativas y que la memoria descriptiva es la que manda. Fuente: https://cpsabogados.com.ar/fideicomiso-departamento-en-pozo-15-senales-de-alerta-para-evitar-una-estafa/ [cons. 11/9/2026]
10. **Nunca escribir "rentabilidad asegurada", "sin riesgo", "precio final" (en un esquema al costo) ni "cuota fija" si ajusta por índice.** Las garantías "demasiado seguras" son señal de alerta. En el al costo el inversor absorbe los mayores costos. Fuentes: https://cpsabogados.com.ar/fideicomiso-departamento-en-pozo-15-senales-de-alerta-para-evitar-una-estafa/ [cons. 11/9/2026]; https://www.reporteinmobiliario.com/article1662-fideicomisos-al-costo-versus-sistema-tradicional.html [cons. 11/9/2026]
11. **El ajuste por CAC se explica con ejemplos y queda por escrito en el plan.** Las fuentes piden un plan de pagos con ejemplos de ajuste y un ajuste atado explícitamente al índice. *(inferencia)*: por chat se puede adelantar la mecánica ("la cuota se actualiza mensualmente por el índice CAC"); el cálculo personalizado se entrega como documento formal o en la reunión. Fuentes: https://www.infobae.com/economia/2025/03/23/claves-para-comprar-departamentos-en-pozo-y-evitar-complicaciones-legales-y-financieras/ [cons. 11/9/2026]; https://cpsabogados.com.ar/fideicomiso-voy-a-comprar-un-departamento-en-pozo-que-necesito-saber-antes/ [cons. 11/9/2026]
12. **Material visual de calidad** (fotos, recorrido virtual, descripción que hable de los beneficios para ese público) como gancho para la visita. Fuente: https://massimoforte.com/blog/quais-melhores-estrategias-para-atrair-e-fidelizar-clientes-compradores/ [cons. 11/9/2026]
13. **Seguimiento sistemático del que no agenda.** Contactos periódicos que aporten valor, no insistencia. Fuentes: MREA (8x8 / 33 toques), https://www.easyagentpro.com/blog/millionaire-real-estate-agent-book-review-cliffnotes-part-1/ [cons. 11/9/2026]; Forte (seguir a los tibios y fríos), https://massimoforte.com/blog/cliente-comprador-ou-interessado/ [cons. 11/9/2026]
14. **Consistencia de marca en todos los canales**, incluidas las inmobiliarias colegas: los mismos datos y las mismas promesas. Fuente: *Everybody Wins* (foco en la marca), muestra https://content.e-bookshelf.de/media/reading/L-584694-5c60476270.pdf [cons. 11/9/2026]

**Normas de Córdoba.** Fuente de las reglas 15 a 19: Ley provincial 9445 de Corredores Públicos Inmobiliarios de Córdoba, con Estatuto y Código de Ética, en el PDF que publica el propio Colegio (CPI Córdoba): https://cpicordoba.org.ar/wp-content/uploads/2023/09/Ley-9445_Estatutos_codigo-de-etica_V1.pdf [cons. 11/9/2026]. Rigen para corredores matriculados. Para los asesores de DOMINIA sirven como estándar de buenas prácticas, y son de cumplimiento obligatorio para las inmobiliarias colegas.

15. **Publicidad clara, precisa y veraz sobre el estado de hecho y jurídico del inmueble. Proponer los negocios con exactitud, precisión y claridad.** En la publicidad del corredor van su nombre y su matrícula. Fuente: Ley 9445, art. 16, incs. m), n) y q).
16. **Por escrito y en voz: moderación y buen trato. La comunicación tiene que ser objetiva y veraz, sin valoraciones que puedan engañar o inducir a error.** La información al interesado debe ser veraz, exacta, detallada, clara y gratuita. Fuente: Código de Ética, art. 1, b) inc. 5 y d) inc. 3.
17. **Una promoción dirigida al público obliga mientras está vigente.** Debe decir fecha de inicio y de fin, modalidad, condiciones y limitaciones. Sin fechas, obliga hasta que se revoque por un medio similar. *(inferencia)*: toda promo o "precio de lanzamiento" que el copiloto mencione tiene que llevar vigencia y condiciones. Fuente: Código de Ética, art. 1, d) inc. 4.
18. **Mismo precio y mismas condiciones para todos.** No diferenciar a los clientes en precio, calidades u otras condiciones relevantes. *(inferencia)*: lo que se cotiza por WhatsApp tiene que coincidir con portales, Instagram y lo que reciben las inmobiliarias colegas. Fuente: Código de Ética, art. 1, a) inc. 6.
19. **Con inmobiliarias colegas: cordialidad, darles toda la información útil, cumplir estrictamente lo comprometido por escrito, no desacreditar a otros profesionales y no meterse en operaciones confiadas a otro colega sin su conocimiento.** En operaciones compartidas, los honorarios de cada uno se acuerdan con claridad. Fuente: Código de Ética, art. 1, c) incs. 1, 2, 4 y 5, y d) inc. 5.
20. **Autenticidad y prudencia: todo lo publicado queda registrado. Nada de guiones clonados. Chequear la información y cuidar la privacidad del comprador.** La mensajería se usa para coordinar y confirmar reuniones y mandar fotos, videos y ubicaciones. Fuente: Migliorisi, *El camino del real estate*, caps. 4, 5 y 6, https://lrvlatam.com/wp-content/uploads/2025/08/el-camino-del-real-estate-Por-Diego-MIgliorisi.pdf [cons. 11/9/2026]

---

## Boleto con precio financiado frente a fideicomiso al costo: cómo responder cuando preguntan "¿es fideicomiso?"

> **Dato de contexto (del coordinador, no verificado en fuentes públicas):** Casona 3 **no es un fideicomiso al costo**. Se vende con **boleto de compraventa con financiación durante la obra**: precio fijado en USD, 40% de anticipo, 30 cuotas (en USD, o en pesos ajustados por CAC) y 20% contra entrega. Antes de cada proyecto nuevo, el copiloto tiene que confirmar el esquema con el contrato real. No debe suponerlo.

### 1. La diferencia de fondo

| | Fideicomiso al costo | Boleto con precio financiado (esquema Casona 3) |
|---|---|---|
| Qué firma el comprador | La adhesión a un contrato de fideicomiso: aporta al costo del proyecto como fiduciante o beneficiario y le da un mandato al fiduciario para ejecutar un plan de negocio. | Un boleto de compraventa por una unidad determinada, con precio y plan de pagos. |
| Precio | No hay precio cerrado: se paga el costo real (tierra y obra) más los honorarios del organizador. Puede subir más que el índice y puede haber aportes extraordinarios. En la variante "costo cerrado con tope CAC", ajusta solo por CAC y el sobrecosto lo absorbe el desarrollista. | Precio fijado en USD al firmar. El riesgo de costo de obra lo asume el vendedor, que incluye su margen en el precio. |
| Quién asume el sobrecosto | El inversor, en el al costo abierto. | El vendedor o desarrollista. |
| Cuotas | Porcentajes del costo, ajustados por índice. Pueden cambiar. | Según el plan pactado: en USD, o en pesos con ajuste CAC en el esquema Casona 3. |
| Protección legal típica | Reglas del fideicomiso (CCyC arts. 1666 y ss.): patrimonio separado; si no alcanza, liquidación judicial y no quiebra (art. 1687). Ley de Defensa del Consumidor si es destinatario final. | Reglas del boleto (CCyC arts. 1170 y 1171), seguro obligatorio del art. 2071 para unidades proyectadas en propiedad horizontal, y Ley de Defensa del Consumidor. |

Fuentes de la tabla:
- Riesgo de costo en pozo con precio cerrado frente al costo: https://www.reporteinmobiliario.com/article1662-fideicomisos-al-costo-versus-sistema-tradicional.html (Tabakman, 2010) [cons. 11/9/2026]; https://www.ambito.com/edicion-impresa/los-fideicomisos-costo-cerrado-un-tope-cac-n3864880 [cons. 11/9/2026]
- Mandato frente a boleto: tesina UFLO que cita el capítulo de Llambías en *Fideicomisos al costo*, https://repositorio.uflo.edu.ar/server/api/core/bitstreams/32be9b87-6d93-4b1b-933d-4de77eead371/content [cons. 11/9/2026]
- Art. 1687: https://codigocivilonline.com.ar/articulo-1687/ [cons. 11/9/2026]
- Arts. 1170 y 1171: https://leyes-ar.com/codigo_civil_y_comercial/1170.htm y https://leyes-ar.com/codigo_civil_y_comercial/1171.htm [cons. 11/9/2026]
- Art. 2071: https://servicios.infoleg.gob.ar/infolegInternet/anexos/280000-284999/281276/norma.htm [cons. 11/9/2026]
- Consumidor: https://aldiaargentina.microjuris.com/2020/04/14/la-relacion-de-consumo-en-los-contratos-de-fideicomiso/ [cons. 11/9/2026]
- La Nación (L. Barreiro, 9/3/2023) describe el al costo como el mecanismo principal para comprar en pozo y marca sus riesgos: cuota ajustable, plazos que se estiran y emprendimientos de actores sin experiencia o sin espalda financiera. https://www.lanacion.com.ar/propiedades/inversiones/fideicomiso-al-costo-cuales-son-los-beneficios-y-los-riesgos-de-comprar-propiedades-de-pozo-nid09032023/ [cons. 11/9/2026]

### 2. Lo que el asesor tiene que saber del boleto (conocimiento de fondo, **no para prometer**)
- **Prioridad frente a embargos (art. 1170 CCyC).** El comprador de buena fe con boleto tiene prioridad sobre quien trabó una cautelar si se cumplen cuatro condiciones: (a) contrató con el titular registral o se encadena con él; (b) pagó al menos el 25% del precio antes de la cautelar; (c) el boleto tiene **fecha cierta**; (d) hay publicidad suficiente, registral o posesoria. https://leyes-ar.com/codigo_civil_y_comercial/1170.htm [cons. 11/9/2026]
- **Oponibilidad en concurso o quiebra del vendedor (art. 1171 CCyC).** El boleto de fecha cierta a favor de un adquirente de buena fe es oponible al concurso o la quiebra del vendedor si se pagó al menos el 25% del precio. El juez debe ordenar la escritura. *(inferencia)*: con un anticipo del 40% se supera ese umbral. Si el boleto de DOMINIA tiene fecha cierta, lo tiene que confirmar legal o la escribanía: **el copiloto no lo afirma.** https://leyes-ar.com/codigo_civil_y_comercial/1171.htm [cons. 11/9/2026]
- **Seguro obligatorio (art. 2071 CCyC).** Para celebrar contratos sobre unidades construidas o proyectadas en propiedad horizontal, el titular del dominio debe contratar un seguro a favor del adquirente por el riesgo de fracaso de la operación. Cubre la devolución de lo pagado con intereses o la liberación de gravámenes. La SSN fijó las condiciones con la Resolución 40925-E/2017. https://servicios.infoleg.gob.ar/infolegInternet/anexos/280000-284999/281276/norma.htm [cons. 11/9/2026]. Una nota especializada de 2019 dice que en la práctica casi no se cumple, por ambigüedades y costos. https://www.elseguroenaccion.com.ar/no-todos-los-seguros-obligatorios-se-cumplen-el-de-prehorizontal-no/ [cons. 11/9/2026]. **No sabemos si Casona 3 tiene ese seguro.** El copiloto no lo menciona como garantía hasta que DOMINIA lo confirme.
- **Qué debería tener un boleto en pozo.** Descripción de la unidad, plazos de obra y de entrega, régimen de demoras, cláusulas penales, seguro y declaración de afectación a propiedad horizontal. https://cspabogados.com.ar/boleto-de-compraventa-de-inmuebles-en-pozo/ (M. E. Castro Sammartino, 20/2/2019) [cons. 11/9/2026]. La nota de Infobae de 2025 agrega: unidad exacta, precio total, cronograma de pagos, fecha de entrega, especificaciones técnicas y un ajuste atado explícitamente al CAC. https://www.infobae.com/economia/2025/03/23/claves-para-comprar-departamentos-en-pozo-y-evitar-complicaciones-legales-y-financieras/ [cons. 11/9/2026]
- **Precio en dólares.** Desde el DNU 70/2023, que reformó el art. 765 CCyC, quien debe dólares se libera solo entregando dólares, y los jueces no pueden cambiar la moneda pactada. El mismo análisis advierte que el DNU no derogó la prohibición de indexar de la Ley 23.928 (arts. 7 y 10). https://www.colescba.org.ar/portal/?revista=el-dnu-2023-70-apn-pte-y-las-obligaciones-de-dar-dinero-en-los-contratos (P. E. Alferillo, Revista Notarial, Colegio de Escribanos de la Provincia de Buenos Aires, 2024) [cons. 11/9/2026]. **Cómo encaja legalmente la opción "pesos + CAC" no está verificado.** El copiloto no discute con el interesado si es válida: describe el mecanismo del contrato y deriva a legal.
- **Registro de boletos.** En CABA el Registro de la Propiedad habilitó la inscripción de boletos de unidades en construcción. https://www.iprofesional.com/legales/434031-compras-un-departamento-en-pozo-ya-se-puede-registrar-un-boleto-de-compraventa-en-caba [cons. 11/9/2026]. **Para Córdoba no se encontró un régimen equivalente.** Una nota de 2019 dice que el Colegio de Corredores de Córdoba impulsaba la adhesión al boleto digital nacional, sin confirmar que se haya concretado. https://infonegocios.info/nota-principal/los-corredores-inmobiliarios-del-cpcpi-trabajan-para-que-cordoba-adhiera-al-boleto-inmobiliario-digital [cons. 11/9/2026]
- **Por qué hay dólares o CAC.** Con el Rodrigazo, los precios fijos en pesos arruinaron tanto a compradores como a constructoras, y quedaron obras sin terminar. Sirve como explicación histórica, no como argumento de miedo. Migliorisi, PDF, cap. 2 [cons. 11/9/2026]

### 3. Cómo responder "¿es fideicomiso?" (guía para el copiloto)
Reglas. La base de fuentes está en la sección de reglas escritas; el guion concreto es *(inferencia)*.
1. **Responder directo y en la primera línea: "No, no es un fideicomiso."** Enseguida, qué es: compra directa por boleto, precio fijado en dólares y financiación durante la obra. Base: veracidad y claridad (Código de Ética CPI Córdoba, art. 1 d) inc. 3) y respuestas que no esquivan (Migliorisi, cap. 6).
2. **Explicar la diferencia en una frase, sin tecnicismos.** En el fideicomiso al costo el comprador paga lo que la obra termine costando. Acá el precio ya está fijado y el riesgo de que la obra cueste más lo asume el desarrollista. Base: Tabakman 2010; Ámbito 2014.
3. **Aclarar la opción en pesos sin prometer equivalencias.** Si paga en pesos, la cuota se actualiza por el índice CAC. No decir "es lo mismo que en dólares" ni estimar cuánto va a subir. Base: Infobae 2025 sobre la transparencia del ajuste; CPS 2026 sobre ajustes descontrolados como señal de alerta.
4. **No desacreditar a los fideicomisos ni a otros desarrolladores.** Nada de "los fideicomisos son peligrosos, lo nuestro es seguro". Además de ser una promesa que no se puede verificar, choca con la moderación y objetividad que pide el Código de Ética (art. 1 b) inc. 5 y c) inc. 1).
5. **No usar como garantía lo que no está confirmado:** seguro del art. 2071, fecha cierta, inscripción del boleto, fecha de entrega. Si el interesado pregunta "¿qué garantías tengo?" (la pregunta que Migliorisi pone como central, cap. 6), responder con la lista validada por DOMINIA o con "te lo mostramos con el modelo de boleto en la reunión".
6. **Cerrar con un avance: ofrecer mostrar el modelo de boleto y el plan de pagos en la visita.** Base: Villarroya (avance), Forte (no negociar condiciones en el primer contacto escrito).

**Ejemplo de respuesta *(inferencia; ajustar con datos validados por DOMINIA)*:**
> "¡Hola, Laura! No, Casona 3 no es un fideicomiso: la compra se hace por boleto de compraventa directo, con el precio fijado en dólares desde que firmás. Pagás un 40% de anticipo, 30 cuotas durante la obra (en dólares, o en pesos actualizadas por el índice CAC) y el 20% restante contra entrega. La diferencia con un fideicomiso al costo es que acá, si la obra termina costando más, esa diferencia no la pagás vos. ¿Querés que te muestre el modelo de boleto y el plan de pagos en la visita? Tengo lugar el jueves 18 a las 17 o el sábado 20 a las 11."

### 4. Lo que el asesor NO puede prometer en un boleto con precio financiado
- Que la cuota en pesos va a mantenerse igual o equivaler a la cuota en dólares.
- Fecha de entrega "segura" más allá del contrato, y garantías (seguro, inscripción) no confirmadas por DOMINIA.
- Revalorización o renta. Que "el pozo es más barato que el terminado", si no está verificado para ese proyecto. En algunos proyectos de la zona el pozo puede estar por encima del terminado: validar con los datos de precios de DOMINIA.
- Características que no estén en la memoria descriptiva o en los planos. El render es ilustrativo.
- Opiniones legales sobre la validez de cláusulas: se derivan a legal o a la escribanía.
- Fuentes: https://cpsabogados.com.ar/fideicomiso-departamento-en-pozo-15-senales-de-alerta-para-evitar-una-estafa/ [cons. 11/9/2026]; https://aldiaargentina.microjuris.com/2020/04/14/la-relacion-de-consumo-en-los-contratos-de-fideicomiso/ [cons. 11/9/2026]; Código de Ética CPI Córdoba (art. 1 d) inc. 3 y 4) [cons. 11/9/2026]; Migliorisi, cap. 3 (el pozo compitiendo con el terminado) [cons. 11/9/2026]

### 5. Si el interesado sí pregunta por fideicomisos en general (para comparar con otra oferta)
Resumen de lo verificado, para explicar sin desacreditar:
- **Es un instrumento, no una garantía.** Conviene evaluar el negocio de fondo, la trayectoria del desarrollista, si el fideicomiso está constituido, quién es dueño del terreno y qué pasa si faltan adherentes. https://www.lanacion.com.ar/economia/una-buena-senal-que-le-dio-aire-al-mercado-nid1559415/ [cons. 11/9/2026]. En palabras del capítulo de Camps en el libro de Tabakman, "no es una palabra mágica" (tesina UFLO) [cons. 11/9/2026].
- **Riesgos del al costo:** presupuestos defectuosos, mala gestión, errores de obra, aportes extraordinarios, demoras por falta de preventa. Tabakman 2010 (URL arriba); https://abogados.com.ar/el-fideicomiso-de-construccion-al-costo-y-los-esquemas-de-indexacion-previstos-por-el-decreto-146-17/19740 [cons. 11/9/2026]; Infobae 2025 [cons. 11/9/2026]
- **Antecedentes en Córdoba:** causas Euromayor (fideicomisos, unidades pagadas y no entregadas) y Márquez y Asociados (desvío de fondos). Explican la desconfianza del público local; el copiloto **no los usa para atacar a la competencia**. https://www.perfil.com/noticias/cordoba/despues-de-seis-anos-de-investigacion-elevan-a-juicio-la-megaestafa-inmobiliaria-del-grupo-euromayor.phtml [cons. 11/9/2026]; https://www.perfil.com/noticias/cordoba/efecto-marquez-y-asociados-diputado-cordobes-presento-un-proyecto-para-proteger-a-los-compradores-de-inmuebles-en-pozo.phtml [cons. 11/9/2026]
- **Proyecto de ley nacional de protección del comprador en pozo** (dip. Agost Carreño, mayo de 2025): registro de desarrollistas, fondo de garantía, informes trimestrales. **Proyecto; su sanción no está verificada.** Mismo enlace de Perfil [cons. 11/9/2026].

### Qué no se pudo verificar en esta sección
- El texto del boleto de Casona 3.
- Si el boleto tiene fecha cierta o si se puede inscribir en Córdoba.
- Si existe el seguro del art. 2071.
- Cómo se calcula la cuota en pesos: si parte del valor en USD convertido a una fecha o de un monto en pesos que se indexa.
- La base legal de la indexación CAC en un contrato con precio en USD.
- La vigencia actual del Decreto 146/2017.

---

## Material gratuito legítimo (punto 1 de la ampliación)

| Material | Quién lo publica y por qué es legítimo | Uso |
|---|---|---|
| *El camino del real estate: Argentina 1956-2025* (PDF completo, 109 pp.) — https://lrvlatam.com/wp-content/uploads/2025/08/el-camino-del-real-estate-Por-Diego-MIgliorisi.pdf | Lo pone el autor como descarga gratuita en la página del libro. Los créditos del PDF indican edición del autor, "descarga y online", con ISBN propio. | **Leído**: base del libro 6 y de reglas escritas y de boleto. |
| *Everybody Wins*: prólogo y prefacio (30 pp.) — https://content.e-bookshelf.de/media/reading/L-584694-5c60476270.pdf | Muestra de lectura de la edición de Wiley que la librería e-bookshelf ofrece como "reading sample". | **Leído**: base del libro 4. |
| Ley 9445, Estatuto y Código de Ética del CPI Córdoba — https://cpicordoba.org.ar/wp-content/uploads/2023/09/Ley-9445_Estatutos_codigo-de-etica_V1.pdf | Lo publica el propio Colegio Profesional de Corredores Públicos Inmobiliarios de Córdoba en su sitio. | **Leído**: reglas escritas 15 a 19 y guía "¿es fideicomiso?". |
| Tesina "Fideicomiso inmobiliario al costo" (V. Scalzotto, UFLO, 2018) — https://repositorio.uflo.edu.ar/server/api/core/bitstreams/32be9b87-6d93-4b1b-933d-4de77eead371/content | Repositorio institucional abierto de la Universidad de Flores. Cita textualmente capítulos del libro de Tabakman. | **Leído**: base del libro 8. |
| Muestra de 20 pp. de *O Poder da Prospeção* (M. Forte) — https://massimoforte.com/produto/ebook-o-poder-da-prospecao/ | La publica el autor, pero pide registro con datos personales, y además es otro libro, no *Comunicar para Vender*. | **No usado.** |
| Villarroya, 14 pp. en FlipHTML5 — https://fliphtml5.com/lner/smap/basic | No se pudo comprobar quién lo subió (403). | **No usado.** |
| MREA en castellano (Scribd) | Solo en copias no autorizadas. | **No usado.** |
| Woscoboinik, Tabakman (libro completo), Forte (*Comunicar para Vender*) | No se encontró muestra oficial gratuita. Google Books no mostró vista previa de Woscoboinik. | — |
