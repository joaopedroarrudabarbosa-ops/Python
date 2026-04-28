lista = ["Paulo", "Ana", "Pedro", "Maria"]
print(lista)
for i in lista:
    print(i)
n = len(lista)
print(f"A lista possui {n} itens")
lista.pop(3) #remove o indice
print(lista)

numeros = []
while True:
    n = int(input("Informe o numero: "))
    if n == 0:
        break
    numeros.append(n) #adiciona valor a lista
print(numeros) #mostra os numeros listados
print(sum(numeros)) #soma os valores da lista
