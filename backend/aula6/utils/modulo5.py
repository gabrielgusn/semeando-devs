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