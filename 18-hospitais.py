import os

pacientes = []

while True:
    os.system("cls")
    print('''
=== HOSPITAL REGIONAL ===

1 - Cadastrar Pacientes
2 - Listar Pacientes
3 - Atualizar Pacientes
4 - Excluir Pacientes
0 - Sair
''')
    
    opcao = int(input("Digite uma das opções: "))
    
    match opcao:
        case 1:
            print("\n=== CADASTRAR PACIENTE ===")
            nome = input("Digite o Nome do paciente: ").title()
            sobrenome = input("Digite o Sobrenome do paciente: ").title()
            paciente_completo = f"{nome} {sobrenome}"
            pacientes.append(paciente_completo)
            print("Paciente cadastrado!")
            input("\nPressione Enter para continuar...")
        case 2:
            print("\n=== LISTAR PACIENTES ===")
            for indice, paciente in enumerate(pacientes, 1):
                print(f"{indice}. {paciente}")
            
            input("\nPressione Enter para continuar...")
        case 3:
            print("\n=== ATUALIZAR PACIENTE ===")
            nome_busca = input("Qual Paciente deseja atualizar (Digite o nome completo): ").title()
            
            if nome_busca in pacientes:
                posicao = pacientes.index(nome_busca)
                
                novo_nome = input("Digite o novo Nome: ").title()
                novo_sobrenome = input("Digite o novo Sobrenome: ").title()
                
                pacientes[posicao] = f"{novo_nome} {novo_sobrenome}"
                print("Paciente Atualizado com Sucesso!")
            else:
                print("Paciente não encontrado!")
            
            input("\nPressione Enter para continuar...")
        case 4:
            print("\n=== EXCLUIR PACIENTE ===")
            nome_excluir = input("Qual Paciente deseja excluir (Digite o nome completo): ").title()
            
            if nome_excluir in pacientes:
                pacientes.remove(nome_excluir)
                print("Paciente excluído com sucesso!")
            else:
                print("Paciente não encontrado!")
            
            input("\nPressione Enter para continuar...")
        case 0:
            print("Saindo...")
            break