def saudacao():
    print("Olá, seja bem-vindo.")
saudacao()

def soma(a,b):
    total = a + b
    print(f"A soma de {a} + {b} = {total}")

a = int(input("Digite seu 1º numero para soma: "))
b = int(input("Digite seu 2º numero para soma: "))
soma(a,b)