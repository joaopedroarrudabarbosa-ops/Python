#forma de criar uma lista
lista = [12,15.5,"Olá."]

print(type(lista))

print(lista)

#insire valor na lista apos a criacao
lista.append("teste de inserção.")
print(lista)

#exibi o valor que esta na lista declarando sua posicao
print(lista[3])

print(lista[0:2])

#exibindo com loop
for valor in lista:
    print(valor)

#remover elemento - ultimo valor
lista.pop()
print(lista)
#valor especifico
lista.remove(15.5)
print(lista)

#quantidade de valores na lista
print(len(lista))