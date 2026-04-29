#criando funcao
def calcularVelocidadeMedia():
#codigo da nossa funcao
    velocidadeMedia = distancia / tempo
    print(f"A velocida média é {velocidadeMedia}.")

distancia = float(input("Digite a distancia percorrida: "))
tempo = float(input(("Digte o tempo de viagem: ")))

#chamando funcao
calcularVelocidadeMedia()

