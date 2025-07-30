# Calculadora de preço final com desconto

# Solicita os valores ao usuário
preco_original = float(input("Digite o preço original do produto: R$ "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))

# Calcula o valor do desconto
valor_desconto = preco_original * (porcentagem_desconto / 100)

# Calcula o preço final
preco_final = preco_original - valor_desconto

# Exibe os resultados formatados
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")