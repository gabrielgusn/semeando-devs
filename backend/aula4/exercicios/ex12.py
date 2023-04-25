cidade_a = {
    "habitantes": 80000,
    "crescimento_anual": 1.03,
}

cidade_b = {
    "habitantes": 200000,
    "crescimento_anual": 1.015
}

anos = 1
while cidade_a["habitantes"] <= cidade_b["habitantes"]:
    cidade_b["habitantes"] = int(cidade_b["habitantes"] * cidade_b["crescimento_anual"])
    cidade_a["habitantes"] = int(cidade_a["habitantes"] * cidade_a["crescimento_anual"])
    anos += 1

print(f"Passaram-se {anos} anos até a cidade A ultrapassar a cidade B")
print(f"Quantia atual de habitantes A:", cidade_a["habitantes"])
print(f"Quantia atual de habitantes B:", cidade_b["habitantes"])

