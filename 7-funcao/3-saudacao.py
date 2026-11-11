import os
os.system("cls")

def mostrar_saudacao(nome, idade):
    print(f"{nome} tem {idade} anos.")
    
print("= Solicitando dados =")
nome = input("Digite seu nome: ").title()
idade = int(input("Digite sua idade: "))

print("\n= Exibindo dados =")
mostrar_saudacao(nome, idade)
