import os
os.system("cls")

vetor = []
quantidade = 5
qtd_negativos = 0
soma_positivos = 0

print("Digite 5 números: ")
for i in range(quantidade):
    numero = float(input(f"Digite o {i + 1}º número: "))
    vetor.append(numero)
for numero in vetor:
    if numero < 0:
        qtd_negativos += 1
    elif numero > 0:
        soma_positivos += numero
print("\n=== Resultados ===")
print(f"Vetor digitado: {vetor}")
print(f"Quantidade de números negativos: {qtd_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")
