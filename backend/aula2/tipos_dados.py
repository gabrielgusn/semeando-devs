#listas são tipos de dados MUTÁVEIS

lista = [1, 2, 3]
lista_2 = ['123', 'abc']
lista_3 = ['string', 1, 2.9]


lista.append(4)
print(lista)

lista.remove(3)
print(lista)

lista.insert(2, 10)
print(lista)

lista.reverse()
print(lista)

lista.sort() #tambem funciona com lista de char
print(lista)

#tuplas são tipos de dados IMUTÁVEIS

tupla = (1, 2, 3)

try:
    tupla[2] = 4 
except(TypeError):
    print(f"{TypeError}"[8:17], "ao tentar mudar tupla")

#sets sao equivalentes a conjuntos na matematica, nao repete valores

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}
c = b.intersection(a)
print(c)

d = b.union(a)
print(d)

a.add(5)
print(d)

# dict é uma sequencia nao ordenada de items

dicionario_notas = {
    'nome_aluno': 'Emanoeli',
    'nota_1': 10,
    'nota_2': 9,
}

print(dicionario_notas)
print(dicionario_notas.get('nota'))

chaves = dicionario_notas.keys()
print(chaves)

valores = dicionario_notas.values()
print(valores)

dicionario_notas['nota_3'] = 5

print(dicionario_notas)

dicionario_notas.clear()
print(dicionario_notas)