import os
os.system("cls")

soma = 0
quantidade_notas = 2

for i in range(2):
    while True:
        nota = float(input(f"Digite o {i+1} nota entre 0 e 10: "))

        if nota < 0 or nota > 10:
            print("\n Nota Inválida, Tente Novamente.")
        else:
            soma = soma + nota
            break

media = soma / quantidade_notas

print(f"\nMédia: {media:.2f}")
print("=== FIM ===")