print("""
======================================================
      Boas vindas ao calculador de inteiros
======================================================
""")

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

# print(type(primeiro_valor)) - print("type"(variavel)) da print na tela mostrando o tipo da variavel (string, int, float etc)

soma = primeiro_valor + segundo_valor
subtracao = primeiro_valor - segundo_valor
divisao = primeiro_valor / segundo_valor
multiplicacao = primeiro_valor * segundo_valor
print(f"O resultado da soma foi: {soma}") # forma mais usavel
print(f"O resultado da subtração foi: {subtracao}")
print(f"O resultado da divisão foi: {divisao}")
print(f"O resultado da multiplicação foi: {multiplicacao}")
# print("O resultado da soma foi: {}".format(soma)) - outra maneira
# print("O resultado da soma foi:", soma) - e outra maneira