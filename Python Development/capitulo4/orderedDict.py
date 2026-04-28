from collections import OrderedDict

dicionarioOrdenado = OrderedDict()
print(dicionarioOrdenado)

dicionarioOrdenado["Nome"] = "Iphone"
dicionarioOrdenado["Marca"] = "Apple"
(dicionarioOrdenado)["Modelo"] = "14 Pro Max"

for chave, valor in dicionarioOrdenado.items():
    print(f"{chave} --> {valor}")
print()
dicionarioOrdenado["Marca"] = "Maça"
for chave, valor in dicionarioOrdenado.items():
    print(f"{chave} --> {valor}")
print()
dicionarioOrdenado.pop("Marca")
for chave, valor in dicionarioOrdenado.items():
    print(f"{chave} --> {valor}")
print()
dicionarioOrdenado["Marca"] = "Apple"
for chave, valor in dicionarioOrdenado.items():
    print(f"{chave} --> {valor}")


