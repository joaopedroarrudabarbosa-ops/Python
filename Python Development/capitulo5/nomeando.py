def exibirFicha(**dados):

    print("----FICHA----")
    #print(dados["nome"])
    #print(dados["estadoCivil"])

    for chave, valor in dados.items():
        print(f"{chave.upper()}: {valor}")

fichaCliente = {
    "nome": "Joao",
    "estado civil": "solteiro",
    "camisa": "preta",
    "filhos": False
}

exibirFicha(**fichaCliente)