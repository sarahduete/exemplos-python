import os
os.system("cls")

nivel = int(input("Digite o seu nível (1, 2 ou 3): "))
aulas_semana = int (input ("Digite a quantidade de aula por semana: "))

if nivel == 1:
   valor_hora = 12

elif nivel == 2:
    valor_hora = 17

elif nivel == 3:
   valor_hora = 25
   
salario = aulas_semana * valor_hora * 4

print("Salário final do professor: R$", salario)


