from datetime import datetime

# Solicita a data de nascimento ao usuário
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte a string para um objeto de data
nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
hoje = datetime.now()

# Calcula a diferença em dias
dias_vivo = (hoje - nascimento).days

print(f"Você está vivo há {dias_vivo} dias.")