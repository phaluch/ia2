/**
 * Função que gera um população aleatória
 * @param  {int} nInd Número de Indivíduos
 * @param  {Array} cromLim Matriz de valores possíveis pra cada cromossomo
 * @return {Array} A população criada
 */
function newPop(nInd, cromLim) {
  var nCrom = cromLim.length;

  var newPop = [];

  for (const i in [...Array(nInd).keys()]) {
    newPop[i] = [];
    for (const j in [...Array(nCrom).keys()]) {
      let inf = cromLim[j][0];
      let sup = cromLim[j][1];
      newPop[i][j] = Math.random() * (sup - inf) + inf;
    }
  }

  return newPop
}