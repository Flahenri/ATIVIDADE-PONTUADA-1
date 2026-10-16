import os
os.system("cls")

while True:
    numero = int(input("Digite um Número Entre 1 e 10: "))
    if numero < 1 or numero > 10:
        print()
        print("Número Inválido, Tente Novamente!")
    else:
        print()
        print("Número Está entre 1 e 10.")
        break

print("=== FIM ===")