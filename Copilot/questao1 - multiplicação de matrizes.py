def multiplicar_matrizes(A, B):
    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]
    
    return resultado

if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    
    resultado = multiplicar_matrizes(A, B)
    
    for linha in resultado:
        print(linha)