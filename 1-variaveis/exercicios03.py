#IMPORTANDO TERMINAIS.
import os
os.system("cls")

#ENTRADA.
A = int(input("DIGITE O NÚMERO A: "))
B = int(input("DIGITE O NÚMERO B: "))

#CÁLCULOS.
if A == B:
    C = A + B
else:
    C = A * B
    print(f"O resultado armazenado na variável C é: {C}")