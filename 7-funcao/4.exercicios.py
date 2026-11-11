import os
os.system("cls")

def logo_senai():
    print("=" *30)
    print("   SISTEMA SENAI - BAHIA.")
    print("=" *30)

def mostrar_dados(nome, email, telefone):
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Telefone: {telefone}")

print("SOLCITIANDO DADOS")

nome = input("Digite seu nome: ").title()

email = input("Digite seu e-mail: ")

telefone = input("Digite seu telefone: ")

print("\n= EXIBINDO DADOS =")
mostrar_dados(nome, email, telefone)