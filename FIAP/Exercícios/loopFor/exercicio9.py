num = int(input("Digite um numero que voce gostaria de saber o fatorial: "))
if num <= 0 or num == 1:
    print("Impossivel de fatoriar")
else:
    fat = num
    for valor in range(1,num,1):
        fat = fat * valor
    print(f"O fatorial para o numero {num}! foi {fat}.")
