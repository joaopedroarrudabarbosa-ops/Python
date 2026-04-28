opc = 0
ficha = {}

while opc != 4:
    print("""
        FICHA CADASTRAL\n
        1 - Incluir informações na ficha.
        2 - Recuperar informações na ficha.
        3 - Exbir a ficha completa.
        4 - Sair.
    """)
    opc = int(input("Informe uma opcao: "))
    if opc == 1:
        chave = input("Informe o campo que deseja cadastrar na ficha: ")
        valor = input("Informe o dado que deseja cadastrar nesse campo: ")
        #ficha [chave] = valor
        ficha.update({chave:valor})
    elif opc == 2:
        print(f"Os campos disponiveis para pesquisa são: {ficha.keys()}")
        chave = input("Digite qual chave gostaria de procura: ")
        #print(ficha.get(chave))
        if chave in ficha.keys():
            #print(ficha[chave])
            print(f"O campo {chave} contem o dado: {ficha.get(chave)}")
        else:
            print("Voce digitou um campo inexistente.")
    elif opc == 3:
        print("FICHA CADASTRAL")
        for chave, valor in ficha.items():
            print(f"{chave.upper} --> {valor}")
    elif opc == 4:
        print("Saindo do sistema de ficha cadastral.")
        break
    else:
        print("Escolha uma opção válida.")
