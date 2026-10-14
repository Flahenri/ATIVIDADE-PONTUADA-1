import os
os.system("cls")

vetor_notas = []

for quantidades_notas in range(3):
    os.system("cls")
    print("=== CÁLCULO DE NOTAS 📝 ===")
    if vetor_notas:
        print("\nNotas digitadas até agora: ")
        numero = 1
        for nota in vetor_notas:
            print(f"Nota {numero}: {nota}")
            numero += 1
        print("-" * 25)
    nota = float(input(f"\nDigite a {quantidades_notas + 1}ª nota: "))
    vetor_notas.append(nota)
print("=== RESULTADO FINAL 📊 ===")
numero = 1
for nota in vetor_notas:
    print(f"Nota {numero}: {nota}")
    numero += 1
media = sum(vetor_notas) / len(vetor_notas)
print("-" * 25)
print(f"Média final: {media:.1f}")