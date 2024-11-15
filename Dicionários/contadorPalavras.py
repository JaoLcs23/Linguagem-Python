arquivo = open('palavras.txt', 'r')

for linha in arquivo:
 print(linha, end="")
 # Converte para minúsculas e separa em palavras
 words = linha.lower().strip().split()
 # Atualiza a contagem de cada palavra
 mini_count = dict()
 conta_palavras = 0

for palavra in words:
 if palavra in mini_count:
  mini_count[palavra] += 1
 else:
  mini_count[palavra] = 1

# Imprime a contagem de cada palavra
print(mini_count)
arquivo.close()