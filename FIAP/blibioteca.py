import random
a = random.randint(1,100)
resp = 0
while True:
    resp = int(input("Digite um numero entre 1 e 100: "))
    if resp == a:
        print("Parabens! Voce acertou!")
        break
    elif resp > a:
        print("Seu chute foi maior que o numero\nTente novamente.")
    else:
        resp < a
        print("Seu chute menor que o numero\nTente novamente.")