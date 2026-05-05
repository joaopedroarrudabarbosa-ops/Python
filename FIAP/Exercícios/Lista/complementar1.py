'''#Preencha uma lista com 10 números aleatórios únicos (sorteados de 1 a 20), ou seja,
sem elementos repetidos.'''

lista = []
import random
while len(lista) < 10:
    a = random.randint(1,20)
    if a not in lista:
        lista.append(a)
print(lista)