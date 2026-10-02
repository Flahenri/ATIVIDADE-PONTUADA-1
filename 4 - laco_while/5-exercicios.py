import os
os.system("cls")
from colorama import Back, Style, init, Fore
import time

print("=" *53)
print("Cadastre-se: registre seu login e senha para acessar.")
print("=" *53)

login_salvo = input("Digite seu login: ")
senha_salva = input("Digite a sua Senha: ")
print()
print(Fore.GREEN + "Cadastro Realizado com Sucesso!")
print("Redirecionando para tela de carregando" + Style.RESET_ALL)
time.sleep(2)
os.system("cls")

while True:
    print("=== TELA DE ACESSO ===")
    usuario = input("Digite seu login: ")

    if usuario == login_salvo:
        senha = input("Digite a sua senha: ")
    
        if senha == senha_salva:
            print()
            print(Fore.GREEN + "Bem Vindo!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Senha incorreta!")
            input("Pressione Enter para tentar novamente....")
            print("Reiniciando Sistema" + Style.RESET_ALL)
            time.sleep(1.5)
            os.system("cls")
    else:
        print(Fore.YELLOW + "\n Usuário Inválido!" + Style.RESET_ALL)
        input(Fore.RED +"Pressione Enter para tentar novamente....")
        print("Reiniciando o sistema" + Style.RESET_ALL)
        time.sleep(3)
        os.system("cls")

print("\n===FIM ===")