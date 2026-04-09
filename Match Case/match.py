print("SISTEMA DE NOTAS\n")
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
        print("Opção inválida.\nTente novamente outra opção.")