
import os
os.system("cls")

# 1 Etapa - Entrada
print("Bem Vindo a Calculadora Virtual")
numero01 = float (input("Digite o primeiro número:"))
operacao = input("Escolha sua operação: ")
numero02 = float (input("Digite o segundo número:"))

# 2 Passo - Processamento 
soma = numero01 + numero02
sub = numero01 - numero02
multi = numero01 * numero02
divi = numero01 / numero02

#se
if operacao  == "+":
    print ("Seu resultado foi: ", soma)
#senão se
elif operacao == "-":
    print ("Seu resultado foi: ", sub)

elif operacao == "*":
    print ("Seu resultado é: ", multi)

elif operacao == "/":
    print ("Seu resultado é: ", divi)

else:
    print("Sua operação é inválida")


 


