def criar_matriz_zeros(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]

def multiplicar_matrizes(A, B):
    linhas_A, colunas_A = len(A), len(A[0])
    linhas_B, colunas_B = len(B), len(B[0])
    
    if colunas_A != linhas_B:
        raise ValueError("O número de colunas de A deve ser igual ao número de linhas de B.")
    
    C = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]
    
    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                C[i][j] += A[i][k] * B[k][j]
                
    return C

def produto_escalar(C, D):
    if len(C) != len(D):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    
    return sum(c * d for c, d in zip(C, D))