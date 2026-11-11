import os

def logo_senai():
    os.system("cls")
    print("=" * 30)
    print("   SISTEMA SENAI - BAHIA.")
    print("=" * 30)
def cadastrar_cliente():
    print("\n= SOLICITANDO DADOS =")
    nome = input("Digite seu nome: ").title()
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")
    print("\nCliente cadastrado com sucesso!")
    input("\nPressione ENTER para continuar...")
    return nome, email, telefone
def mostrar_dados(nome, email, telefone):
    print("\n= EXIBINDO DADOS =")
    if nome == "":
        print("Nenhum cliente cadastrado ainda.")
    else:
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"Telefone: {telefone}")
    input("\nPressione ENTER para continuar...")
def menu():
    nome = ""
    email = ""
    telefone = ""
    while True:
        logo_senai()
        print('''
1 - Cadastrar Cliente
2 - Mostrar dados do cliente
3 - Sair
        ''')
        print("=" * 30)
        
        opcao = int(input("Insira uma das opções: "))
        match opcao:
            case 1:
                nome, email, telefone = cadastrar_cliente()
            case 2:
                mostrar_dados(nome, email, telefone)
            case 3:
                print("\nEncerrando o sistema...")
                break
            case _:
                print("\nOpção inválida!")
                input("Pressione ENTER para tentar novamente...")
menu()
