while True:
    # Lê a ordem da matriz
    N = int(input().strip())
    
    # Verifica se a ordem é zero para encerrar o programa
    if N == 0:
        break
    
    # Inicializa a matriz
    matriz = [[0] * N for _ in range(N)]
    
    # Preenche a matriz de acordo com o padrão
    for i in range(N):
        for j in range(N):
            matriz[i][j] = min(i, j, N - 1 - i, N - 1 - j) + 1
    
    # Imprime a matriz formatada
    for linha in matriz:
        print(" ".join(f"{num:3}" for num in linha))
    print()