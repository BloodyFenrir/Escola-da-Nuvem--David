import requests

cep = input("Digite o CEP (somente números): ")

try:
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    response.raise_for_status()
    dados = response.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        logradouro = dados.get("logradouro", "")
        bairro = dados.get("bairro", "")
        cidade = dados.get("localidade", "")
        estado = dados.get("uf", "")

        print("Logradouro:", logradouro)
        print("Bairro:", bairro)
        print("Cidade:", cidade)
        print("Estado:", estado)
except Exception as e:
    print("Erro ao consultar o CEP:", e)