#IMPORTANDO SISTEMAIS.
import os
os.system("cls")

#CÁLCULOS.
A = int(input("DIGITE O NÚMERO (A): "))
B = int(input("DIGITE O NÚMERO (B): "))
C = int(input("DIGITE O NÚMERO (C): "))

#CÁLCULANDO.
match (A +B ):
    case soma if soma < C:
        print("A SOMA DE (A + B) É MENOR QUE C")
    case soma if soma > C:
        print("A SOMA DE (A + B) É MAIOR QUE C")
    case _:
        print("INVÁLIDO")