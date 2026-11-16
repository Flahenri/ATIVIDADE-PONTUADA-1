import os
from datetime import date
os.system("cls")


def cadastro_calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    if ano_nascimento > ano_atual:
        return None
    idade = ano_atual - ano_nascimento
    return idade

ano = int(input("Digite o ano de nascimento: "))

idade_usuario = cadastro_calcular_idade(ano)

if idade_usuario is None:
    print("Ano inválido! O ano de nascimento não pode ser maior que o atual.")
else:
    print(f"Você tem (ou completará este ano) {idade_usuario} anos.")