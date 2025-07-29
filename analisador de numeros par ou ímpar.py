# Analisador de números: par ou ímpar

quantidade = int(input("Quantos números você deseja analisar? "))
pares = 0
impares = 0

for i in range(quantidade):
    numero = int(input(f"Digite o número {i+1}: "))
    if numero % 2 == 0:
        pares += 1
        print(f"{numero} é par.")
    else:
        impares += 1
        print(f"{numero} é ímpar.")

print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")