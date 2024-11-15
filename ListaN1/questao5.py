num = int(input("Digite um número inteiro maior que zero: "))

if num > 0:
    somaAlgarismos = sum(int(digito) for digito in str(num))
    print(f"A soma dos algarismos de {num} é: {somaAlgarismos}")

else:
    print("Número inválido")