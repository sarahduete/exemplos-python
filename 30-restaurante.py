import os
os.system("cls")

def dividir_conta(valor_total,numero_pessoas):
    resultado = valor_total / numero_pessoas
    return resultado

def calcular():
    input("==== Pressione Enter para calcular ====")

print("Seja bem vindo ao App Minha Conta!")

valor_total = float(input("Informe o valor da conta: "))
numero_pessoas = int(input("Digite o número de pessoas: "))

calcular()

print (f"Total da conta: R${valor_total}")
print(f"Número de pessoas: {numero_pessoas}")
print(f"Valor por pessoa: R$ {dividir_conta(valor_total,numero_pessoas)}")

