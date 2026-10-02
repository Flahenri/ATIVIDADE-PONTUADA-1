import os
os.system("cls")
import time

login_salvo = "lucky"
senha_salvo = "123456"
print("Solicite seu Login")
print()
for i in range(3):
    login = input(">>> Digite o login: ")
    senha = input(">>> Digite a senha: ")
    if login == login_salvo and senha == senha_salvo:
        print()
        print("Bem-vindo!")
        break
    else:
        tentativas_restantes = 2 - i
        if tentativas_restantes > 0:
            print(
                f"Login ou senha inválidos. Restam {tentativas_restantes} tentativa(s).\n"
            )
            time.sleep(2.5)
        else:
            print("\nNúmero máximo de tentativas excedido! Acesso bloqueado.")
print()
print("=== FIM ===")























