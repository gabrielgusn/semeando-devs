function ehBissexto(ano) {
  if (ano % 4 === 0 && ano % 100 !== 0) return true
  return false
}

var ano = prompt("Insira um ano:")

var [body] = document.getElementsByTagName("body")

body.innerHTML = ehBissexto(ano) ? `O ano ${ano} é bissexto` : `O ano ${ano} NÃO é bissexto`