import os
os.system("cls")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: não é possível dividir por zero"
    return a / b

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


print(f"Soma: {somar(num1, num2):.2f}")
print(f"Subtração: {subtrair(num1, num2):.2f}")
print(f"Multiplicação: {multiplicar(num1, num2):.2f}")
print(f"Divisão: {dividir(num1, num2):.2f}")