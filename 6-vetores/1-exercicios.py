# EXEMPLO.

import os
os.system("cls")

print("= INSERINDO NÚMEROS NO VETOR =")

vetor_numeros = []

numero = int(input("Digite um Número: "))
vetor_numeros.append(numero)
numero = int(input("Digite um Número: "))
vetor_numeros.append(numero)
numero = int(input("Digite um Número: "))
vetor_numeros.append(numero)

print("\n= Exibindo números do vetor =")
print(f"Primeira posição do vetor: {vetor_numeros[0]}")
print(f"Útlima posição do vetor: {vetor_numeros[2]}")