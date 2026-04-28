# loop for - repete um trecho do programa com base em um intervalo de valores
# for - para
# in - dentro de
# range - intervalo de valores
# para (variavel) dentro de intervalo de valores(1,11,2):
''''# 1 (primeiro valor do intervalo), 11 (ultimo valor do intervalo)
2 (de quanto em quanto eu vo sair do - primeiro intervalo - e ir ate o ultimo intervalo)'''


for i in range(2,101,2):
    print(i)
    if i == 20:
        break

numero = int(input("Digite um numero que voce gostaria de saber o fatorial: "))
fat = numero
for valor in range(1,numero,1):
    fat = fat * valor
print(f"O fatorial para o numero informado foi {fat}.")
