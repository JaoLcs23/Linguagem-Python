# Função para calcular o valor em tons de cinza
def calcular_tons_de_cinza(conversao, R, G, B):
    if conversao == 'eye':
        return int(0.30 * R + 0.59 * G + 0.11 * B)
    elif conversao == 'mean':
        return int((R + G + B) / 3)
    elif conversao == 'max':
        return max(R, G, B)
    elif conversao == 'min':
        return min(R, G, B)

# Lê o número de casos de teste
T = int(input().strip())

# Processa cada caso de teste
for t in range(1, T + 1):
    conversao = input().strip()
    R, G, B = map(int, input().strip().split())
    P = calcular_tons_de_cinza(conversao, R, G, B)
    print(f"Caso #{t}: {P}")