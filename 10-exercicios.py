import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

qtd_pessoas = 0
soma_salario = 0.0
qtd_mulheres_salario_alto = 0

maior_idade = None
menor_idade = None

limpar_tela()

while True:
    print("=" * 38)
    print("         PESQUISA REGIONAL          ")
    print("=" * 38)
    print(" Código | Descrição")
    print("    1   | Adicionar pessoa")
    print("    2   | Exibir resultados")
    print("    3   | Sair")
    print("=" * 38)

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        limpar_tela()
        print("--- CADASTRO DE PESSOA ---")
        
        while True:
            try:
                idade = int(input("Digite a idade: "))
                if idade >= 0:
                    break
                print("Idade não pode ser negativa.")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")

        while True:
            sexo = input("Digite o sexo (M/F): ").strip().upper()
            if sexo in ["M", "F"]:
                break
            print("Sexo inválido! Digite apenas 'M' ou 'F'.")

        while True:
            try:
                salario = float(input("Digite o salário (R$): "))
                if salario >= 0:
                    break
                print("Salário não pode ser negativo.")
            except ValueError:
                print("Entrada inválida! Digite um valor numérico.")

        qtd_pessoas += 1
        soma_salario += salario

        if maior_idade is None or idade > maior_idade:
            maior_idade = idade

        if menor_idade is None or idade < menor_idade:
            menor_idade = idade

        if sexo == "F" and salario >= 5000.0:
            qtd_mulheres_salario_alto += 1

        limpar_tela()
        print(">> Pessoa adicionada com sucesso!\n")

    elif opcao == "2":
        limpar_tela()
        print("=" * 45)
        print("         RESULTADOS DA PESQUISA             ")
        print("=" * 45)

        if qtd_pessoas > 0:
            media_salario = soma_salario / qtd_pessoas
            print(f"a) Média de salário do grupo : R$ {media_salario:.2f}")
            print(f"b) Maior idade do grupo       : {maior_idade} anos")
            print(f"   Menor idade do grupo       : {menor_idade} anos")
            print(f"c) Mulheres com salário >= 5k : {qtd_mulheres_salario_alto}")
        else:
            print("Nenhuma pessoa foi cadastrada ainda.")

        print("=" * 45 + "\n")

    elif opcao == "3":
        limpar_tela()
        print("Programa encerrado.")
        break

    else:
        limpar_tela()
        print("Opção inválida! Escolha 1, 2 ou 3.\n")