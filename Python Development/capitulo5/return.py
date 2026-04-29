def soma(a,b):
    resultado = a + b
    return resultado
def subtracao(a,b):
    resultado = a - b
    return resultado
def multiplicacao(a,b):
    resultado = a * b
    return resultado
def divisao(a,b):
    resultado = a / b
    return resultado

valor1 = int(input("Digite o primeiro valor que deseja somar: "))
valor2 = int(input("Digite o segundo valor que deseja somar: "))

resposta = soma(valor1,valor2)
print(f"A resposta da soma é {resposta}")
print(f"A resposta da soma é {soma(valor1,valor2)}")

resposta = subtracao(valor1,valor2)
print(f"A resposta da subtracao é {resposta}")

resposta = multiplicacao(valor1,valor2)
print(f"A resposta da multiplicacao é {resposta}")

resposta = divisao(valor1,valor2)
print(f"A resposta da divisao é {resposta}")