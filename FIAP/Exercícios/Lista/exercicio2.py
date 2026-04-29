lista = []
par = []
for i in range(10):
    n = int(input("Digite 10 números: "))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
print(sum(par))
print(len(lista)/(sum(lista)))