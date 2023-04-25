var nome = prompt("Insira o nome do produto:")
var quantia = prompt("Insira a quantia que ira comprar:")
var valor = prompt("Insira o valor:")

console.log(`Sera gasto R$ ${+quantia * +valor} em ${quantia} unidades de ${nome}`)