import os
os.system("cls")

idade = int(input("Digite a idade: "))
ano_atual = int(input("Digite o ano atual: "))

idade_2035 = idade + (2035 - ano_atual)

print("Em 2035 você terá", idade_2035, "anos.")