frase_lista = input("Insira uma frase: ").split(" ")
frase_formatada = ""
primeira_palavra = True

for palavra in frase_lista:
    if(palavra != "" and not primeira_palavra):
        frase_formatada += f" {palavra}"
    elif(palavra != "" and primeira_palavra):
        frase_formatada += palavra
        primeira_palavra = False

print(frase_formatada)