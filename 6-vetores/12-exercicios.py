import os
os.system("cls")


cardapio = {
    1: ("Picanha", 25.00),
    2: ("Lasanha", 40.00),
    3: ("Strogonoff", 18.00),
    4: ("Bife Acebolado", 15.00),
    5: ("Pão com Ovo", 5.00)
}

pedidos = []
continuar = "s"

while continuar == "s":
    print("\n===== CARDÁPIO DO RESTAURANTE =====")
    for codigo, (prato, valor) in cardapio.items():
        print(f"{codigo} - {prato}: R$ {valor:.2f}")
    escolha = int(input("\nDigite o número do prato desejado: "))
    if escolha in cardapio:
        prato, valor = cardapio[escolha]
        pedidos.append((prato, valor))
        print(f"\nVocê escolheu: {prato} - R$ {valor:.2f}")
    else:
        print("\nOpção inválida! Escolha um número do cardápio.")
        continue
    continuar = input("\nDeseja escolher outro prato? (s/n): ").lower()
print("\n===== RESUMO DO PEDIDO =====")
total = 0
for prato, valor in pedidos:
    print(f"{prato}: R$ {valor:.2f}")
    total += valor
print("-----------------------------")
print(f"VALOR TOTAL DA CONTA: R$ {total:.2f}")
print("Obrigado pela preferência!")
