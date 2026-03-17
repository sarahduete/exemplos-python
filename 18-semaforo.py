import os
os.system("cls")

cor = input ("Digite a cor de um semáforo: ")

if cor == "Verde":
    print ("Pode passar")

elif cor == "Amarelo": 
    print ("Atenção")

elif cor == "Vermelho":
    print ("Pare")

else:
    print ("Cor inválida")
