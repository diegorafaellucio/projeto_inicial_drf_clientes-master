def cpf_valido(self, cpf):
    if len(cpf) == 11:
        return cpf


def nome_valido(self, nome):
    if str(nome).isalpha():
        return nome
    else:
        raise serializers.ValidationError("Não inclua numeros nesse campo!")


def validate_cpf(self, rg):
    if len(rg) != 9:
        raise serializers.ValidationError("O RG deve ter  9 Digitos!")
    else:
        return rg


def validate_celular(self, celular):
    if len(celular) != 11:
        raise serializers.ValidationError("O Celular deve ter  11 Digitos!")
    else:
        return celular