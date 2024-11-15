import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while not acertou:
        chute = int(input("Digite seu chute: "))
        tentativas += 1

        if chute == numero_secreto:
            acertou = True
            print(f"Muito bem, acertou em {tentativas} tentativas!")
        elif chute < numero_secreto:
            print("Seu chute é menor que o número secreto.")
        else:
            print("Seu chute é maior que o número secreto.")

jogo_adivinhacao()