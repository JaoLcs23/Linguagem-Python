# Lê o valor de N
N = int(input())

# Lê os valores do vetor X
X = list(map(int, input().split()))

# Inicializa o menor valor e a posição
menor_valor = X[0]
posicao = 0

# Encontra o menor valor e sua posição
for i in range(1, N):
    if X[i] < menor_valor:
        menor_valor = X[i]
        posicao = i

# Exibe o menor valor e sua posição
print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")