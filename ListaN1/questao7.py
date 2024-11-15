n = int(input("Digite a quantidade de números a inserir: "))

b = []

for i in range(n):
    numero = int(input(f"Digite o número {i + 1}: "))
    b.append(numero)

maior = max(b)
menor = min(b)
soma_total = sum(b)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A soma total dos números é: {soma_total}")

b.sort()
print("Números em ordem crescente:", b)

b.sort(reverse=True)
print("Números em ordem decrescente:", b)