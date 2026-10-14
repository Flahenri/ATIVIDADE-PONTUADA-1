import os
os.system("cls" if os.name == "nt" else "clear")

vetor_notas = []
quantidades_de_notas = 4
print("= Digite as Notas. =")

for i in range(quantidades_de_notas):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    vetor_notas.append(nota)

print("\n= Exibindo as Notas =")
for indice, numero in enumerate(vetor_notas, start=1):
    print(f"{indice}ª Nota: {numero:.1f}")

soma = sum(vetor_notas)
media = soma / quantidades_de_notas

print(f"\nMédia final: {media:.1f}")
print("= Situação do aluno =")

if media >= 7.0:
    print("Aluno Aprovado!!!")
elif media >= 5.0:
    print("Aluno em Recuperação")
else:
    print("Aluno Reprovado.")
