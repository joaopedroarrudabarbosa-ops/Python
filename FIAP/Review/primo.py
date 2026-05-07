n = 0

while n < 2:
    n = int(input("Informe o número que deseja verificar se é primo: "))
    if n < 0:
        print("Informe um valor maior que 0.")
if n == 2:
    print(f"O número {n} é primo")
else:
    for i in range(3,n,2):
        if n % i == 0:
            print(f"O número {n} não é primo")
            break

    if i == n-1:
        print(f"O número {n} é primo")