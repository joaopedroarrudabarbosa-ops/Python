print("Companhia Aerea")

tipoCliente = input("Informe o tipo de cliente:\nPREMIUM.\nGOLD.\nNORMAL.\n")
pesoBagagem = float(input("Informe o peso da bagagem que deseja despacha: "))

if tipoCliente.upper() == "PREMIUM":
    if pesoBagagem <= 32:
        print(f"Cliente {tipoCliente}, sua bagagem esta dentro do limite permitido! Não é necessário pagar nennhum valor para despacha-la.")
    else:
        print(f"Cliente {tipoCliente}, sua bagagem exedeu o limite permitido! Você terá que pagar um valor adicional para despacha-la.")
elif tipoCliente.upper() == "GOLD":
    if pesoBagagem <= 28:
        print("fCliente {tipoCliente}, sua bagagem esta dentro do limite permitido! Não é necessário pagar nennhum valor para despacha-la.")
    else:
        print(f"Cliente {tipoCliente}, sua bagagem exedeu o limite permitido! Você terá que pagar um valor adicional para despacha-la.")
else:
    print(f"Cliente {tipoCliente}, você devera pagar pelos {pesoBagagem}kg da sua bagagem despachada. Dirija-se ao balcão para realizar o pagamento.")

# if - se
# else - senao
# elif - senao se
# .upper() - deixa tudo que foi escrito no input em maiusculo