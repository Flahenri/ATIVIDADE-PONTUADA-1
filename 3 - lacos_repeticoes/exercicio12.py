import os
os.system("cls")

print("=== SOLICITANDO NOTAS ===")
print()
notas = 0
recuperação = 0

for i in range(3):
    notas = float(input("Digite sua Nota: "))
    notas += notas

media_final = notas / 3
if media_final >= 7:
    print("O ALUNO ESTÁ APROVADO!")
if media_final < 7:
    print(" O ALUNO ESTÁ EM RECUPERAÇÂO!")
elif recuperação <= 7:
    print("O ALUNO ESTÁ APROVADO PELA RECUPERAÇÃO!")
recuperação = float(input("Digite quanta notas tu tirou na Recuperação: "))

if recuperação:
    print("ALUNO ESTÁ REPROVADO!")

print(f"O Aluno tirou {recuperação} na recuperação.")
if recuperação > 7:
    print("O ALUNO ESTÁ APROVADO PELA RECUPERAÇÂO!")
else:
    print("O ALUNO NÂO FOI PARA RECUPERAÇÃO!")

print(f"\n Média Final: {media_final}")
print("\nFIM")

