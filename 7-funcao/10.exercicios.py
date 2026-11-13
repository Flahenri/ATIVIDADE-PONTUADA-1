import os
os.system("cls")

print("Função, se o numéro é par ou ímpar.")
numero = int(input("Digite um número inteiro: "))

match numero % 2:
    case 0:
        resultado = "Par"
    case _:
        resultado = "Ímpar"

print(f"\nO número {numero} é {resultado}.")