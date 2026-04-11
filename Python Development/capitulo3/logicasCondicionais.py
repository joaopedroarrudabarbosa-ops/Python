a = 10
b = 15

# and - ambos verdade (retorna true)
# or - necessita de apenas 1 verdade (retorna true)
# not - inverte o resultado

teste = a == 10 and b > 3
print(teste)
teste1 = a == 10 or b > 3
print(teste1)
teste2 = a == 9 or b < 3
print(teste2)

usuario = input("Digite o usuario que deseja acessar o sistema: ")
senha = input("Informe a senha de usuario que deseja acessar o sistema: ")
if usuario.upper() == "ADMIN" and senha == "1234":
    print("Acesso do sistema")
else:
    print("Username/Password incorreto! Acesso negado.")