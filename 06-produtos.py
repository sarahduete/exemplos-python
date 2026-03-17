import os
os.system("cls")

descricao = input ("Digite o nome do seu produto: ")
quantidade = int (input ("Digite a quantidade adquirida? "))
preco = float (input("Digite o preço unitário do produto? "))

# cálculo do total sem desconto
total = quantidade * preco

# cálculo do desconto
if quantidade <= 5:
    desconto = total * 0.02

elif quantidade >5 and quantidade <= 10:
    desconto = total * 0.03

elif quantidade > 10:
    desconto = total * 0.05

# total a pagar
total_pagar = total - desconto

print("Produto:", descricao)
print("Total sem desconto: R$", total)
print("Desconto: R$", desconto)
print("Total a pagar: R$", total_pagar)
     