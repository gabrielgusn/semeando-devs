temperatura_fahrenheit = float(input("Insira uma temperatura: "))

temperatura_convertida = 5 * (temperatura_fahrenheit - 32)/9

print("%.2fºF equivale a %.2fºC" % (temperatura_fahrenheit, temperatura_convertida))