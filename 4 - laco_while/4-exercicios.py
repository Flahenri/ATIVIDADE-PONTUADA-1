import os

os.system("cls")

print("Solicite suas notas")

nota1 = float(input("Digite sua primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print("Nota inválida! A nota deve ser entre 0 e 10.")
    nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

while nota2 < 0 or nota2 > 10:
    print("Nota inválida! A nota deve ser entre 0 e 10.")
    nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

print(f"\nSua média é: {media:.2f}")