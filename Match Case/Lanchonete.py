erro = ("Opção invalida")
resp = "s"
total = 0
while resp == "s":

    print("LANCHONETE DO ESQUINÃO\n")
    print("1. Lanches.")
    print("2. Bebidas.")
    print("3. Sobremesas.")
    cardapio = input("Esolha uma opção: ")
    match cardapio:
        case "1":
            print("Você escolheu a opção lanches.")
            print("1. Cachorro-quente: R$15,00.")
            print("2. Hamburguer: R$20,00.")
            lanche = input("Escolha uma opção de lanche: ")
            match lanche:
                case "1":
                    print("Você escolheu cachorro-quente - R$15,00.")
                    quantidade = int(input("Quantos você gostaria? "))
                    cachorro = 15
                    valor_ch = quantidade * cachorro
                    valor = (f"O valor do cachorro-quente será: {valor_ch}")
                    print(valor)
                case "2":
                    print("Você escolheu hamburguer - R$20,00.")
                    quantidade = int(input("Quantos você gostaria? "))
                    hamburguer = 20
                    valor_hm = quantidade * hamburguer
                    valor = (f"O valor do hamburguer será: {valor_hm}")
                    print(valor)
                case _:
                    print(erro)
        case "2":
            print("Você escolheu a opção bebidas.")
            print("1. Refrigerante: R$6,00.")
            print("2. Suco natural: R$10,00.")
            bebida = input("Escolha uma opção de bebida: ")
            match bebida:
                case "1":
                    print("Você escolheu refrigerante - R$6,00.")
                    quantidade = int(input("Quantos você gostaria? "))
                    refri = 6
                    valor_rf = quantidade * refri
                    valor = (f"O valor do refrigerante será: {valor_rf}")
                    print(valor)
                case "2":
                    print("Você escolheu suco natural - R$10,00.")
                    quantidade = int(input("Quantos você gostaria? "))
                    suco = 10
                    valor_sc = quantidade * suco
                    valor = (f"O valor do refrigerante será: {valor_sc}.")
                    print(valor)
                case _:
                    print(erro)
        case "3":
            print("Você escolheu a opção sobremesas.")
            print("1. Açai: R$25,00.")
            print("2. Sorvete: R$18,00.")
            sobremesa = input("Escolha uma opção de sobremesa: ")
            match sobremesa:
                case "1":
                    print("Você escolheu Açai - R$25,00.")
                    quantidade_ac = int(input("Quantos você gostaria? "))
                    acai = 25
                    valor_aç = quantidade_ac * acai
                    valor = (f"O valor do açai será: {valor_aç}.")
                    print(valor)
                case "2":
                    print("Você escolheu sorvete - R$18,00.")
                    quantidade = int(input("Quantos você gostaria? "))
                    sorvete = 18
                    valor_sv = quantidade * sorvete
                    valor = (f"O valor do sorvete será: {valor_sv}.")
                    print(valor)
                case _:
                    print(erro)

            total += valor
        if 1 <= opc <= 3 and 1 <= pedido <= 2:
            print(total, valor)
        resp = input("Deseja continuar? S/N: ")

    if total > 0:
        print(f"Seu pedido custará {total:.2f}.")