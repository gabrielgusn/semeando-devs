var quantiaOvos = prompt("Digite a quantia de ovos que você irá comprar:")

console.log(`${quantiaOvos / 12 <= 1 ? `Sera comprada ${quantiaOvos / 12} duzia` : `Serão compradas ${quantiaOvos / 12} duzias`}`)