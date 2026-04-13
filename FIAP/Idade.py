resp = 1
cont = 0
while resp <= 10:
    idade = int(input(f"Diga a {resp}º idade: "))
    if idade >= 18:
        cont += 1
    resp += 1
print(f"Tem {cont} maiores de idade.")

