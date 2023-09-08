import re
from validate_docbr import CPF
def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)



def nome_valido(nome):
    if str(nome).isalpha():
        return nome


def rg_valido(rg):
    if len(rg) == 9:
        return rg


def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)

    return  resposta

