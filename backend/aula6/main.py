# import utils as validacoes

# from utils import validacoes

import utils

texto = 'Olá, eu tenho 20 anos!'
numeros = utils.extrai_numeros(texto)
print(numeros) 

cep = '12345-678'
if utils.cep_valido(cep):
    print(f'O CEP {cep} é válido.')
else:
    print(f'O CEP {cep} é inválido.')

cpfs = [
    '12345678900',    # CPF inválido
    '98765432100',    # CPF inválido
    '529.982.247-25', # CPF válido
    '862.883.667-57', # CPF válido
    '153.509.460-56', # CPF válido
    '017.497.150-15', # CPF válido
]

for cpf in cpfs:
    if utils.valida_cpf(cpf):
        print(f'O CPF {cpf} é válido.')
    else:
        print(f'O CPF {cpf} é inválido.')

cnpj = '12.345.678/0001-01'
if utils.valida_cnpj(cnpj):
    print(f'CNPJ {cnpj} válido')
else:
    print(f'CNPJ {cnpj} inválido')


data = "20/04/2020"

utils.confere_data(data)

uf = 'SP'
if utils.valida_uf(uf):
    print(f'UF {uf} válida')
    estado = utils.estado_por_uf(uf)
    print(estado)
else:
    print(f'UF {uf} inválida')

