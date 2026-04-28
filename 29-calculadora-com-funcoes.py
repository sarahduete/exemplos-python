import os 
os.system("cls")

def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def subtrair(numero1,numero2):
    resultado = numero1 - numero2
    return resultado

def multiplicar(numero1,numero2):
    resultado = numero1 * numero2
    return resultado

def dividir(numero1,numero2):
    resultado = numero1 / numero2
    return resultado

def encerrar_programa():
    print("Operação inválida!")
    input("Pressione Enter para finalizar...")
    exit()

print("Seja bem vindo a super calculadora 2.0 pro max")

numero1 = int (input("Informe o primeiro número: "))
numero2 = int (input("Informe o segundo número: "))

print("Escolha umda das opções abaixo: ")
print ("[1] - Somar")
print ("[2] - Subtrair")
print ("[3] - Multiplicar")
print ("[4] - Dividir")
opcao = int(input(" Escolha uma opção:"))

if(opcao == 1):
    #Chamar a função Somar
    print (f"A soma é: {somar(numero1, numero2)}")
elif(opcao == 2):
    #Chamar a função Subtrair
    print(f"A subtrção é: {subtrair(numero1,numero2)} ")
elif(opcao == 3):
    #Chamar a função Multiplicar
    print (f"A multiplicação é: {multiplicar(numero1, numero2)}")
if (opcao == 4):
    #Chamar a função Divisão
    print (f"A divição é: {dividir(numero1, numero2)}")

else:
    #Chamar a função encerrar programa
    encerrar_programa