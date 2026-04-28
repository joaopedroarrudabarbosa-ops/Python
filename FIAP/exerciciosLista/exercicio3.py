import random
lista = []
for i in range(20):
    a = random.randint(1, 50)
    n = int(input("Digite 20 numeros ai: "))
    lista.append(n)
print(lista)
print(sum(lista))
print(max(lista))
print(min(lista))