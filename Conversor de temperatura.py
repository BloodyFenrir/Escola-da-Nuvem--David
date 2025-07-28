# Solicita os dados do usuário
temperatura = float(input("Digite a temperatura: "))
origem = input("Informe a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
destino = input("Informe a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()

# Conversão
resultado = None

if origem == destino:
    resultado = temperatura
elif origem == "C" and destino == "F":
    resultado = (temperatura * 9/5) + 32
elif origem == "C" and destino == "K":
    resultado = temperatura + 273.15
elif origem == "F" and destino == "C":
    resultado = (temperatura - 32) * 5/9
elif origem == "F" and destino == "K":
    resultado = (temperatura - 32) * 5/9 + 273.15
elif origem == "K" and destino == "C":
    resultado = temperatura - 273.15
elif origem == "K" and destino == "F":
    resultado = (temperatura - 273.15) * 9/5 + 32
else:
    print("Unidade inválida.")

if resultado is not None:
    print(f"{temperatura}°{origem} equivale a {round(resultado, 2)}°{destino}")