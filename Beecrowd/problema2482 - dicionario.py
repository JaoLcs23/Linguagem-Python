# Lê o número de traduções
N = int(input())

# Cria um dicionário para armazenar as traduções
traducao = {}

# Lê as traduções
for _ in range(N):
    lingua = input().strip()
    mensagem = input().strip()
    traducao[lingua] = mensagem

# Lê o número de crianças
M = int(input())

# Cria uma lista para armazenar as etiquetas
etiquetas = []

# Lê os nomes das crianças e suas línguas nativas
for _ in range(M):
    nome = input().strip()
    lingua = input().strip()
    etiquetas.append(f"{nome}\n{traducao[lingua]}\n")

# Imprime as etiquetas
for etiqueta in etiquetas:
    print(etiqueta)