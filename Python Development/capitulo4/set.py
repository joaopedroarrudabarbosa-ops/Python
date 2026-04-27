#criar um set vazio
conjunto = set()
print(type(conjunto))

#criando um set a partir de uma lista
lista = ["Joao", "Fernando", "Davi", "Yuri", "Luiz", "Joao"]
print(lista)
conjunto2 = set(lista)
print(conjunto2)

#criar um set com valores
conjunto3 = {"Joao", "Mae", "Pai", "Joao"}
print(conjunto3)

#adicionando elementos (add)
conjunto3.add("Filho")
print(conjunto3)

#remove elementos que estao em outro set (difference_update)
conjunto4 = {"PlayStation", "Xbox", "Nitendo"}
conjunto5 = {"PlayStation", "Mega Drive", "Nitendo 64", "Sega Saturn", "Dreamcast"}
print(f"Os itens do primeiro set são: {conjunto4}.")
print(f"Os itens do segundo set são: {conjunto5}.")
conjunto4.difference_update(conjunto5)
print(f"O primeiro set contem {conjunto4}.")

#remover um elementos especifico do set (remove)
conjunto4 = {"PlayStation", "Xbox", "Nitendo"}
print(conjunto4)
#conjunto4.remove("Nitendo")
#conjunto4.remove("Nitendo") - erro

#remover um elemento especifico do set (discard)
conjunto4.discard("Xbox")
print(conjunto4)
conjunto4.discard("Xbox")
print(conjunto4)

