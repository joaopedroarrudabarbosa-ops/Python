'''#Preencha duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas.'''

import random
lista1 = []
lista2 = []

for i1 in range(10):
    a = random.randint(1,20)
    lista1.append(a)
for i2 in range(10):
    b = random.randint(21,40)
    lista2.append(b)

print(f"Os valores da primeira lista são: {lista1}")
print(f"Os valores da segunda lista são: {lista2}")

lista3 = []
for i in zip(lista1,lista2):
    for i3 in i:
        lista3.append(i3)
print(f"Os valores da 1º lista e 2º lista juntos, intercalando são: {lista3}")