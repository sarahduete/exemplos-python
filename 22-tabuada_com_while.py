import os
os.system("cls")

numero = int(input("Digite um número: "))

#contador = i
limite_da_tabuada = int(input("Digite o limite da tabuada: "))

contador = 0
while(contador <= limite_da_tabuada):
    print (f"{numero} x {contador} = {numero * contador}")
    contador+=1

