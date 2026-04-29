def exibirPromocao(*clientes):
    for cliente in clientes:
        print(f"Olá, {cliente}!\nQueremos te avisar que a nova X-WING esta em promoção!")

listaClientes = ["Luke", "Princesa Isabel", "Mestre Dave"]
exibirPromocao(*listaClientes)

#exibirPromocao("Luke", "Princesa Isabel", "Mestre Dave"])

#exibirPromocao("Luke")
#exibirPromocao("Princesa Isabel")
#exibirPromocao("Mestre Dave")