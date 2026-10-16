import os
os.system("cls")

qtd_pares = 0
qtd_impares = 0
qtd_total = 0

soma_pares = 0
soma_total = 0

while True:
    try:
        numero = int(input("Digite um número inteiro positivo (0 para encerrar): "))

        if numero == 0:
            break
        if numero < 0:
            print("Apenas números positivos são aceitos. Tente novamente.\n")
            continue

        qtd_total += 1
        soma_total += numero
        if numero % 2 == 0:
            qtd_pares += 1
            soma_pares += numero
        else:
            qtd_impares += 1

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.\n")

print("\n" + "=" * 40)
print("            RESULTADO FINAL             ")
print("=" * 40)
print(f" Quantidade de números pares  : {qtd_pares}")
print(f" Quantidade de números ímpares: {qtd_impares}")

# Média dos pares
if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
    print(f" Média dos valores pares      : {media_pares:.2f}")
else:
    print(" Média dos valores pares      : Nenhum número par digitado")

# Média geral
if qtd_total > 0:
    media_geral = soma_total / qtd_total
    print(f" Média geral dos números lidos: {media_geral:.2f}")
else:
    print(" Média geral                  : Nenhum número digitado")

print("=" * 40)