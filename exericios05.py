#IMPORTANDO TERMINAIS.
import os
os.system("cls")

#CÁLCULOS.
operacao = input("Digite a Operação (+, -, *, /): ").strip()
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

#CÁLCULANDO.
if operacao == '+':
    resultado = A + B
elif operacao == '-':
    resultado = A - B
elif operacao == '*':
    resultado = A * B
elif operacao == '/':
    if B != 0:
        resultado = A / B
    else:
        print("Erro: Não é possível dividir por zero!")
        erro = True
else:
    print("Erro: Operação inválida!")
    erro = True

resultado = 0
erro = False

#RESULTADO.
if not erro:
    print(f"Resultado: {A} {operacao} {B} = {resultado}")

