# Verificador de senha de usuário

senha = input("Digite sua senha: ")

# Critérios: mínimo 8 caracteres e pelo menos um número
tem_numero = any(c.isdigit() for c in senha)
tamanho_ok = len(senha) >= 8

if tamanho_ok and tem_numero:
    print("Senha forte! Atende aos critérios de segurança.")
else:
    print("Senha fraca! A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")