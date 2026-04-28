lista = []
notas = float(input("Digite uma nota: "))

while notas > 0:
    lista.append(notas)
    notas = float(input("Digite uma nota: "))
    cont = len(lista)
print(f"Foram informadas {cont} notas.")
print(f"Notas informadas: {lista}.")

media = sum(lista) / cont
print(f"Media aritmedia foi: {media}.")

acimaMedia = 0
for i in lista:
    if i > media:
        acimaMedia += 1
print(f"Quantidade de notas acima da média foram: {acimaMedia}.")


