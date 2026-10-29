import os
import time

lista_serie = []

while True:
    os.system("cls")
    print("=== Conhecimentos ===")
    print("1 - Listar Série,")
    print("2 - Listrar Série.")
    print("3 - Sair.")
    print()
    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("Opção Inválida! Digite apenas número.")
        print("Pressione Enter para continuar....")
        continue
    match opcao:
        case 1:
            print("\n=== Cadastrar Séries ===")
            nome_serie = input("Digite nome da série favorita: ").title()
            if nome_serie == "":
                print("O Nome não pode ficar vazio!.")
            elif nome_serie in lista_serie:
                print(f"{nome_serie}, Sua Série já está cadastrada.")
            else:
                lista_serie.append(nome_serie)
                print("Série Colocada com Sucesso!!!")
            
            input("\nPressione Enter para continuar....")
        case 2:
            print("\n=== Listar Série ===")
            if len(lista_serie) == 0:
                print("O Série está vazio.")
            else:
                for i, serie in enumerate(lista_serie):
                    print(f"{i + 1}. {serie}")
                print(f"\nTotal de Série Favoritado: {len(lista_serie)}")
            input("\nPressione Enter para continuar...")
        case 0:
            print("\nSaindo do programa...")
            time.sleep(1)
            print("Saído com sucesso.")
            break
        case _:
            print("Opção Inválida!")
            input("\nPressione Enter para continuar...")
