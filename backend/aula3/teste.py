# ler um valor de um produto, e caso o valor seja maior que 100 reais, aplicar um desconto de 5%. Caso contrário, não precisa aplicar desconto.

valor = input('Informe o valor do produto: ')

valor = float(valor)

if valor > 100:
    valor = valor = valor * 0.05

print(valor)