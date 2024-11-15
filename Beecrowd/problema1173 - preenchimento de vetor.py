# Lê o valor de entrada
V = int(input().strip())

# Inicializa o vetor N com 10 posições
N = [0] * 10

# Coloca o valor lido na primeira posição do vetor
N[0] = V

# Preenche as posições subsequentes com o dobro do valor da posição anterior
for i in range(1, 10):
    N[i] = N[i - 1] * 2

# Mostra o vetor
for i in range(10):
    print(f"N[{i}] = {N[i]}")