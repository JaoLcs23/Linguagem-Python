while True:
    # Lê os valores de M e N
    M, N = map(int, input().strip().split())
    
    # Verifica se algum dos valores é menor ou igual a zero para encerrar o programa
    if M <= 0 or N <= 0:
        break
    
    # Garante que M seja menor que N
    if M > N:
        M, N = N, M
    
    # Calcula a sequência e a soma dos valores entre M e N
    sequencia = list(range(M, N + 1))
    soma = sum(sequencia)
    
    # Imprime a sequência e a soma
    print(" ".join(map(str, sequencia)), f"Sum={soma}")