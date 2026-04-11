#loop while - repete um trecho do programa enquanto uma determinada condicao for verdadeira

'''#while 1 == 1:
    print("EITA")'''

resposta = ""
tentativas = 0
while resposta != "python":
    resposta = input("Digite a senha secreta: ")
    tentativas += 1
print("A senha correta foi digitada.")
print(f"Foram digitados {tentativas} tentativas até acerta a senha secreta, burrao kkkkk")
