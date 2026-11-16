import os
os.system("cls")

def inflacionar_preco(preco: float) -> float:
    """
    Aumenta o preço em 10% se for menor que 100,
    ou em 20% se for maior ou igual a 100.
    """
    if preco < 100:
        return preco * 1.10
    else:
        return preco * 1.20


try:
    preco_original = float(input("Digite o preço do produto: R$ ").replace(",", "."))
    
    if preco_original < 0:
        print("O preço não pode ser negativo.")
    else:
        novo_preco = inflacionar_preco(preco_original)
        print(f"Preço original: R$ {preco_original:.2f}")
        print(f"Preço inflacionado: R$ {novo_preco:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico.")
    print("Entrada inválida. Por favor, digite um valor numérico.")