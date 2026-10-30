import os

jogadores = []

while True:
    os.system("cls")
    print('''
=== GERENCIADOR DE JOGADORES ===

1 - Cadastrar jogador
2 - Listar jogadores
3 - Atualizar jogador
4 - Excluir jogador
0 - Sair
''')

    opcao = int(input("Opção: "))
    match opcao:
        case 1:
            print("\n=== CADASTRAR JOGADOR ===")
            nome = input("Nome: ").strip().title()
            posicao = input("Posição: ").strip().title()
            camisa = input("Camisa: ").strip()
            jogador_formatado = f"{nome} | {posicao} | #{camisa}"
            jogadores.append(jogador_formatado)
            
            print("Jogador cadastrado!")
            input("\nPressione Enter para continuar...")

        case 2:
            print("\n=== LISTAR JOGADORES ===")
            if not jogadores:
                print("Nenhum jogador cadastrado.")
            else:
                for indice, jogador in enumerate(jogadores, 1):
                    print(f"{indice}. {jogador}")
            
            input("\nPressione Enter para continuar...")

        case 3:
            print("\n=== ATUALIZAR JOGADOR ===")
            if not jogadores:
                print("Nenhum jogador cadastrado para atualizar.")
            else:
                for indice, jogador in enumerate(jogadores, 1):
                    print(f"{indice}. {jogador}")
                
                num = int(input("\nDigite o número do jogador que deseja atualizar: ")) - 1
                
                if 0 <= num < len(jogadores):
                    novo_nome = input("Novo Nome: ").strip().title()
                    nova_posicao = input("Nova Posição: ").strip().title()
                    nova_camisa = input("Nova Camisa: ").strip()
                    
                    jogadores[num] = f"{novo_nome} | {nova_posicao} | #{nova_camisa}"
                    print("Jogador atualizado com sucesso!")
                else:
                    print("Número inválido!")
            
            input("\nPressione Enter para continuar...")

        case 4:
            print("\n=== EXCLUIR JOGADOR ===")
            if not jogadores:
                print("Nenhum jogador cadastrado para excluir.")
            else:
                for indice, jogador in enumerate(jogadores, 1):
                    print(f"{indice}. {jogador}")
                
                num = int(input("\nDigite o número do jogador que deseja excluir: ")) - 1
                
                if 0 <= num < len(jogadores):
                    removido = jogadores.pop(num)
                    print("Jogador excluído com sucesso!")
                else:
                    print("Número inválido!")
            
            input("\nPressione Enter para continuar...")

        case 0:
            print("Saindo...")
            break