import os
os.system ("cls")

#Criando a primeira função
def escreva():
    print ("Olá Mundo")

#Chamando a função
escreva()

#Criando uma função com parametro
def exibir_dados(nome,idade,email):
    print (f"Nome: {nome}")
    print (f"Idade: {idade}")
    print (f"Email: {email}")
    print ("=" * 100)

#Chamando a função escreva
escreva()
#Chamando a função exibir_dados
exibir_dados("Sarah", 16, "sarah.duete@gmail.com")
exibir_dados("Caio", 38, "caio@gmail.com")

#Criando uma função com retorno
def somar (num1,num2):
    resultado = num1 + num2
    return resultado 

#Chamando a função com retorno
total = somar (10,20)
print(f"O total será: {somar(10,20)}")

