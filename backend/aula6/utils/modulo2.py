import re

def cep_valido(cep):
    padrao = r'^\d{5}-\d{3}$'
    if re.match(padrao, cep):
        return True
    else:
        return False
    