import os
os.system("cls")

print("=== Solicite suas Notas ===")
print()

soma_notas = 0.0
quantidade_notas = 2

for i in range(1, quantidade_notas + 1):
    while True:
        nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
        
        if 0 <= nota <= 10:
            soma_notas += nota
            break
        else:
            print("Nota inválida! A nota deve estar entre 0 e 10. Tente novamente.\n")
            
media = soma_notas / quantidade_notas

print("\n------------------------------")
print(f"A Média do Aluno é: {media:.2f}")
print("------------------------------")


