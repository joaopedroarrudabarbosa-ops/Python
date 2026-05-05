'''#Preencha uma lista com 10 itens e verifique se ela é um palíndromo, ou seja, se ela é
igual quando lida da esquerda para a direita e da direita para a esquerda.'''

lista = []
cont = 0
print("Informe 10 números")

for i in range(10):
    cont += 1
    n = int(input(f"Digite o {cont}º numero: "))
    lista.append(n)

if lista == lista[::-1]:
    print("A lista é um palíndromo!")
else:
    print("A lista não é um palíndromo.")