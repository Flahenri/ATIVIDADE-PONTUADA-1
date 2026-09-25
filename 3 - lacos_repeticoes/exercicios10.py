import os
os.system("cls")

pares = 0
impares = 0

for i in range(5):
    numero = int(input("Digite um Número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\n Quantidade de Pares: {pares}")
print(f"\n Quantidade de Ímpares: {impares}")
print("\nFIM!")