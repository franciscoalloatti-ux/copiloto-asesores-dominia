// Chequeos de las reglas duras del copiloto (V1 en adelante), en JavaScript.
// Es el mismo archivo para el front (generar_visor.py lo inserta en visor/index.html) y para el test de
// paridad con Python (pruebas/test_paridad.py), así las dos implementaciones no se separan (D-28).
(function (raiz) {
const DIAS = ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"];
const diaDe = d => DIAS[(d.getDay() + 6) % 7];
const norm = s => String(s).replace(/°/g, "º").replace(/\s+/g, "").toUpperCase();

function verificarFicha(f, datos, llamadas, tarifario){
  const out = [], ch = (codigo, regla, ok, detalle = "") => out.push({codigo, regla, ok, detalle});
  const borrador = f.borrador_mensaje || "";
  const lista = f.lista_asignada.lista;
  const edif = lista === "casona_2_terminados" ? "Casona 2" : lista === "casona_3_pozo" ? "Casona 3" : null;
  ch("V1", "Consultó el tarifario antes de responder", llamadas.length > 0, `${llamadas.length} llamada(s)`);
  const edificios = [...new Set(f.unidades_propuestas.map(u => u.edificio))];
  ch("V2", "Lista única: unidades de un solo edificio y coherentes con la lista asignada",
     edif ? edificios.every(e => e === edif) : f.unidades_propuestas.length === 0,
     `lista=${lista}; edificios propuestos=${edificios.join(", ") || "—"}`);
  const malas = [];
  for (const u of f.unidades_propuestas){
    const fila = tarifario.find(x => x.edificio === u.edificio && norm(x.unidad) === norm(u.unidad));
    if (!fila) malas.push(`${u.edificio} ${u.unidad}: no existe en el tarifario`);
    else if (Number(fila.precio_lista_usd) !== u.precio_lista_usd) malas.push(`${u.unidad}: USD ${u.precio_lista_usd} ≠ tarifario USD ${fila.precio_lista_usd}`);
    else if (fila.disponible !== "si") malas.push(`${u.unidad}: no está disponible`);
  }
  ch("V3", "Precios y disponibilidad idénticos al tarifario", !malas.length, malas.join("; "));
  ch("V4", "Hasta 3 unidades propuestas", f.unidades_propuestas.length <= 3, `${f.unidades_propuestas.length} unidad(es)`);
  const montos = [...borrador.matchAll(/USD\s*([\d.]{4,})/g)].map(m => Number(m[1].replace(/\./g, "")));
  const permitidos = new Set();
  tarifario.filter(x => x.edificio === edif).forEach(x => ["precio_lista_usd","anticipo_usd","cuota_mensual_usd","saldo_contra_entrega_usd"]
    .forEach(k => { if (x[k]) permitidos.add(Number(x[k])); }));
  const fuera = montos.filter(m => !permitidos.has(m));
  ch("V5", "Todo monto en USD del borrador sale del tarifario de la lista asignada", !fuera.length,
     fuera.length ? `montos no respaldados: ${fuera.join(", ")}` : `${montos.length} monto(s)`);
  const alCliente = (borrador + " " + (f.seguimiento || []).map(s => s.texto).join(" ")).toLowerCase();
  const prohibidas = ["descuento","bonificaci","comisi","rebaja"].filter(p => alCliente.includes(p));
  ch("V6", "El borrador y el seguimiento no mencionan descuentos ni comisiones", !prohibidas.length, prohibidas.join(", "));
  const promesas = ["garantiz","te aseguro","sin dudas","se revaloriza","rentabilidad asegurada","olímpica","semiolímpica",
                    "seguro de caución","fecha cierta","últimas unidades","última unidad","solo por hoy","decidí hoy"]
                   .filter(p => alCliente.includes(p));
  ch("V7", "El borrador no promete lo que no se puede cumplir ni mete urgencia artificial", !promesas.length, promesas.join(", "));
  const firma = `${datos.asesor}, Asesor Comercial de DOMINIA`;
  ch("V8", "Firma exacta del asesor", borrador.trim().endsWith(firma), `esperada: «${firma}»`);
  const lineas = borrador.trim().split("\n").filter(l => l.trim());
  const tope = datos.canal === "inmobiliaria" ? 2 : 1;
  ch("V11", "El asesor se presenta al inicio (primera línea; con colegas, primera o segunda)",
     lineas.slice(0, tope).some(l => l.includes(datos.asesor)), `inicio: «${lineas.slice(0, tope).join(" / ").slice(0, 80)}»`);
  const preguntas = (borrador.match(/\?/g) || []).length;
  ch("V9", "Como máximo dos preguntas", preguntas <= 2, `${preguntas} pregunta(s)`);
  const palabras = borrador.split(/\s+/).filter(Boolean).length;
  const corto = ["whatsapp","instagram"].includes(datos.canal);
  ch("V10", "Menos de 120 palabras en WhatsApp o Instagram", palabras < 120 || !corto, `${palabras} palabras · canal ${datos.canal}`);
  // La fecha se lee igual que en Python: los primeros diez caracteres; sin fecha exacta, no se verifica (D-28).
  const mFecha = /^(\d{4})-(\d{2})-(\d{2})/.exec(datos.fecha || "");
  const d0 = mFecha ? new Date(Number(mFecha[1]), Number(mFecha[2]) - 1, Number(mFecha[3]), 12) : null, errados = [];
  const texto = (borrador + " " + (f.proximo_paso.propuesta_de_visita || "")).toLowerCase();
  if (d0) for (const m of texto.matchAll(/(lunes|martes|miércoles|jueves|viernes|sábado|domingo)\s+(\d{1,2})\/(\d{1,2})/g)){
    const anio = d0.getFullYear() + (Number(m[3]) < d0.getMonth() + 1 ? 1 : 0);
    const real = diaDe(new Date(anio, Number(m[3]) - 1, Number(m[2])));
    if (real !== m[1]) errados.push(`«${m[1]} ${m[2]}/${m[3]}» es ${real}`);
  }
  ch("V12", "Días de la semana coherentes con las fechas propuestas", !errados.length,
     errados.join("; ") || `${[...texto.matchAll(/\d{1,2}\/\d{1,2}/g)].length} fecha(s) verificada(s)`);
  const hayVisita = f.camino_del_comprador.etapa === "listo_para_visita", b = borrador.toLowerCase();
  const faltan = [["la dirección", b.includes("costanera de la cañada 4140")],
                  ["el aviso de confirmación", b.includes("confirmo el día anterior") || b.includes("te confirmo")]]
                 .filter(x => !x[1]).map(x => x[0]);
  ch("V13", "Si la visita quedó acordada, el borrador lleva dirección y aviso de confirmación", !hayVisita || !faltan.length,
     !hayVisita ? "la visita todavía no está acordada" : (faltan.length ? "falta " + faltan.join(" y ") : "dirección y confirmación"));
  const vocab = ["jardín privado","jardin privado","jardín propio","patio privado","monoambiente","pileta olímpica"]
                .filter(v => alCliente.includes(v));
  ch("V14", "Sin vocabulario que la ficha desmiente (el jardín es de uso exclusivo)", !vocab.length, vocab.join(", "));
  const boton = /me interesa .+ de casona (iii|3)\b/.test((datos.consulta || "").toLowerCase());
  const preguntasTxt = borrador.match(/[^.!?\n]*\?/g) || [];
  const preguntaPago = preguntasTxt.some(q => /pag|cuota|contado|crédito|credito|financ/.test(q.toLowerCase())
                                         && !/a las \d/.test(q.toLowerCase()));
  ch("V15", "Si la consulta vino del botón de la web, el borrador pregunta cómo paga (T-28)", !boton || preguntaPago,
     !boton ? "la consulta no vino del botón de la web" : (preguntaPago ? "pregunta por la forma de pago" : "no pregunta cómo piensa pagar"));
  return out.sort((a, b) => Number(a.codigo.slice(1)) - Number(b.codigo.slice(1)));
}

const api = {verificarFicha, DIAS, diaDe, norm};
if (typeof module !== "undefined" && module.exports) module.exports = api; else Object.assign(raiz, api);
})(typeof globalThis !== "undefined" ? globalThis : this);
