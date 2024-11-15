import math

# Função para calcular as raízes da equação de Bhaskara
def calcular_raizes(a, b, c):
    delta = b**2 - 4 * a * c
    if a == 0 or delta < 0:
        return "Impossivel calcular"
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"R1 = {raiz1:.5f}\nR2 = {raiz2:.5f}"

# Lê os valores de A, B e C
A, B, C = map(float, input().strip().split())

# Calcula e imprime as raízes
resultado = calcular_raizes(A, B, C)
print(resultado)