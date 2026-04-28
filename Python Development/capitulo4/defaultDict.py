from collections import defaultdict

dicionarioLista = defaultdict(list)
dicionarioLista["PRODUTO"] = "MacBook Pro"
dicionarioLista["MARCA"] = "Apple"
print(dicionarioLista)
print(dicionarioLista["VALOR"])
print(dicionarioLista)

def funcaoExemplo():
    return "Inexistente"
print(funcaoExemplo())
dicionarioFuncao = defaultdict(funcaoExemplo)
dicionarioFuncao["PRODUTO"] = "MacBook Pro"
dicionarioFuncao["MARCA"] = "Apple"
print(dicionarioFuncao)
print(dicionarioFuncao["PREÇO"])
print(dicionarioFuncao)

dicionarioLambda = defaultdict(lambda: "Não disponivel")
dicionarioLambda["PRODUTO"] = "MacBook Pro"
dicionarioLambda["MARCA"] = "Apple"
print(dicionarioLambda)
print(dicionarioLambda["PREÇO"])
print(dicionarioLambda)
