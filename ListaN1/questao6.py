votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]

contA = 0
contB = 0
contC = 0

for voto in votos:
    if voto == "A":
        contA += 1
    elif voto == "B":
        contB += 1
    elif voto == "C":
        contC += 1

print(f"Votos para A: {contA}")
print(f"Votos para B: {contB}")
print(f"Votos para C: {contC}")