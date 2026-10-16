import os
os.system("cls")

print("= INSERINDO NÚMEROS DO VETOR =")

vetor_numeros = []
quantidade = 5

for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1}º Números: "))
    if numero < 0:
        numero = 0
    vetor_numeros.append(numero)
print("\n === Valores do Vetor ===")
posicao = 0
for numero in vetor_numeros:
    print(f"Poisção: {posicao} - {numero}")
    posicao += 1