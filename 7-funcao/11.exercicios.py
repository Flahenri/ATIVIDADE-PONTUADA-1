import os
os.system("cls")

def verificar_numero(valor):
    if valor > 0:
        return "Positivo"
    elif valor < 0:
        return "Negativo"
    else:
        return "Zero (Neutro)"

numero = int(input("Digite um número inteiro: "))

resultado = verificar_numero(numero)
print(f"O número {numero} é {resultado}.")