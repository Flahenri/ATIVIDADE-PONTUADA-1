import os

os.system("cls")

quantidade_numerica = 4
notas = []

def solicitar_notas():
    print("= Solicitando notas =")
    for i in range(quantidade_numerica):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)

solicitar_notas()

soma = sum(notas)
media = soma / quantidade_numerica

match media:
    case _ if media >= 7:
        resultado = "Aprovado"
    case _ if media >= 5:
        resultado = "Recuperação"
    case _:
        resultado = "Reprovado"

print("\n= Resultado Final =")
print(f"Notas informadas: {notas}")
print(f"Média: {media:.2f}")
print(f"Situação: {resultado}")