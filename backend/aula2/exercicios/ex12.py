valor_compra = float(input("Insira o valor da compra: "))
cupom = input("Insira o Cupom de Desconto: ")
cupom = cupom.upper()

if(cupom == "APP5"):
    print(f"O preço com desconto é R$ {valor_compra-(valor_compra*0.05)}")
elif(cupom == "APP10"):
    print(f"O preço com desconto é R$ {valor_compra-(valor_compra*0.10)}")
elif(cupom == "APP15"):
    print(f"O pre;o com desconto é R$ {valor_compra-(valor_compra*0.15)}")
else:
    raise Exception(f"Cupom {cupom} não existe ou já foi esgotado.")