#IMPORTANDO TERMINAIS
import os
os.system("cls")

#PREÇOS.
PRECO_ALCOOL = 3.79
PRECO_GASOLINA = 6.59

#ENTRADAS
tipo_combustivel = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ").strip().upper()
litros = float(input("Digite a quantidade de litros vendidos: "))

valor_final = 0.0

if tipo_combustivel == 'A':
    if litros <= 25:
        percentual_desconto = 0.10  # 10%
    else:
        percentual_desconto = 0.20  # 20%
        
    preco_com_desconto = PRECO_ALCOOL * (1 - percentual_desconto)
    valor_final = litros * preco_com_desconto
elif tipo_combustivel == 'G':
    if litros <= 25:
        percentual_desconto = 0.15  # 15%
    else:
        percentual_desconto = 0.30  # 30%
        
    preco_com_desconto = PRECO_GASOLINA * (1 - percentual_desconto)
    valor_final = litros * preco_com_desconto
else:
    print("Tipo de combustível inválido! Use 'A' para Álcool ou 'G' para Gasolina.")
if tipo_combustivel in ['A', 'G']:
    print(f"\nTotal a pagar: R$ {valor_final:.2f}")