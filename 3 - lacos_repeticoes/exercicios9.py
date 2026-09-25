import os
os.system("cls")

print("ACUMULANDO VALORES EM UMA VARIÁVEL.")
soma = 0

print(f"Valor INICIAL da Variável Soma: {soma}")

for i in range(3):
    numero = int(input("Digite um Número para Somar: "))
    soma = soma + numero
    print(f"Valor TEMPORÁRIO da Variável Soma: {soma}")
print(f"\n Valor Final da Variável Soma: {soma}")
