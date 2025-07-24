# Valores e taxas
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Conversão
valor_dolar = round(valor_reais / taxa_dolar, 2)
valor_euro = round(valor_reais / taxa_euro, 2)

# Exibição dos resultados
print("Valor em reais: R$", valor_reais)
print("Valor em dólares: US$", valor_dolar)
print("Valor em euros: €", valor_euro)