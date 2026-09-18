#IMPORTANDO TERMINAIS - COMANDOS.
import os
os.system("cls")
from colorama import Back, Fore, init, Style

#REGISTRO
print(Fore.GREEN + "=" *100 + Style.RESET_ALL)
aluno = input(">>> Digite Seu Nome: ")
idade = input(">>> Digite Sua Idade: ")
print(Fore.GREEN + "=" *100 + Style.RESET_ALL)
print(Fore.GREEN + "\n   ACESSO LIBERADO, CONTINUE" + Style.RESET_ALL)
print("")
print("Calcule sua nota, veja resutaldo a seguir")
print("")

#NOTAS.
nota1 = float(input("Digite Sua Primeira Nota: "))
nota2 = float(input("Digite Sua Segunda Nota: "))
print("")

#MÉDIAS.
media =(nota1 + nota2) /2
print(Fore.MAGENTA + f"Média: {media:.2f}")

#RESULTADOS.
if media >= 6.0:
    print(Fore.GREEN + "Parabéns! Você foi aprovado!")
elif 4.0 <= media <= 5.9:
    print(Fore.YELLOW + "Você está em recuperação.")
else:
    print(Fore.RED + "Aluno reprovado.")