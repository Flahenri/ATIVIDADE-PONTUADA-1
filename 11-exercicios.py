import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

total_familias = 0
soma_salario = 0.0
total_filhos = 0

maior_salario = None

limpar_tela()

while True:
    print("=" * 38)
    print("      PESQUISA DE HABITANTES        ")
    print("=" * 38)
    print(" Código | Descrição")
    print("    1   | Adicionar família")
    print("    2   | Sair e exibir resultados")
    print("=" * 38)

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        limpar_tela()
        print("--- CADASTRO DE FAMÍLIA ---")

        while True:
            try:
                salario = float(input("Digite o salário da família (R$): "))
                if salario >= 0:
                    break
                print("O salário não pode ser negativo.")
            except ValueError:
                print("Entrada inválida! Digite um valor numérico.")

        while True:
            try:
                filhos = int(input("Digite o número de filhos: "))
                if filhos >= 0:
                    break
                print("O número de filhos não pode ser negativo.")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")

        total_familias += 1
        soma_salario += salario
        total_filhos += filhos

        if maior_salario is None or salario > maior_salario:
            maior_salario = salario

        if menor_salario is None or salario < menor_salario:
            menor_salario = salario

        limpar_tela()
        print(">> Família cadastrada com sucesso!\n")

    elif opcao == "2":
        limpar_tela()
        print("=" * 45)
        print("       RESULTADOS DA PESQUISA DE HABITANTES  ")
        print("=" * 45)

        if total_familias > 0:
            media_salario = soma_salario / total_familias
            media_filhos = total_filhos / total_familias

            print(f"a) Total de famílias pesquisadas : {total_familias}")
            print(f"b) Média de salário da população : R$ {media_salario:.2f}")
            print(f"c) Média do número de filhos    : {media_filhos:.2f}")
            print(f"d) Maior salário encontrado      : R$ {maior_salario:.2f}")
            print(f"e) Menor salário encontrado      : R$ {menor_salario:.2f}")
        else:
            print("Nenhuma família foi cadastrada.")

        print("=" * 45)
        break

    else:
        limpar_tela()
        print("Opção inválida! Digite 1 ou 2.\n")