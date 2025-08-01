import random
import string

# Solicita ao usuário a quantidade de caracteres da senha
tamanho = int(input("Informe o tamanho da senha desejada: "))

# Conjunto de caracteres: letras, dígitos e caracteres especiais
caracteres = string.ascii_letters + string.digits + string.punctuation

# Gera a senha aleatória
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

print("Senha gerada:", senha)