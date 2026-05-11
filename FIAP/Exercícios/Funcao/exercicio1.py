def validarNota(nota):
    while nota < 0 or nota > 10:
        nota = float(input("Informe uma nota válida (entre 0 e 10): "))
    return nota1

def media(nota1,nota2):
    media = (nota1 + nota2) / 2
    if media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")

#main
nota1 = float(input("Digite sua 1º nota: "))
nota1 = validarNota(nota1)

nota2 = float(input("Digite sua 2º nota: "))
nota2 = validarNota(nota2)

media(nota1,nota2)
