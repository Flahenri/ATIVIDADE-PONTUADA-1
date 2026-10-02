import os
os.system("cls")

print("=== Solicite as notas ===")

while True:
    nota = int(input("Digite sua Nota: "))
    if nota < 0 or nota > 10:
        print("Nota Inválido, Tentem Novamente.")
    else:
        print(f"A Nota do Aluno é: {nota}")
        break

print("=== FIM ===")
