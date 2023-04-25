divisores = [1]
numero = int(input("Insira um número: "))

soma = 1
i = 2

metade = numero/2
while i <= metade:
  if(numero%i == 0):
    divisores.append(i)
    soma += i
  i += 1

if(soma  == numero):
  print(f"O número {numero} é perfeito")
else:
  print(f"O número {numero} NÃO é perfeito")

print("Divisores:", (divisores))