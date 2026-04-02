import os
os.system("cls")

print ("Bem-Vindo ao Caixa Eletrônico!")
saldo = 1000
escolha = "Sair"

while escolha == "Sair": 
    print("\n=== Caixa Eletrônico ===")
    print("Ver saldo")
    print("Depositar")
    print("Sacar")
    print("Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "Ver saldo":
        print (f"Seu saldo atual é de: R${saldo}")

    elif opcao == "Depositar":
        valor = float (input ("Qual valor você deseja depositar? "))
        input (f"Você confirma depositar {valor}? ")
        print ("Depósito feito!")

    elif opcao == "Sacar":
        valor = input("Digite o valor que deseja sacar: ")
        if valor:
                valor = float(valor)
                if valor <= saldo:
                    saldo -= valor
                    print(f"Saque realizado! Saldo atual: R${saldo}")
                else:
                    print("Saldo insuficiente!")
        else:
                print("Valor inválido! Digite apenas números.")

    elif opcao == "Sair":
        print("Saindo do programa...")
    break
            
            






