import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

try:
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()

    chave = f"{moeda}BRL"
    if chave in dados:
        info = dados[chave]
        print(f"Moeda: {moeda}/BRL")
        print(f"Valor atual: R$ {info['bid']}")
        print(f"Valor máximo: R$ {info['high']}")
        print(f"Valor mínimo: R$ {info['low']}")
        print(f"Última atualização: {info['create_date']}")
    else:
        print("Moeda não encontrada ou código inválido.")
except Exception as e:
    print("Erro ao consultar cotação:", e)