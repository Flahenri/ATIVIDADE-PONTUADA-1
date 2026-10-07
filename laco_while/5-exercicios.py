import os
os.system("cls")
from colorama import init, Fore, Back, Style

def ler_nota_valida(numero_nota):
    while True:
        try:
            nota = float(input(f"Digite a {numero_nota}ª nota (entre 0 e 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print(Fore.RED + "Nota inválida! A nota deve estar entre 0 e 10. Tente novamente." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Entrada inválida! Por favor, digite um número válido." + Style.RESET_ALL)

nota1 = ler_nota_valida(1)
nota2 = ler_nota_valida(2)
nota3 = ler_nota_valida(3)

media = (nota1 + nota2 + nota3) / 3

print(f"\nMédia final: {media:.2f}")

if media >= 7.0:
    print("Situação:", Fore.GREEN + "APROVADO" + Style.RESET_ALL)
elif media >= 5.0:
    print("Situação:", Fore.YELLOW + "RECUPERAÇÃO" + Style.RESET_ALL)
else:
    print("Situação:", Fore.RED + "REPROVADO" + Style.RESET_ALL)
