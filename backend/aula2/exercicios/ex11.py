def print_dicionario(dicionario):
    for (nome, valor) in dicionario.items():
        print(f"\t{nome}: {valor}")

usuario = {
    "nome": input("Insira o nome: "),
    "nota_1": float(input("Insira a nota 1: ")),
    "nota_2": float(input("Insira a nota 2: "))
}

print("\nDicionário antigo:")
print_dicionario(usuario)

usuario["media_aluno"] = (usuario["nota_1"] + usuario["nota_2"]) / 2

print("\nDicionário novo:")
print_dicionario(usuario)
