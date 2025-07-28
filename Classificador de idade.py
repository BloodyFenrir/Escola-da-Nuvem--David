idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Categoria: Criança")
elif idade >= 13 and idade <= 17:
    print("Categoria: Adolescente")
elif idade >= 18 and idade <= 59:
    print("Categoria: Adulto")
elif idade >= 60:
    print("Categoria: Idoso")
else:
    print("Idade inválida.")