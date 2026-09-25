import os
os.system("cls")
import time

print("Número Informado, Escreva.")
numero = int(input("Digite um Número: "))

for i in range(numero, 0, -1):
    print(i)
    time.sleep(1)
print("FIM")

