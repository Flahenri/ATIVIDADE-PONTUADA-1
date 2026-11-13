import os
os.system("cls")

# Função com parâmetros e com retorno.
def calcular_notas():
    resultado = nota1 + nota2
    return resultado
print("= SOLICITANDO NOTAS =")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Usando a função com parâmetro e
# Inserindop o retorno na varivável soma
soma = calcular_notas(nota1, nota2)

print("= EXIBINDO NOTAS =")
print(f"Soma: {soma}")