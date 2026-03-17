import os
os.system("cls")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso / (altura * altura)

if IMC < 16.9:
    print ("Muito abaixo do peso")

elif IMC >= 17 and IMC <= 18:
    print ("Abaixo do peso")

elif IMC >= 18.5 and IMC <= 24.9:
    print ("Peso normal")

elif IMC >= 25 and IMC <= 29.9:
    print ("Acima do peso")

elif IMC >= 30 and IMC <= 34.9:
    print ("Obesidade grau I")

elif IMC >= 35 and IMC <= 40:
    print ("Obesidade grau II")

else:
    ("Obesidade grau III")
    
  