import os
os.system("cls")

veiculo = (input("Digite o tipo de veículo: "))

if veiculo == "Carro":
    print ("O valor do pedágio correspondente a R$10")

elif veiculo == "Moto":
    print ("O valor do pedágio correspondente a R$5")

elif veiculo == "Caminhão":
    print ("O valor do pedágio correspondente a R$20")

else:
    print ("Tipo inválido")