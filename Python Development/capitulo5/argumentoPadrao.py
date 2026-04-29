#criando funcao
def calcularVelocidadeMedia(distancia:float, tempo:float, unidadeMedia="km/h"):

#codigo da nossa funcao
    velocidadeMedia = distancia / tempo
    print(f"A velocida média é {velocidadeMedia}{unidadeMedia}.")

#chamando funcao
calcularVelocidadeMedia(200, 3,"m/s")
calcularVelocidadeMedia(200,4)