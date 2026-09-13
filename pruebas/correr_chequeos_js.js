// Corre los chequeos de JavaScript (visor/chequeos.js) sobre los casos que arma pruebas/test_paridad.py.
const fs = require("fs");
const path = require("path");
const {verificarFicha} = require(path.join(__dirname, "..", "visor", "chequeos.js"));
const {casos, tarifario} = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const salida = {};
for (const caso of casos) {
  const chequeos = verificarFicha(caso.ficha, caso.datos, Array(caso.llamadas).fill({}), tarifario);
  salida[caso.nombre] = Object.fromEntries(chequeos.map(x => [x.codigo, x.ok]));
}
process.stdout.write(JSON.stringify(salida));
