import os
import time

lista_produtos = []

while True:
    os.system("cls")
    print("=== MERCADINHO DENDEZEIROS ===")
    print()
    print("1 - Cadastrar Produtos")
    print("2 - Listar Produtos")
    print("0 - Sair")
    print()
    try:
        opcao = int(input(">>> Digite uma opção: "))
    except ValueError:
        print("Opção inválida! Digite apenas números.")
        input("Pressione Enter para continuar...")
        continue
    match opcao:
        case 1:
            print("\n=== Cadastrar Produtos ===")
            nome = input("Nome do novo Produto: ").strip().upper()
            
            if nome == "":
                print("O nome não pode ficar vazio.")
            elif nome in lista_produtos:
                print(f"{nome} já está cadastrado.")
            else:
                lista_produtos.append(nome)
                print("Produto cadastrado com sucesso!")
            
            input("\nPressione Enter para continuar...")
        case 2:
            print("\n=== Listar Produtos ===")
            if len(lista_produtos) == 0:
                print("O estoque está vazio.")
            else:
                for i, produto in enumerate(lista_produtos):
                    print(f"{i + 1}. {produto}")
                print(f"\nTotal de Produtos: {len(lista_produtos)}")
            input("\nPressione Enter para continuar...")
        case 0:
            print("\nSaindo do programa...")
            time.sleep(1)
            print("Saído com sucesso.")
            break
        case _:
            print("Opção Inválida!")
            input("\nPressione Enter para continuar...")