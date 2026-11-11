import os
os.system("cls")

def mostrar_tabuada(numero):
    print(f"\n= TABUADA do {numero} = ")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

while True:
    numero = int(input("Digite um número para ver a tabuada: "))
    if 1 <= numero <= 10:
        break
    else:
        print("Número inválido! ")

mostrar_tabuada(numero)
