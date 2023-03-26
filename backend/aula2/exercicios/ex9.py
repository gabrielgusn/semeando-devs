numero = int(input("Insira um numero de 3 digitos: "))
aux_numero = numero

ultimo_num = numero//100
numero = numero%100
segundo_num = numero//10
numero = numero%10
primerio_num = numero

print(f"{aux_numero} -> {primerio_num}{segundo_num}{ultimo_num}")