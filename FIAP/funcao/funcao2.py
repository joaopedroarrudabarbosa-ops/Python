def parImpar (numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

#main
n = int(input("Digite o número que gostaria de saber se é par ou ímpar: "))
parImpar(n)
