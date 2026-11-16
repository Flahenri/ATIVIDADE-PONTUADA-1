import os
os.system("cls")

quantidade_numerica = 3
notas = []

def calcular_notas(lista_notas):
    return sum(lista_notas) / len(lista_notas)

def mostrar_resultado(lista_notas):
    for nota in lista_notas:
        print(f"Nota: {nota}")
    print(f"Média: {media}")

quantidade_numerica = 3
lista_notas = []

for i in range(quantidade_numerica):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

media = calcular_notas(lista_notas)

mostrar_resultado(media)