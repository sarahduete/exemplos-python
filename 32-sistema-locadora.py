import os

# ====================
#Pior Filme
# ====================
def pior_filme(filmes):
    return max(filmes, key=lambda item: item ["Média"])

# ====================
#Melhor Filme
# ====================
def melhor_filme(filmes):
    return max(filmes, key=lambda item: item["Média"])

# ====================
#Devolver Filme
# ====================
def devolver_filme():
    os.system("cls")
    print("=== Devolver Filme ===")
    titulo = input("Informe o nome do filme: ")

    for item in filmes:
        if item ["Título"].lower() == titulo.lower(): 
            if not item ["Disponível"] == False:
                print(f"O filme estava com {item['Cliente']}")
            nota = float(input("Dê uma nota de 0 a 10: "))
            item["Avaliações"].append(nota)
            item["Média"] = calcular_media(item["Avaliações"])
            item ["Classificação"] = classificar_filme(item["Média"])
            item["Cliente"] = None
            item["Disponível"] = True
            print("Filme devolvido com sucesso!")
            print(f"A nova média do filme é {item['Média']}")
            input("Pressione Enter para continuar...")
        else:
            print("Esse filme está disponível!")

 

# ====================
#Alugar Filme
# ====================
def alugar_filme(filmes):
    os.system("cls")
    print("=== Alugueis de Filme ===")
    titulo = input("Informe o nome do filme: ")

    for item in filmes:

        if item["Título"].lower == titulo.lower():
            #Filme existe
            if item["Disponível"] == True:
                nome = input ("Informe seu nome: ")
                item["Disponível"] = False
                item["Cliente"] = nome

                print("Filme alugado com Sucesso")
            else:
                print(f"O filme está alugado pelo cliente {item['Cliente']}")

    input("Pressione Enter para continuar...")

# ====================
#CLassificar Filme
# ====================
def classificar_filme(media):
    if(media >8):
        return "Sucesso"
    elif(media >=5):
        return "Regular"
    else:
        return "Flop"

# ====================
#Carcular Média 
# ====================
def calcular_media(avaliacoes):
    if len(avaliacoes) == 0:
        return 0
    
    return round(sum(avaliacoes) / len(avaliacoes),1)

# ====================
#Buscar Filme 
# ====================
def buscar_filme(titulo, filmes):
    filme_encontrado = ""
    for item in filmes:
        if item ["Título"].lower() == titulo.lower():
            filme_encontrado = item
        
    return filme_encontrado

# ====================
#Menu de Cliente 
# ====================
def carregar_menu_cliente():
    while True:
        os.system("cls")
        print("=== Menu Cliente ===")
        print("[1] - Ver Catálogo")
        print("[2] - Buscar Filme")
        print("[3] - Alugar Filme")
        print("[4] - Devolver Filme")
        print("[5] - Voltar ")

        opcao = int(input("Escolha uma opção: "))

        if (opcao == 1):
            os.system("cls")
            exibir_catalogo(filmes)
            input("Pressione Enter para continuar")

        elif (opcao == 2):
            os.system("cls")
            print ("=== Encontre um Filme ===")
            titulo = input ("Digite o nome do Filme: ")
            filme = buscar_filme(titulo, filmes)

            if filme:
                print(f"Filme encontrado: {filme}")
            else: 
                print ("Filme não encontrado")
            
            input("Pressione Enter para continuar")

        elif (opcao == 3):
            alugar_filme(filmes)

        elif (opcao == 4):
            devolver_filme(filmes)

# ====================
#Exibir Catálogo de Filmes
# ====================
def exibir_catalogo(filmes):
    print("=== Catálogo de Filmes ===")

    for item in filmes:
        print(f"Título: {item["Título"]}")
        print(f"Gênero: {item["Gênero"]}")
        print(f"Classsificação: {item["Classificação"]}")
        print(f"Avaliações: {len(item["Avaliações"])}")

        if (item["Disponível"] == True):
            status = "Disponível"
        else:
            status = f"Alugado por {item["Cliente"]}"
        print (f"Status: {status}")
        print("=============================================")

# ====================
#Cadastrar Filme
# ====================
def cadastrar_filme():
    titulo = input("Título do Filme: ")
    genero = input("Gênero: ")
   
    filme = {
       "Título": titulo,
       "Gênero": genero, 
       "Avaliações" : [],
       "Média": 0,
       "Classificação": "Sem avaliações",
       "Disponível": True, 
       "Cliente": None
   }
    return filme

# ====================
#Menu Administrador 
# ====================
def carregar_menu_admin():
    os.system("cls")
    senha = input("Informe a senha do admin: ")

    if (senha != "123"):
        print("Acesso negado!")
        return
    
    while True:
        os.system("cls")
        print("=== Menu ADMIN ===")
        print("[1] - Cadastrar Filme")
        print("[2] - Ver catálogo")
        print("[3] - Top e Flop")
        print("[4]- Voltar")

        opcao = int(input("Escolha uma opção: "))

        if (opcao == 1):
            os.system("cls")
            print("Cadrastro de Filmes")
            filme = cadastrar_filme()
            filmes.append(filme)
            print("Filme cadastrado!")
            input("Pressiona Enter para continuar")


        elif (opcao == 2):
            os.system("cls")
            exibir_catalogo(filmes)
            input("Pressione Enter para continuar")

        elif (opcao == 3):
            os.system("cls")
            print("=== FIlmes Top e Flop ===")
            print(f"Melhor filme:,{melhor_filme(filmes)}")
            print(f"Pior filme: {pior_filme(filmes)}")
            input("Pressione Enter para continuar... ")

        elif (opcao == 4):
            break

# ====================
#Sistema Principal
# ====================

os.system("cls")

#Lista de filmes
filmes = [
    {
        "Título": "Titanic",
        "Gênero": "Romance/Drama",
        "Avaliações": [],
        "Média": 0,
        "Classificação": "Sem avaliações",
        "Disponível": True,
        "Cliente": None
    },
    {
        "Título": "Frozen",
        "Gênero": "Animação",
        "Avaliações": [],
        "Média": 0,
        "Classificação": "Sem avaliações",
        "Disponível": True,
        "Cliente": None
    },
    {
        "Título": "Interstellar",
        "Gênero": "Ficção científica",
        "Avaliações": [],
        "Média": 0,
        "Classificação": "Sem avaliações",
        "Disponível": True,
        "Cliente": None
    },
    {
        "Título": "Gladiator",
        "Gênero": "Ação/Drama",
        "Avaliações": [],
        "Média": 0,
        "Classificação": "Sem avaliações",
        "Disponível": True,
        "Cliente": None
    },
    {
        "Título": "Jurassic Park",
        "Gênero": "Aventura/Ficção",
        "Avaliações": [],
        "Média": 0,
        "Classificação": "Sem avaliações",
        "Disponível": True,
        "Cliente": None
    }
]

while True:
    print("=== Bem-vindo a locadora do sesi ===")
    print("[1]- Entrar como cliente")
    print("[2] - Entrar como administrador")
    print("[3]- Sair")

    opcao = int(input("Escolha uma opção: "))

    #Verificar qual foi a opção escolhida
    if (opcao == 1):
        #Entrou como cliente
        print("Entrou como Cliente")
        carregar_menu_cliente()
    

    elif (opcao ==2):
        #Entrou como administrador
        print("Entrou como Admin")
        carregar_menu_admin()

    elif (opcao == 3):
        #Escolheu sair 

        print ("Obrigado por utilizar o sistema ..")
        print ("Pressione Enter para sair")
        break