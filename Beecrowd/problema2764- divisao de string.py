# Lê a data no formato DD/MM/AA
data = input().strip()

# Separa a data em dia, mês e ano
dia, mes, ano = data.split('/')

# Imprime a data nos formatos solicitados
print(f"{mes}/{dia}/{ano}")
print(f"{ano}/{mes}/{dia}")
print(f"{dia}-{mes}-{ano}")