import os
os.system("cls")
import random

print ("Bem-Vindo ao Pokémon")

adversario = 100
jogador1 = 100

turno = "jogador"
computador_fugiu = False
jogador_fugiu =  False

while jogador1 > 0 and adversario> 0 and computador_fugiu == False and jogador_fugiu ==  False:

    if turno == "jogador":
        print ("Seu Turno!")

    acao = input("Escolha se você irá, Atacar, Curar ou Fugir:").upper()
    
    if (acao == "ATACAR"):
        adversario = adversario - 10
        print (f"Você Atacou. A vida do adversário ficou {adversario}")
    
    elif (acao == "CURAR"):
        jogador1 = jogador1 + 5
        print(f"Você se curou, sua vida é de {jogador1}")
    
    elif (acao == "FUGIR"):
        print(f"Você Fugiu!")
        jogador_fugiu = True
        break
    
    else:
        print ("Digite apenas uma das 3 opções")

    turno = "inimigo"

    print("Turno do inimigo")
    input("Pressione enter para continuar.....")

    inimigo = random.choice(["Atacar", "Cura", "Fugir"])
    print(f"Inimigo escolher: {inimigo}")

    if (inimigo == "Atacar"):
        jogador1 - 10
        print ("O inimigo te atacou!")
    elif (inimigo == "Cura"):
        adversario + 5
    elif (inimigo == "Fugir"):
        print ("O inimigo Fugiu")
        computador_fugiu = True

    turno = "jogador"

print (f"Sua vida: {jogador1}")
print (f"Vida do inimigo: {adversario}")
if (jogador1 > adversario):
    print ("Você ganhou!")

else:
    print ("Você Perdeu!")