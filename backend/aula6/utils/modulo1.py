def extrai_numeros(texto):
    numeros = ''
    for caractere in texto:
        if caractere.isdigit():
            numeros += caractere
    return numeros