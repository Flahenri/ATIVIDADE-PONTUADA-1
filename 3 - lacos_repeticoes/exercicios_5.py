#IMPORTANDO TERMINAIS - COMANDOS.
import os
os.system("cls")
import time

#ENTRADA.
soma = 0
for i in range(5):
    numero = int(input(f"Digite o {i+1}º Número Inteiro: "))
    soma += numero

print(f"\nA Soma de todos os números é: {soma}")
print("\nFIM")

