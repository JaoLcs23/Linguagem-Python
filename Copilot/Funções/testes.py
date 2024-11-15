from minhas_funcoes import criar_matriz_zeros, multiplicar_matrizes, produto_escalar

def testar_funcoes():
    # Testando criar_matriz_zeros
    matriz_zeros = criar_matriz_zeros(2, 3)
    print("Matriz de zeros 2x3:")
    for linha in matriz_zeros:
        print(linha)

    # Testando multiplicar_matrizes
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    resultado_multiplicacao = multiplicar_matrizes(A, B)
    print("\nMultiplicação das matrizes A e B:")
    for linha in resultado_multiplicacao:
        print(linha)

    # Testando produto_escalar
    C = [1, 2, 3]
    D = [4, 5, 6]
    resultado_produto_escalar = produto_escalar(C, D)
    print("\nProduto escalar de C e D:")
    print(resultado_produto_escalar)

if __name__ == "__main__":
    testar_funcoes()