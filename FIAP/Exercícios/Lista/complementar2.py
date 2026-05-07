'''#Preencha uma lista com 30 números aleatórios (sorteados de 1 a 50).
A partir dessa lista, gere uma nova lista contendo apenas os números primos da lista'''

import random
lista = []
primos = []
for i in range(30):
    lista.append(random.randint(1,50))
print(f"Lista principal: {lista}")