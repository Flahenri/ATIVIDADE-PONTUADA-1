import os
os.system("cls")

def cabecalho():
    print("="*25)
    print("\t SENAI")
    print("="*25)

cabecalho()
nome = input("Digite seu nome: ")

cabecalho()
idade = int(input("Digite sua idade: "))

cabecalho()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
