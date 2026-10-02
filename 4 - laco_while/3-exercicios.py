import os
os.system("cls")

print("=" * 30)
print("  Mercadinho do seu Antônio")
print("=" * 30)
print()
while True:
    print("1 - 🍌 Banana (1Kilo) 5$")
    print("2 - 🍎 Maça (1Kilo) 5$")
    print("3 - 🥭 Manga (1Kilo) 8$")
    print("4 - 🥜 Caju (1Kilo) 3$")
    print("5 - 🍇 Uva (1kilo) 5$")
    break
print()

opcao = input("Digite a opção escolhida: ")

item_escolhido = ""
preco_escolhido = 0.0

if opcao == "1":
    item_escolhido = "Banana"
    preco_escolhido = 5.00
elif opcao == "2":
    item_escolhido = "Maça"
    preco_escolhido = 5.00
elif opcao == "3":
    item_escolhido = "Manga"
    preco_escolhido = 8.00
elif opcao == "4":
    item_escolhido = "Caju"
    preco_escolhido = 3.00
elif opcao == "5":
    item_escolhido = "Uva"
    preco_escolhido = 5.00
else:
    print("Opção inválida!")

if item_escolhido != "":
    print(f"Você escolheu {item_escolhido} - R$ {preco_escolhido:.2f}")