#IMPORTANDO TERMINAIS - COMANDOS.
import os
os.system("cls")
from colorama import Back, Fore, init, Style

#ENTRADAS.
print("Bem-vindo à Loja de CDs. Escolha a cor de sua preferência.")
print("")
print(" COR        | PREÇO ")
print(Fore.GREEN + "CD VERDE  " + Style.RESET_ALL + "  | R$ 10,00 ")
print(Fore.BLUE + "CD AZUL  " + Style.RESET_ALL + "   | R$ 20,00")
print(Fore.YELLOW + "CD AMARELO  " + Style.RESET_ALL + "| R$ 30,00")
print(Fore.RED + "CD VERMELHO " + Style.RESET_ALL + "| R$ 40,00")
print("")
cor = input("Digite a cor do CD (Verde, Azul, Amarelo ou Vermelho): ").strip().lower()
print("")

#SAÍDA
if cor == "verde":
    preco = 10.00
elif cor == "azul":
    preco = 20.00
elif cor == "amarelo":
    preco = 30.00
elif cor == "vermelho":
    preco = 40.00
else:
    preco = None

#RESULTADOS.
if preco is not None:
    print(f"O Preço do CD de cor {cor.capitalize()} é: R$ {preco:.2f}")
else:
    print("Cor inválida! Por favor, escolha entre Verde, Azul, Amarelo ou Vermelho.")