print("RESTAURANTE")

precoQuilo = float(input("Informe o valor cobrado por quilo: "))
pesoPrato = float(input("Informe o peso do prato do cliente (em kg): "))

precoPrato = pesoPrato * precoQuilo
if pesoPrato < 1:
    print(f"O valor do prato sera {precoPrato:.2f}")
else:
    print("O valor cobrado a partir de 1kg é fixo de R$80,00.\nO valor do prato sera R$80,00.")