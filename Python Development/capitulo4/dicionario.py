#criar um dicionario
dicionario = {
    "Nome": "Star Wars - Episódio IV - Uma nova esperança",
    "Diretor": "George Lucas",
    "Ano de lançamento": 1977,
    "Bilheteria": 775000000.00
}
print(type(dicionario))

#exebicao do dicionario completo
print(dicionario)

#exibir valor de uma chave especifica do dicionario
print(dicionario["Nome"])

#insercao de uma nova chave e valor (genero)
dicionario["Gênero"] = "Space Opera"
print(dicionario)

#metodo keys
print(dicionario.keys())
for chave in dicionario.keys():
    print(chave)

#metodo valeus
print(dicionario.values())
for valor in dicionario.values():
    print(valor)

#metodo items
print(dicionario.items())
for chave, valor in dicionario.items():
    print(f"{chave} -- {valor}")

#metodo get
print(dicionario.get("Publico"))
print(dicionario.get("Nome"))

#metodo setdefault
dicionario.setdefault("Publico", 1000)
print(dicionario)
dicionario.setdefault("Publico", 100)
print(dicionario)