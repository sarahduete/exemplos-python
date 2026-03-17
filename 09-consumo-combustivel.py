import os
os.system("cls")

km = float(input("Digite os quilômetros percorridos: "))
litros = float(input("Digite os litros de combustível gastos: "))

consumo = km / litros

print ("O consumo médio do veículo em km por litro foi:", consumo)
