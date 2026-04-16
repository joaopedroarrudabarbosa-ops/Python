inimigos = [(50, 50), (100, 100), (10,90), (30,25)]

'''#for inimigo in inimigos:
    print(inimigo)
    for coordenada in inimigo:
        print(coordenada)'''

for x, y in inimigos:
    print(f"A posição é X={x} e Y={y}.")
x = int(input("Informe a posição X que deseja arriscar: "))
y = int(input("Informe a posição Y que deseja arriscar: "))
if (x,y) in inimigos:
    inimigos.remove((x, y))
    print("Boa! Você acertou um inimigo.")
else:
    print("Água! Você errou o inimigo.")
print(inimigos)