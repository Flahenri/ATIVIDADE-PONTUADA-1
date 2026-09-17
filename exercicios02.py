#IMPORTANDO TERMINAIS - COMANDOS.
import os
os.system("cls")
from colorama import Back, Fore, init, Style

#REGISTRO
nome = input("Digite Seu Nome: ")
sexo = input("Digite Seu Gênero " + Fore.BLUE + "(M) " + Style.RESET_ALL + "ou " + Fore.MAGENTA + "(F)" + Style.RESET_ALL + ": ").strip().upper()
estado_civil = input("Digite Seu Estado Civil, (Solteiro), (Casado(a), (Divorciado) : ")

if estado_civil == "Casado" or estado_civil == "Casada":
    tempo_de_casamento = input("Quanto tempo de casamento?: ")
    print(f"que legal {tempo_de_casamento}, muitos anos de felicidade Sr(a),{nome}!")
else:
    print("Obrigado Pela Informações")