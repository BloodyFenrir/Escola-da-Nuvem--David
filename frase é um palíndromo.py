def eh_palindromo(frase: str) -> bool:
    """
    Verifica se uma palavra ou frase é um palíndromo, ignorando espaços e pontuação.

    Parâmetros:
    frase (str): Palavra ou frase a ser verificada

    Retorna:
    bool: True se for palíndromo, False caso contrário
    """
    import string
    frase_limpa = ''.join(c.lower() for c in frase if c.isalnum())
    return frase_limpa == frase_limpa[::-1]

# Exemplo de uso:
texto = input("Digite uma palavra ou frase: ")
if eh_palindromo(texto):
    print("Sim")
else:
    print("Não")