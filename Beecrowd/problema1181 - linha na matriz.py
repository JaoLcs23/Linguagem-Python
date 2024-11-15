# Lê o número da linha L
L = int(input().strip())

# Lê o tipo de operação T
T = input().strip()

# Inicializa a matriz M[12][12]
M = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input().strip()))
    M.append(linha)

# Calcula a soma ou média dos elementos da linha L
soma = sum(M[L])
if T == 'S':
    resultado = soma
elif T == 'M':
    resultado = soma / 12

# Imprime o resultado com 1 casa decimal
print(f"{resultado:.1f}")