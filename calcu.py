import os

os.system("cls")

quantidade_notas = 4
notas = []

print("= Solicitando notas =")
for i in range(quantidade_notas):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

soma = sum(notas)
media = soma / quantidade_notas

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print("\n= Resultado Final =")
print(f"Notas informadas: {notas}")
print(f"Média: {media:.2f}")
print(f"Situação: {resultado}")
