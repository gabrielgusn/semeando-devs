var nota = prompt("Insira a sua nota: ")

if (nota >= 1 && nota <= 10) {
  nota <= 6 ?
    alert("Pode buscar o cartão fidelidade, você foi reprovado!")
    :
    nota <= 7 ?
      alert("Você está em recuperação")
      :
      alert("Parabéns, você foi aprovado!")
}
else {
  alert("Nota inválida")
}