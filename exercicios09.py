#IMPORTANDO TERMINAIS.
import os
os.system("cls")

#ENTRADAS.
renda_mensal = float(input("Informe a renda mensal do solicitante (R$): "))
valor_emprestimo = float(input("Informe o valor total do empréstimo solicitado (R$): "))
num_parcelas = int(input("Informe o número de prestações desejado: "))

#CÁLCULOS.
limite_emprestimo_total = renda_mensal * 10
valor_parcela = valor_emprestimo / num_parcelas
limite_parcela_maxima = renda_mensal * 0.30

emprestimo_valido = valor_emprestimo <= limite_emprestimo_total
parcela_valida = valor_parcela <= limite_parcela_maxima

#RESULTADOS.
print("\n--- Resultado da Análise ---")
if emprestimo_valido and parcela_valida:
    print("Empréstimo CONCEDIDO!")
else:
    print("Empréstimo NEGADO.")
    print("Motivo(s):")
    if not emprestimo_valido:
        print(f"- O valor solicitado (R$ {valor_emprestimo:.2f}) excede o limite de 10x a renda (R$ {limite_emprestimo_total:.2f}).")
    if not parcela_valida:
        print(f"- A parcela (R$ {valor_parcela:.2f}) excede 30% da renda mensal (R$ {limite_parcela_maxima:.2f}).")