import os
os.system("cls")


soma = 0
contador = 0

while True:
    try:
        valor = int(input("Digite um número inteiro positivo (ou negativo para encerrar): "))
        
        if valor < 0:
            break
            
        soma += valor
        contador += 1

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.\n")
print()
if contador > 0:
    media = soma / contador
    print("=" * 38)
    print(f" Total de números informados: {contador}")
    print(f" Média aritmética: {media:.2f}")
    print("=" * 38)
else:
    print("Nenhum número positivo foi informado.")