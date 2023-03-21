#https://docs.python.org/3/library/string.html

nome = "Gabriel"
sobrenome = "Nicolodi"

print(nome, sobrenome)

frase = "esta é uma frase"

print(frase)

varias_linhas="""
string
de
varias
linhas
"""

print(varias_linhas)

linguagem = "Python"
versao = "3.11"
resultado = linguagem + " " + versao

resultado_2 = f'{linguagem} versão {versao}'
resultado_3 = '{0} versão {1}'.format(linguagem, versao)

print(resultado)
print(resultado_2)
print(resultado_3)

print('Py' in linguagem)
print('Pi' in linguagem)
print('pi' in linguagem)

linguagem = "python versao 3.11"
print(linguagem.capitalize())
print(linguagem.title())
print(linguagem.upper())
print(linguagem.lower())
print(linguagem.find('versao'))
print(linguagem.isalnum())
print(linguagem.replace("versao", "verao"))
print(linguagem)
print(linguagem.split(' '))

dados = "1.00, 2.00, 3.00"

print(dados.split(', '))

