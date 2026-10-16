import os
from colorama import Fore, Back, Style, init

# Inicializa o colorama
init()

os.system("cls" if os.name == "nt" else "clear")

print("Bem-vindo ao Restaurante Ponto do Sol ☀️\n")

while True:
    
    print(Fore.GREEN + "=" * 43)
    print(" Código     |     Prato      |     Valor   ")
    print("=" * 43)
    print(" 1          |     Picanha    |     25,00 R$")
    print(" 2          |     Lasanha    |     20,00 R$")
    print(" 3          |    Strogonoff  |     18,00 R$")
    print(" 4          | Bife Acebolado |     15,00 R$")
    print(" 5          |   Pão com ovo  |      5,00 R$")
    print("=" * 43 + Style.RESET_ALL)
    print()

    opcao = input("Digite a opção que deseja: ")

    total_conta = 0.0
    cardapio_escolhido = ""
    preco_escolhido = 0.0

    if opcao == "1":
        cardapio_escolhido = "Picanha"
        preco_escolhido = 25.00
    elif opcao == "2":
        cardapio_escolhido = "Lasanha"
        preco_escolhido = 20.00
    elif opcao == "3":
        cardapio_escolhido = "Strogonoff"
        preco_escolhido = 18.00
    elif opcao == "4":
        cardapio_escolhido = "Bife Acebolado"
        preco_escolhido = 15.00
    elif opcao == "5":
        cardapio_escolhido = "Pão com Ovo"
        preco_escolhido = 5.00
    else:
        print(Fore.RED + "\nOpção inválida, tente novamente!\n" + Style.RESET_ALL)
        continue
    total_conta += preco_escolhido
    print(Fore.CYAN + f"\n>>> {cardapio_escolhido} adicionado! (R$ {preco_escolhido:.2f})" + Style.RESET_ALL)
    continuar = input("\nDeseja escolher outro prato? (S/N): ").strip().upper()
    print()

    if continuar != "S":
        break

# Exibe o total final formatado
print(Fore.YELLOW + "=" * 43)
print(f" TOTAL A PAGAR: R$ {total_conta:.2f}".center(43))
print("=" * 43 + Style.RESET_ALL)