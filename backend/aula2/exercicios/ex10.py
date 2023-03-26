d1 = {
    "batata": 1.25,
    "tomate": 5.00,
    "repolho": 3.00,
    "abóbora": 2.50
    }

d2 = {
    "abobrinha": 4.00,
    "tomate": 5.50,
    "cebola-rocha": 7.25,
    "batata": 2.40
}

lista_formatada = f"{set(d1).intersection(set(d2))}"

lista_formatada = lista_formatada.strip("{").strip("}").replace("\'", "")



print(f"Os produtos em comum são: {lista_formatada}")