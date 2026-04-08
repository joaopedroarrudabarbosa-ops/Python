'''#print("SISTEMA DE NOTAS\n")
print("1. Verificar nota")
print("2. Editar nota")
print("3. Inserir nota")
print("4. Excluir nota")
print("5. Sair")
opc = input("Escolha uma opção: ")
match opc:
    case "1":
        print("Você escolheu a opção de verificar a nota do aluno.")
    case "2":
        print("Você escolheu a opção de editar a nota do aluno.")
    case "3":
        print("Você escolheu a opção de inserir a nota do aluno.")
    case "4":
        print("Você escolheu a opção de excluir a nota do aluno.")
    case "5":
        print("Você escolhe a opção de sair.\nSaindo...")
    case _:
        print("Opção inválida.\nTente novamente outra opção.")'''

print("LANCHONETE DO ESQUINÃO\n")
print("1. Lanches.")
print("2. Bebidas.")
print("3. Sobremesas.")
print("4. Sair.")
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
                quantidade_ch = int(input("Quantos você gostaria? "))
                valor_ch = quantidade_ch * 15
                final_ch = (f"O valor do cachorro-quente será: {valor_ch}")
                print(final_ch)
            case "2":
                print("Você escolheu hamburguer - R$20,00.")
                quantidade_hm = int(input("Quantos você gostaria? "))
                valor_hm = quantidade_hm * 15
                final_hm = (f"O valor do hamburguer será: {valor_hm}")
                print(final_hm)
    case "2":
        print("Você escolheu a opção bebidas.")
        print("1. Refrigerante: R$6,00.")
        print("2. Suco natural: R$10,00.")
        bebida = input("Escolha uma opção de bebida: ")
        match bebida:
            case "1":
                print("Você escolheu refrigerante - R$6,00.")
                quantidade_rf = int(input("Quantos você gostaria? "))
                valor_rf = quantidade_rf * 6
                final_rf = (f"O valor do refrigerante será: {valor_rf}")
                print(final_rf)
            case "2":
                print("Você escolheu suco natural - R$10,00.")
                quantidade_sc = int(input("Quantos você gostaria? "))
                valor_sc = quantidade_sc * 10
                final_sc = (f"O valor do refrigerante será: {valor_sc}.")
                print(final_sc)
    case "3":
        print("Você escolheu a opção sobremesas.")
        print("1. Açai: R$25,00.")
        print("2. Sorvete: R$18,00.")
        sobremesa = input("Escolha uma opção de sobremesa: ")
        match sobremesa:
            case "1":
                print("Você escolheu Açai - R$25,00.")
                quantidade_aç = int(input("Quantos você gostaria? "))
                valor_aç = quantidade_aç * 25
                final_aç = (f"O valor do açai será: {valor_aç}.")
                print(final_aç)
            case "2":
                print("Você escolheu sorvete - R$18,00.")
                quantidade_sv = int(input("Quantos você gostaria? "))
                valor_sv = quantidade_sv * 18
                final_sv = (f"O valor do sorvete será: {valor_sv}.")
                print(final_sv)
    case "4":
        print("Você escolheu a opção Sair.\nSaindo...")