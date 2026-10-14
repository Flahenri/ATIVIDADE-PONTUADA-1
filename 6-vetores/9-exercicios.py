import os
os.system("cls")

print("=== Inserindo Números no vetor ===")
vetor_numeros = []

for i in range(6):
    numero = int(input(f"Digite o {i+1} Número: "))
    vetor_numeros.append(numero)

print("\n=== Exibindo Números ===")
for indice, numero in enumerate(vetor_numeros, start=1):
    print(f"{indice} Número: {numero}")

pares = 0
impares = 0

for numero in vetor_numeros:
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")