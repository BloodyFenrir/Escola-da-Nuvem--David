import requests

try:
    response = requests.get("https://randomuser.me/api/")
    response.raise_for_status()
    dados = response.json()

    usuario = dados['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print("Nome:", nome)
    print("Email:", email)
    print("País:", pais)
except Exception as e:
    print("Erro ao obter dados do usuário:", e)