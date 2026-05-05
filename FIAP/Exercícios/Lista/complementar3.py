'''#Preencha uma lista com 30 números aleatórios (sorteados de 1 a 50).
A seguir solicite um número inteiro e multiplique todos os itens da lista por esse número.'''

import random
lista = []
n = int(input("Digite um numero que deseja multiplicar: "))
for i in range(30):
    lista.append(random.randint(1,50))
res = [i * n for i in lista]
print(lista)
print(res)