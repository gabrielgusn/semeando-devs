segundos = int(input("Insira um valor em segundos:"))

horas = segundos//3600
segundos -= horas*3600
minutos = segundos//60
segundos-= minutos*60

print(f"{horas} segundos equivale a {horas}:{minutos}:{segundos}")