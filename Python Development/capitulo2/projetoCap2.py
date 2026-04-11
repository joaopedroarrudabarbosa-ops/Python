print("Cadastro de doador de sangue")

nome = input("Por favor, informe seu nome completo: ")

peso = float(input("Por favor, informe seu peso: "))
pesoMinimo = 50
temPesoMinimo = peso > pesoMinimo

anoNascimento = int(input("Por favor, informe seu ano de nascimento: "))
ano = 2026
idade = ano - anoNascimento
temIdadeMinima = idade >= 16

altura = float(input("Por favor, informe sua altura: "))

texto_saida = f"\tNOME: {nome}\n\tIDADE: {idade}\n\tPESO: {peso}\n\tALTURA: {altura}\n\tTEM PESO MINIMO PARA DOAR {temPesoMinimo}\n\tTEM IDADE MINIMA PARA DOAR {temIdadeMinima}"
print(texto_saida)