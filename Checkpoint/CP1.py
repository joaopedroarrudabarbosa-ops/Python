# João Pedro de Arruda Barbosa - RM570342
# Nicolas Ramalho Franco - RM572939
# Lucas Lima Cruz - RM572047

print("""
    ================================================
    Calculadora de Tarifas de Transporte
    ================================================

    Tarifa Base: R$2,50 por quilômetro percorrido.
    Categoria de Passageiros:

    1. Estudante -> 50% de desconto no valor total.
    2. Trabalhador -> 20% de desconto no valor total.
    3. Idoso -> Passagem gratuita.
    4. Comum -> Sem desconto.
""")
opc = input("Digita a sua categoria: ")
match opc:
    case "1":
        print("Categoria Estudante:")
        distancia_es = float(input("Digite a quilômetragem que irá percorrer: "))
        valor_es = distancia_es * 2.50 * 0.5
        print(f"O valor total ficou R${valor_es: .2f}")
    case "2":
        print("Categoria Trabalhador:")
        distancia_tr = float(input("Digite a quilômetragem que irá percorrer: "))
        valor_tr = distancia_tr * 2.50 * 0.8
        print(f"O valor total ficou R${valor_tr: .2f}")
    case "3":
        print("Idoso:")
        print("Independete da quilômetragem a passagem é gratuita.")
    case "4":
        print("Categoria Comum:")
        distancia_cm = float(input("Digite a quilômetragem que irá percorrer: "))
        valor_cm = distancia_cm * 2.50
        print(f"O valor total ficou R${valor_cm: .2f}")
    case _:
        print("Opção inválida.\nSaindo...")