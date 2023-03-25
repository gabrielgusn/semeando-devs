frase = input("Insira uma frase para ser criptografada: ")

char_a = input("Insira um caracter para criptografar a ou A: ")
char_e = input("Insira um caracter para criptografar e ou E: ")
char_i = input("Insira um caracter para criptografar i ou I: ")
char_o = input("Insira um caracter para criptografar o ou O: ")
char_u = input("Insira um caracter para criptografar u ou U: ")

# frase.replace()

nova_frase = frase.replace("a", char_a)
nova_frase = nova_frase.replace("e", char_e)
nova_frase = nova_frase.replace("i", char_i)
nova_frase = nova_frase.replace("o", char_o)
nova_frase = nova_frase.replace("u", char_u)

print(nova_frase)