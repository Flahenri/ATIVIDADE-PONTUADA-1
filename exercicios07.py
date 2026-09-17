#IMPORTANDO TERMINAIS - COMANDOS.
import os
os.system("cls")
from colorama import Back, Fore, init, Style

#PRODUTOS
produto = input("Digite o Nome do Produto: ")
quantidade = int(input("Digite a Quantidade do Produto: "))
preco = float(input("Digite o Preço Unitário: R$"))
print("")

#CÁLCULOS.
total = quantidade * preco

if quantidade <= 5:
    percentual_desconto = 0.02
elif quantidade <= 10:
    percentual_desconto = 0.03
else:
    percentual_desconto = 0.05

desconto = total * percentual_desconto
total_a_pagar = total - desconto

#RESUMO DAS COMPRAS.
print(Fore.GREEN + "   === RESUMO DAS COMPRAS ===  " + Style.RESET_ALL)
print("")
print(Fore. MAGENTA + "Produto: " + Style.RESET_ALL + f"{produto}" )
print(Fore.CYAN + "Quantidade: " + Style.RESET_ALL + f"{quantidade}")
print(Fore.YELLOW + "Preço Unitário: " + Style.RESET_ALL + f"{preco}")
print(Fore.RED + "Preço Total Bruto: " + Style.RESET_ALL + f"{total:.2f}")
print(Fore.BLUE + f"Desconto ({int(percentual_desconto * 100)}%): " + Style.RESET_ALL+ f"R$ {desconto:.2f}")
print(Fore.GREEN + f"Total a Pagar: " + Style.RESET_ALL + f"R$ {total_a_pagar:.2f}")