print("""
===========================================
    Simulador de controlador de bordo
===========================================
""")

distancia = float(input("Informe a distancia percorrida: "))
tempo = float(input("Informe o tempo: "))

velocidade_media = distancia / tempo
print(f"A sua velocidade media foi: {velocidade_media:.2f}km/h")