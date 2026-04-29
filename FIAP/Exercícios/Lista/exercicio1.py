par = []
impar = []
for i in range(10):
    n = int(input("Digite 10 números: "))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(par)
print(impar)

