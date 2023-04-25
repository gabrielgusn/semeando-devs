var intervalo = [prompt("Insira um valor"), prompt("Insira um segundo valor")]

const [body] = document.getElementsByTagName("body")

body.innerHTML = "<h3>Os numeros pares sao:</h3>"
for (let i = intervalo[0]; i < intervalo[1]; i++) {
  if (i % 2 === 0) {
    if (i >= intervalo[1] - 2) {
      // if (intervalo[1] % 2 === 0) {
      //   if (i === intervalo[1]) {
      //     console.log("entrou no primeiro")
      //     body.innerHTML += i
      //     break
      //   }
      //   else if (i === intervalo[1] - 1) {
      //     console.log("entrou no segundo")
      body.innerHTML += i
      break
      // }
    }
    body.innerHTML += i + ", "
  }
}
