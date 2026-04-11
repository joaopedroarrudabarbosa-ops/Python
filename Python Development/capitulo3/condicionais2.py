print("Saldão da alegria!!")

valorDaCompra = float(input("Qual o valor da compra? "))
formaDePagamento = input("Qual a forma de pagamento:\n1 - Boleto.\n2 - Cartao.\n")
if formaDePagamento == "1":
    print("Pagamentos no boleto tem 5% de desconto.")
    desconto = valorDaCompra * 0.95
    print(f"O valor total será de R${desconto:.2f}.")
else:
    formaDePagamento == "2"
    print("Você pode parcelar o valor total em ate 12x.")
    parcelas = int(input("Quantas vezes deseja parcelar? "))
    parcelaValor = valorDaCompra / parcelas
    print(f"Você terá {parcelas} parcelas de R${parcelaValor:.2f} para pagar.")
