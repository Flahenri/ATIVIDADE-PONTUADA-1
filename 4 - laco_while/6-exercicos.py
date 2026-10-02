import os
os.system("cls")

soma = 0
quantidade_notas = 3
print("=" *60)
print("Calcule suas notas e veja o resultado total das suas médias.")
print("=" *60)

for i in range(quantidade_notas):
    nota = float(input(f"Digite a {i + 1}ª nota do seu boletim: "))
    soma += nota

media = soma / quantidade_notas

print(f"\nMédia final: {media:.2f}")
if media >= 7.0:
    print("Situação: Aprovado!")
elif media >= 5.0:
    print("Situação: Em recuperação.")
else:
    print("Situação: Reprovado.")