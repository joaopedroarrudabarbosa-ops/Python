'''#Preencha uma lista com 10 itens e verifique se ela é um palíndromo, ou seja, se ela é
igual quando lida da esquerda para a direita e da direita para a esquerda.'''

'''#lista = []
cont = 0
print("Informe 5 números")

for i in range(5):
    cont += 1
    n = int(input(f"Digite o {cont}º numero: "))
    lista.append(n)

if lista == lista[::-1]:
    print("A lista é um palíndromo!")
else:
    print("A lista não é um palíndromo.")'''

P = []
for i in range(5):
    n = int(input(f"Digite um valor inteiro: "))
    P.append(n)
isPallindrome = True
for left in range(int(len(P) / 2)):
    right = len(P)-1-left
    if P[right]!= P[left]:
        isPallindrome = False
        break

if isPallindrome:
    print("Palindromo")
else:
    print("Não é palindromo")
