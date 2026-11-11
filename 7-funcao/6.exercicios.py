import os
os.system("cls")

lista_produtos = []
quantidade_numerica = 3

def mostrar_dados(lista_produtos):
    for i in range(quantidade_numerica):
        print(f"{i+1} - {lista_produtos[1]} ")

print("= SOLICITANDO DADOS =")
for i in range(3):
    produto = input("Digite o nome do produto: ")
    lista_produtos.append(produto)

print("\n= EXIBINDO DADOS =")
mostrar_dados(lista_produtos)