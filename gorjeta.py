def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)

    Retorna:
    float: O valor da gorjeta calculada
    """
    return valor_conta * (porcentagem_gorjeta / 100)

# Exemplo de uso:
conta = float(input("Digite o valor total da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))
gorjeta = calcular_gorjeta(conta, porcentagem)
print(f"Valor da gorjeta: R$ {gorjeta:.2f}")