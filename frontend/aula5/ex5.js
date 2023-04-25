var valor1 = prompt("Insira um valor:")
var valor2 = prompt("Insira um segundo valor:")
var valor3 = prompt("Insira um terceiro valor:")

var array = [valor1, valor2, valor3]

console.log(`Maior: ${array.find(val, index => val > array[index - 1])}`)