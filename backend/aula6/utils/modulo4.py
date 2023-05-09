import re

def valida_cnpj(cnpj):
    regex = r'^(?:(?=\d{14}$)(\d)\1{13}|(\d{2})\.\d{3}\.\d{3}\/\d{4}\-\d{2})$'
    if re.match(regex, cnpj):
        return True
    else:
        return False