valor = float(input("Insira o valor total: "))

valorAVista = valor-(valor*0.1)
valorParcelado = valor/3
comissaoAVista = (valor-(valor*0.1))*0.05
comissaoParcelado = valor*0.05

print(f"Valor com desconto: R$ {valorAVista:.2f}")
print(f"Valor de cada parcela, no parcelamento de 3x sem juros: R$ {valorParcelado:.2f}")
print(f"Comissão com pagamento a vista: R$ {comissaoAVista:.2f}")
print(f"Comissão com pagamento parcelado: R$ {comissaoParcelado:.2f}")