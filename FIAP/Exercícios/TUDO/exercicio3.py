'''#Em um jogo de dados, pode ser sorteado qualquer número entre 1 e 6. Faça uma
função que simule 1 milhão de lançamentos de dados e mostre quantas vezes cada
número foi sorteado.'''

import random
def dados():
    dado = [0, 0, 0, 0, 0, 0]
    for i in range(1001):
        x = random.randint(1,6)
        match x:
            case 1:
                dado[x-1] += 1
            case 2:
                dado[x-1] += 1
            case 3:
                dado[x-1] += 1
            case 4:
                dado[x-1] += 1
            case 5:
                dado[x-1] += 1
            case 6:
                dado[x-1] += 1
    return dado
dado = dados()
for i in range(len(dado)):
    print(f"O número {i+1} apareceu {dado} vezes.")
