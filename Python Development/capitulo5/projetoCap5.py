def calcularVelocidadeMedia(distancia:float, tempo:float, unidadeMedida="km/h"):
    if tempo == 0:
        return 0
    velocidadeMedia = distancia / tempo
    return f"{velocidadeMedia} {unidadeMedida}"

def converterTemperatura(temperatura:float, unidadeMedida="Celsius"):
    if unidadeMedida == "celsius":
        return temperatura * 1.8 + 32
    elif unidadeMedida == "farenheit":
        return (temperatura - 32) / 1.8
    else:
        return 0


def exibirMenu():
    print("""
        1 - Calcular velocidade média.
        2 - Converter temperatura.
        3 - Sair.
    """)

def alunoDeFisica():
    opc = 0
    while opc != 3:
        exibirMenu()
        opc = int(input("Informe a opção desejada: "))
        if opc == 1:
            distanciaPercorrida = float(input("Digite a distancia percorrida: "))
            tempoViagem = float(input("Digite o tempo de viagem: "))
            medida = input("Informe a unidade de medida: ")
            print(f"A velocidade média é {calcularVelocidadeMedia(distanciaPercorrida, tempoViagem, medida)}")
        elif opc == 2:
            temperaturaInformada = float(input("Digite a temperatura que deseja converter: "))
            medida = input("A temperatura informada esta em celsius ou farenheit? ")
            print(f"O resultado da conversão é {converterTemperatura(temperaturaInformada, medida)}")
        elif opc == 3:
            print("Saindo do sistema...")
            break
        else:
            print("Opção invalida.")
alunoDeFisica()