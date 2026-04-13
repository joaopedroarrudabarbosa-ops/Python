print("MENU")
opcao = 0
while opcao != 3:
    print("1 - Receber um elogio.")
    print("2 - Calcular o fatorial.")
    print("3 - Sair.")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print("Você é muito inteligente.")
    elif opcao == 2:
        numero = int(input("Insira o número que deseja fatoriar: "))
        fat = numero
        for valor in range(1,numero,1):
            fat = fat * valor
            print(f"O fatorial para o numero informado foi {fat}.")
    elif opcao == 3:
        print("Saindo do programa.")
    else:
        print("Escolha uma opção do menu!")