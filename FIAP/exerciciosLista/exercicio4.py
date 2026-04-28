lista_nome = []
lista_idade = []
for i in range(2):
    nome = input("Digite seu nomes: ")
    lista_nome.append(nome)
    idade = int(input("Digite sua idades: "))
    lista_idade.append(idade)
print(lista_nome)
print(lista_idade)

print("Pessoas com idade igual ou superior a 18:")
for indice in range(len(lista_idade)):
    if lista_idade[indice] >= 18:
        print(lista_nome[indice])