function ehPrimo(numero) {
  let contadorDivisores = 0;
  for (let i = 1; i <= numero; i++) {
    if (numero % i === 0)
      contadorDivisores++;
  }

  if (contadorDivisores == 2) return true;
  return false;
}

let numero = prompt("Insira um número: ");

var [body] = document.getElementsByTagName("body");

ehPrimo(numero) ? body.innerHTML = `O número ${numero} eh primo` : body.innerHTML = `O número ${numero} NÃO é primo`