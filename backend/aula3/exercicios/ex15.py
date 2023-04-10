telefonou = (input("Telefonou para a vítima?(s ou n)")).upper()
esteve_no_local = (input("Esteve no local do crime?(s ou n)")).upper()
mora_perto = (input("Mora perto da vítima?(s ou n)")).upper()
devia = (input("Devia para a vítima?(s ou n)")).upper()
trabalhou_junto = (input("Já trabalhou com a vítima?(s ou n)")).upper()

arr_respostas = [telefonou, esteve_no_local, mora_perto, devia, trabalhou_junto]

quantia_s = 0
quantia_n = 0

for i in arr_respostas:
    if i == 'S':
        quantia_s+=1
    else:
        quantia_n+=1

print("\nClassificação: ", end='')
if(quantia_s == 2):
    print("Suspeita")
elif(3<=quantia_s<=4):
    print("Cúmplice")
elif(quantia_s == 5):
    print("Assassino")
else:
    print("Inocente")