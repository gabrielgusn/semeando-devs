import re

def valida_cpf(cpf):
    regex = r'^(?:(?=\d{11}$)(\d)\1{10}|[\d]{3}\.[\d]{3}\.[\d]{3}\-[\d]{2})$'
    if re.match(regex, cpf):
        return True
    else:
        return False