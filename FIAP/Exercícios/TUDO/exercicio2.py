'''#Dizemos que um número natural é triangular se ele é produto de três números
naturais consecutivos.
Por exemplo:
120 é triangular, pois 4 * 5 * 6 = 120.
2730 é triangular, pois 13 * 14 * 15 = 2730.
Faça uma função que receba um número inteiro e retorne True se for um número
triangular e False, caso contrário.'''

def triangular(num):
    cont = 1
    while True:
        if cont * (cont + 1) * (cont+2) == num:
            return True
        elif cont * (cont + 1) * (cont+2) > num:
            return False
        cont += 1

n = int(input("Digite um número que gostaria de saber se é traingular: "))
if triangular(n):
    print(f"O número {n} É triangular.")
else:
    print(f"O número {n} NÃO É triangular.")