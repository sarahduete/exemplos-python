import os
os.system("cls")

nome = input ("Digite seu nome de usuário: ")
senha = int (input("Digite sua senha: "))

if nome == "admin" and senha == 123:
    print ("Acesso liberado")

else:
    print ("Acesso negado")
