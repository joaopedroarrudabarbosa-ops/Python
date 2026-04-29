#criando funcao
def calcularVelocidadeMedia(distancia, tempo):
#codigo da nossa funcao
    velocidadeMedia = distancia / tempo
    print(f"A velocida média é {velocidadeMedia}.")

dist = float(input("Digite a distancia percorrida: "))
temp = float(input(("Digte o tempo de viagem: ")))

#chamando funcao
calcularVelocidadeMedia(dist, temp)

def soma(a, b):
    total = a + b
    print(f"A soma é {total}")
soma(20,3)