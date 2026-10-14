import os
os.system("cls")

print("= INSERINDO NÚMEROS NO VETOR =")

vetor_numeros = []

for i in range(3):
    numero = int(input("Digite um Número: "))
    vetor_numeros.append(numero)

print("\n =Exibindo números do vetor =")
for valor in vetor_numeros:
    print(f"Valor: {valor}")