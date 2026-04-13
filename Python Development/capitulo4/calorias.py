print("CALORIAS")
refeicoes = []
calorias = []
resp = ""
while resp.upper() != "NÃO":
    refeicao = input("Que tipo de refeicão você comeu? ")
    refeicoes.append(refeicao) # .append adiciona algo depois da lista ser criada
    caloria = int(input("Quantas calorias você consumiu nessa refeição? "))
    calorias.append(caloria) # .append adiciona algo depois da lista ser criada
    resp = input("Deseja informar as calorias de mais uma refeicão? [SIM/NÃO] ").upper()

cont = 1
total = 0
for caloria, refeicao in zip (calorias, refeicoes):
    print(f"Na {cont} refeição, você comeu {refeicao} que totalizou {caloria} calorias.")
    cont += 1
    total = total + caloria
print(calorias)
print(f"Foram totalizados {total} calorias.")