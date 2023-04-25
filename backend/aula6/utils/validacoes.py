import re

def extrai_numeros(texto):
    numeros = ''
    for caractere in texto:
        if caractere.isdigit():
            numeros += caractere
    return numeros

def cep_valido(cep):
    padrao = r'^\d{5}-\d{3}$'
    if re.match(padrao, cep):
        return True
    else:
        return False
    
def valida_cpf(cpf):
    regex = r'^(?:(?=\d{11}$)(\d)\1{10}|[\d]{3}\.[\d]{3}\.[\d]{3}\-[\d]{2})$'
    if re.match(regex, cpf):
        return True
    else:
        return False

def valida_cnpj(cnpj):
    regex = r'^(?:(?=\d{14}$)(\d)\1{13}|(\d{2})\.\d{3}\.\d{3}\/\d{4}\-\d{2})$'
    if re.match(regex, cnpj):
        return True
    else:
        return False
    
# VALIDACAO DE DATA

def ehDiaMesAno(arrData) -> bool:
    if(len(arrData[0]) == 2 and len(arrData[1]) == 2 and len(arrData[2]) == 4):
        return True
    return False

def ehAnoMesDia(arrData) -> bool:
    if(len(arrData[0]) == 4 and len(arrData[1]) == 2 and len(arrData[2]) == 2):
        return True
    return False

def valida_dia_mes(dia, mes, ano) -> bool:
    meses31Dias = [1, 3, 5, 7, 8, 10, 12]
    meses30Dias = [4, 6, 9, 11]
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    if((1<= dia <= 31) and (mes in meses31Dias)):
        return True
    elif((1<= dia <= 30) and (mes in meses30Dias)):
        return True
    elif(mes == 2):
        if(dia == 29):
            if((ano%4 == 0)):
                if((ano % 100 == 0)):
                    if((ano % 400 == 0)):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
    elif(1<=dia<=28):
        return True
    else:
        return False

def confere_data(stringData):
    if('/' in stringData):
        numerosData = stringData.split('/')
    elif('.' in stringData):
        numerosData = stringData.split('.')

    if(ehAnoMesDia(numerosData)):
        if(valida_dia_mes(dia= numerosData[2], mes= numerosData[1], ano= numerosData[0])):
            print(f"A data {stringData} eh valida!")
    else:
        print(f"A data {stringData} NAO eh valida!")
    if(ehDiaMesAno(numerosData)):
        if(valida_dia_mes(dia= numerosData[0], mes= numerosData[1], ano= numerosData[2])):
            print(f"A data {stringData} eh valida!")
        else:
            print(f"A data {stringData} NAO eh valida!")
    else:
        print(f"A data {stringData} NAO eh valida!")

# FIM VALIDA DATA

def valida_uf(uf):
    ufs = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
    if uf.upper() in ufs:
        return True
    else:
        return False
    
def estado_por_uf(uf):
    estados = {
        'AC': 'Acre',
        'AL': 'Alagoas',
        'AP': 'Amapá',
        'AM': 'Amazonas',
        'BA': 'Bahia',
        'CE': 'Ceará',
        'DF': 'Distrito Federal',
        'ES': 'Espírito Santo',
        'GO': 'Goiás',
        'MA': 'Maranhão',
        'MT': 'Mato Grosso',
        'MS': 'Mato Grosso do Sul',
        'MG': 'Minas Gerais',
        'PA': 'Pará',
        'PB': 'Paraíba',
        'PR': 'Paraná',
        'PE': 'Pernambuco',
        'PI': 'Piauí',
        'RJ': 'Rio de Janeiro',
        'RN': 'Rio Grande do Norte',
        'RS': 'Rio Grande do Sul',
        'RO': 'Rondônia',
        'RR': 'Roraima',
        'SC': 'Santa Catarina',
        'SP': 'São Paulo',
        'SE': 'Sergipe',
        'TO': 'Tocantins'
    }
    if uf.upper() in estados:
        return estados[uf.upper()]
    else:
        return 'UF inválida'