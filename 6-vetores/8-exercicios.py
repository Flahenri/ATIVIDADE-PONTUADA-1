import os
os.system("cls")

print("= inserindo números no vetor =")
vetor_numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}, o número: "))
    vetor_numeros.append(numero)

print("\n= Exibindo números =")
for indice, numero in enumerate(vetor_numeros, start=1):
    print(f"{indice}, o número é: {numero}")

maior_numero = max(vetor_numeros)
menor_numero = min(vetor_numeros)

print(f"Maior Número é: {maior_numero}")
print(f"Menor Número é: {menor_numero}")