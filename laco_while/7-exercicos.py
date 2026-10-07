import os
os.system("cls")

soma_notas = 0.0
contador = 0

while True:
    try:
        contador += 1
        
        nota = float(input(f"Digite a {contador}ª nota: "))
        soma_notas += nota
        
        resposta = input("Deseja inserir mais uma nota? (S/N): ").strip().upper()
        print()
        
        if resposta == "N":
            break

    except ValueError:
        print("Entrada inválida! Digite apenas números.\n")
        contador -= 1 
if contador > 0:
    media = soma_notas / contador
    print("=" * 38)
    print(f" Total de notas inseridas: {contador}")
    print(f" Média aritmética: {media:.2f}")
    print("=" * 38)