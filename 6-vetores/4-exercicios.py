import os
os.system("cls")

vetor_livros = []

for i in range(6):
    print("=== ESCOLHA UM LIVRO 📖 ===")
    if vetor_livros:
        print("\nLivros adicionados até agora:")
        for idx, livro in enumerate(vetor_livros, 1):
            print(f"{idx}. {livro}")
        print("-" * 30)
    livro = input(f"\nDigite o nome do {i + 1}º livro: ")
    vetor_livros.append(livro)
os.system("cls")
print("=== LISTA FINAL DE LIVROS 📚 ===")
for idx, livro in enumerate(vetor_livros, 1):
    print(f"{idx}. {livro}")