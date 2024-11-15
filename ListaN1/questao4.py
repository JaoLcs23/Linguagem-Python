notas = input("Insira as duas notas separadas por espaço: ").split()

nota1 = float(notas[0])
nota2 = float(notas[1])

if(nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10):
    print((nota1+nota2)/2)

else:
    print("Nota inválida")