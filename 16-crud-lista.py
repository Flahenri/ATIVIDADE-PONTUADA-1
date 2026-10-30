import os

lista_produtos = []

while True:
    os.system("cls")
    print('''
=== MERCADO DENDEIZEIROS ===
1 - Cadastrar
2 - Listar todos os produtos
3 - Atualizar Produto
4 - Remover Produto
5 - Buscar Produto
0 - Sair
''')
    
    opcao = int(input("Digite uma Opção: "))
    
    match  opcao:
        case 1:
            print("=== CADASTRAR PRODUTO ===")
            nome_produto = input("Digite o nome do novo produto: ").strip().upper()
            if nome_produto in lista_produtos:
                print("O Produto já cadastrado.")
            else:
                lista_produtos.append(nome_produto)
                print("Produto cadastrado com sucesso!")
        case 2:
            print("=== PRODUTO NO ESTOQUE ===")
            for produto in lista_produtos:
                print(f"- {produto}")
            print(f"Total: {len(lista_produtos)}")
        case 3:
            print("=== ATUALIZAR PRODUTO ===")
            nome = input("Qual produto deseja atualizar? ")
            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input("Novo Nome: ")
                lista_produtos[posicao] = novo
                print("Produto alterado com sucesso!")
            else:
                print("Produto não encontrado.")
        case 4:
            print("=== REMOVER PRODUTO ===")
            nome = input("Qual produto deseja remover?: ")
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print("Produto excluído com sucesso!")
            else:
                print("Produto não encontrado.")
        case 5:
            print("\n=== EXIBINDO PRODUTO ===")
            nome = input("Qual Produto deseja buscar? ")
            if nome in lista_produtos:
                print("Produto Encontrado!")
            else:
                print("Este Produto não está no estoque.")
        case 0:
            print("Saindo do programa...")
            break
        case _:
            print("Opção Inválida Tente Novamente")
        
    input("Pressione Enter para continuar...")
