A = int(input("Insira valor para A: "))
B = int(input("Insira valor para B: "))
C = int(input("Insira valor para C: "))
D = int(input("Insira valor para D: "))

if(B>C and D>A and C+D>A+B and C>0 and D>0 and A%2==0):
    print("Valores aceitos")

else:
    print("Valores nao aceitos")