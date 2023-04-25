var sexo = prompt("Qual é o seu sexo?")
sexo.toLowerCase()

const [body] = document.getElementsByTagName("body")

const validaSexo = (sexo) => {
  sexo === 'm' || sexo === 'f' ?
    (sexo === 'm' ? body.innerHTML = "Sexo Masculino" : body.innerHTML = "Sexo Feminino")
    : body.innerHTML = "Opção Inválida"
}

validaSexo(sexo)