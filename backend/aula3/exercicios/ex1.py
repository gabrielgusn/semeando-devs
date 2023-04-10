tipo = (input('Tipo: ')).upper()
valor_litro = float(input('Valor do litro: '))
litros = float(input('Litros: '))
valor_total = 0

if(tipo == 'A'):
  if(litros<20):
    valor_total = litros * valor_litro - ((litros*valor_litro)*0.03)
  else:
    valor_total = litros * valor_litro - ((litros*valor_litro)*0.05)
  print('O valor com desconto é: %.2f' % valor_total)
elif(tipo == 'G'):
  if(litros<20):
    valor_total = litros * valor_litro - ((litros*valor_litro)*0.04)
  else:
    valor_total = litros * valor_litro - ((litros*valor_litro)*0.06)
  print('O valor com desconto é: %.2f' % valor_total)
else:
  print("A opção não é valida")

