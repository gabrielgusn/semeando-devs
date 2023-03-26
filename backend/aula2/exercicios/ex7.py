ano = int(input("Insira um ano: "))

if(ano >= 0):
  print(f"O ano {ano} d.C. pertence ao seculo {ano//100 + 1}")
else:
  print(f"O ano {-1*ano} a.C. pertence ao seculo {(-1*ano)//100 +1} a.C.")