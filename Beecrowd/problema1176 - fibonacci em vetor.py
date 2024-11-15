# Função para calcular o N-ésimo termo da série de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Lê o número de casos de teste
T = int(input().strip())

# Processa cada caso de teste
for _ in range(T):
    N = int(input().strip())
    resultado = fibonacci(N)
    print(f"Fib({N}) = {resultado}")