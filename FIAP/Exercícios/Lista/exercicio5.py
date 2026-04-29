import random
lista = []
for i in range(10):
    a = random.randint(1,10)
    lista.append(a)
numero = int(input("Digite um de 1 à 10: "))
quantidade = lista.count(numero)
print(f"A lista gerada foi: {lista}")
print(f"O numero {numero} aparece {quantidade} vezes na lista.")
