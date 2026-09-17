#IMPORTANDO TERMINAIS.
import os
os.system("CLS")
from colorama import Back, Fore, init, Style

#MERCADO
print("Mercadinho das Frutas")
print("Preço logo a abaixo")
print("-" *50)
print(Fore.GREEN + "   FRUTA   | ATÉ 5KG        | ACIMA DE 5KG"   + Style.RESET_ALL)
print(Fore.RED + "   Morango" + Style.RESET_ALL + " | R$ 2,50 por Kg | R$ 2,20 por Kg")
print(Fore.RED + "   Maça    " + Style.RESET_ALL + "| R$ 1,80 por Kg | R$ 1,50 por Kg")
print("-" *50)
kg_morango = float(input("Digite a Quantidade (em Kg) de Morangos: "))
kg_maca = float(input("Digite a Quantidade (em Kg) de Maçãs: "))
print("")

#CÁLCULANDO O MORANGO.
if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

#CÁLCULANDO A MAÇAS.
if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

#TOTAL DOS KILOS
total_kg = kg_morango + kg_maca
valor_total = preco_morango + preco_maca

#RESULTADO.
if total_kg > 8 or valor_total > 25.00:
    valor_total = valor_total * 0.90
print("Valor final a ser pago pelo cliente: " + Fore.GREEN +  f"R$ {valor_total:.2f} " + Style.RESET_ALL)