from os import system
from random import randint
from getpass import getpass
def limpatela():
    system("cls")
def CadastroLoja():
    Nome_da_Loja_a_ser_Cadastro = input("Digite o nome da sua Loja:   ")
    limpatela()
    print("Moda e Acessórios: Lojas de roupas, calçados, bolsas e acessórios, como Zara, Renner e C&A.\nEletrônicos e Tecnologia: Lojas de eletrônicos, celulares e informática, como Fast Shop e Casas Bahia.\nAlimentação: Praças de alimentação com restaurantes, fast foods e cafés, como Outback Steakhouse e Starbucks.\nSaúde e Beleza: Farmácias, perfumarias e salões de beleza, como O Boticário e Sephora.\nLazer e Entretenimento: Cinemas, boliches e parques de diversão, como UCI Kinoplex e Hotzone.\nServiços: Bancos, correios e consertos de roupas, como Conserte1.\nCasa e Decoração: Lojas de móveis e artigos para o lar, como Tok & Stok e Camicado.")
    Categoria_da_Loja = input("Digite a Cartegoria da sua loja:  ").upper()
    Senha = str(input("Digite uma senha:   "))
    while True:
               limpatela()
               Produto = input("Digite o nome do Produto:  ")
               Descricao = input(f"Descrição de {Produto}:   ")
               Valor = float(input(f"Valor de {Produto}:   "))
               Dados_dos_Produtos = {'Produto' : Produto,'Descricao' : Descricao,'Valor' : Valor}
               Lista_dos_Produtos.append(Dados_dos_Produtos)
               continua = input("Digite \n1 para Cadastrar \n0 para Parar:   ")
               if continua == "0" or continua == "O" or continua == "o":
                     break
    Dados_da_Loja = {'NomeLoja': Nome_da_Loja_a_ser_Cadastro , 'Categoria_da_Loja' : Categoria_da_Loja , 'Produtos_da_loja': Lista_dos_Produtos, 'Senha' : Senha }
    print(Dados_da_Loja['Produtos_da_loja'])
    Lojas.append(Dados_da_Loja)
    menu()
def ListarLojas(x):
      if x==0:
         posicao = 1
         print("As lojas registrada no [Nome_do_Shopping]")
         for i in Lojas:
             senha = len(i['Senha'])
             senha = "*" * senha
             print(f"{posicao} - Nome: {i['NomeLoja']}  -  Categoria: {i['Categoria_da_Loja']} senha:{senha} ||Tamanho da senha {len(i['Senha'])} caracteres")
             posicao+=1
         input()
      elif x == 1:
             for i in Lojas:
                    print(f"{i['NomeLoja']}  - Categoria {i['Categoria_da_Loja']}")
                    y = i['Produtos_da_loja']
                    print("="*15)
                    posicao =1
                    for l in y:
                           preco = f"R${l['Valor']:_.2f}"
                           preco = preco.replace('.',',').replace('_','.')
                           print(f"{posicao} - Nome: {l['Produto']}   Descrição: {l['Descricao']}      Preço: {preco}")
                           posicao+=1
                    print("="*15)
                    input()
      elif x == 2:
             posicao = 1
             print("As lojas registrada no [Nome_do_Shopping]")
             for i in Lojas:
               print(f"{posicao} - Nome: {i['NomeLoja']}   Categoria: {i['Categoria_da_Loja']}")
               posicao+=1
             decisao = int(input("Digite o número corresponde o nome da loja que você deseja ver os produtos:  "))
             limpatela()
             decisao = decisao - 1
             y = Lojas[decisao]
             print(f"{y['NomeLoja']}")
             y = y['Produtos_da_loja']
             posicao = 1
             print("="*15)
             for l in y:
                    preco = f"R${l['Valor']:_.2f}"
                    preco = preco.replace('.',',').replace('_','.')
                    print(f"{posicao} - Nome: {l['Produto']}   Descrição: {l['Descricao']}      Preço: {preco}")
                    posicao+=1
             print("="*15)
             input()
      elif x == 3:
            posicao = 1
            print("As lojas registrada no [Nome_do_Shopping]")
            for i in Lojas:
                print(f"{posicao} - Nome: {i['NomeLoja']}  -  Categoria: {i['Categoria_da_Loja']} senha:{i['Senha']}  || Tamanho da senha {len(i['Senha'])} caracteres")
                posicao+=1
            input()
      menu()
def Mudaritens(x):
    print("Digite o número corresponde o nome da loja que você deseja mudar")
    posicao= 1
    for i in Lojas:
            print(f"{posicao} - Nome: {i['NomeLoja']}")
            posicao+=1
    Numero_da_Loja_que_Vai_algo_pra_mudar = int(input("\n Qual é o número:  "))
    Item_a_mudar = Numero_da_Loja_que_Vai_algo_pra_mudar - 1
    Item_a_mudar = Lojas[Item_a_mudar]
    Senha_do_item = Item_a_mudar['Senha']
    nomeloja=Item_a_mudar['NomeLoja']
    if x == 1:
            limpatela()
            Novo_nome = input(f"O vai ser o novo nome para Loja {Item_a_mudar['NomeLoja']}:  ")
            print(f"Vai de {Item_a_mudar['NomeLoja']} para  {Novo_nome}")
            decisao = input("Digite 1 para confirmar a alteração\nDigite 0 para negar a alteração: ")
            if decisao == "1":
               sd = getpass(f"Digite a Senha da loja {Item_a_mudar['NomeLoja']} # ")
               a = randint(0,2)
               a = Palavras_chaves[a]
               CheckSenha(Senha_do_item,sd,a)
               Item_a_mudar['NomeLoja'] = Novo_nome
            else:
                  print("Quem sabe")
    elif x == 2:
          input(f"A categoria da loja {Item_a_mudar['NomeLoja']} é de {Item_a_mudar['Categoria_da_Loja']}")
          limpatela()
          print("Moda e Acessórios: Lojas de roupas, calçados, bolsas e acessórios, como Zara, Renner e C&A.\nEletrônicos e Tecnologia: Lojas de eletrônicos, celulares e informática, como Fast Shop e Casas Bahia.\nAlimentação: Praças de alimentação com restaurantes, fast foods e cafés, como Outback Steakhouse e Starbucks.\nSaúde e Beleza: Farmácias, perfumarias e salões de beleza, como O Boticário e Sephora.\nLazer e Entretenimento: Cinemas, boliches e parques de diversão, como UCI Kinoplex e Hotzone.\nServiços: Bancos, correios e consertos de roupas, como Conserte1.\nCasa e Decoração: Lojas de móveis e artigos para o lar, como Tok & Stok e Camicado.")
          Nova_Categoria_da_Loja = input("Digite a Cartegoria da sua loja:  ").upper()
          print(f"Vai de {Item_a_mudar['Categoria_da_Loja']} para  {Nova_Categoria_da_Loja}")
          decisao = input("Digite 1 para confirmar a alteração\n Digite 0 para negar a alteração")
          if decisao == "1":
               sd = getpass(f"Digite a Senha da loja {Item_a_mudar['NomeLoja']} # ")
               a = randint(0,2)
               a = Palavras_chaves[a]
               CheckSenha(Senha_do_item,sd,a)
               Item_a_mudar['Categoria_da_Loja'] = Nova_Categoria_da_Loja
          else:
                  print("Quem sabe")
    elif x == 3:
          limpatela()
          Item_a_mudar = Item_a_mudar['Produtos_da_loja']
          posicao= 1
          for i in Item_a_mudar:
                print(f"{posicao} - Nome do Produto {i['Produto']}")
                posicao+=1
          Numero_do_Produto_que_Vai_algo_pra_mudar = int(input("\n Qual é o número que corresponde o Produto:  "))
          n = Numero_do_Produto_que_Vai_algo_pra_mudar - 1
          Item_a_mudar = Item_a_mudar[n]
          n = int(input("Digite 2 para Mudar o nome\nDigite 4 para Mudar a descrição do Produto\nDigite 6 para Mudar o valor do produto:  "))
          if n == 2:
                Novo_nome = input("Digite um novo nome para o Produto:  ")
                print(f"Vai de {Item_a_mudar['Produto']} para  {Novo_nome}")
                decisao = input("Digite 1 para confirmar a alteração\n Digite 0 para negar a alteração")
                if decisao == "1":
                          sd = getpass(f"Digite a Senha da loja {nomeloja} # ")
                          a = randint(0,2)
                          a = Palavras_chaves[a]
                          CheckSenha(Senha_do_item,sd,a)
                          Item_a_mudar['Produto'] = Novo_nome
                else:
                          print("Quem sabe")
          elif n == 4:
                Novo_Descricao = input("Digite uma nova descrição para o Produto:  ")
                limpatela()
                print(f"Vai de {Item_a_mudar['Descricao']}\n para\n  {Novo_Descricao}")
                decisao = input("Digite 1 para confirmar a alteração\n Digite 0 para negar a alteração")
                if decisao == "1":
                          sd = getpass(f"Digite a Senha da loja {nomeloja} # ")
                          a = randint(0,2)
                          a = Palavras_chaves[a]
                          CheckSenha(Senha_do_item,sd,a)
                          Item_a_mudar['Descricao'] = Novo_Descricao
                else:
                          print("Quem sabe")
          elif n == 6:
                 Novo_Valor = float(input("Digite um novo valor para o Produto:  "))
                 print(f"Vai de {Item_a_mudar['Valor']}\n para\n  {Novo_Valor}")
                 decisao = input("Digite 1 para confirmar a alteração\n Digite 0 para negar a alteração")
                 if decisao == "1":
                          sd = getpass(f"Digite a Senha da loja {nomeloja} # ")
                          a = randint(0,2)
                          a = Palavras_chaves[a]
                          CheckSenha(Senha_do_item,sd,a)
                          Item_a_mudar['Valor'] = Novo_Valor
                 else:
                          print("Quem sabe")
    elif x ==4:
       limpatela()
       Nova_senha = input(f"O vai ser a nova senha para Loja {Item_a_mudar['NomeLoja']} ##:  ")
       print(f"\nA nova senha vai ser {Nova_senha}")
       decisao = input("Digite 1 para confirmar a alteração\nDigite 0 para negar a alteração: ")
       if decisao == "1":
           Item_a_mudar['Senha'] = Nova_senha
       elif decisao == "0" or decisao == "O":
             Controle_de_fluxo = 1
             vezes_feita = 1
             while Controle_de_fluxo == 1:
                   decisao = int(input("Digite 2 caso você quer digitar outra coisa no lugar da senha\nDigite 4 caso você mudou de ideia sobre mudara senha: "))
                   if decisao == 4:
                         Controle_de_fluxo+=1
                   elif decisao == 2:
                     Nova_senha = input(f"O vai ser a nova senha para Loja {Item_a_mudar['NomeLoja']} ##:  ")
                     print(f"\n a nova senha vai ser {Nova_senha}")
                     decisao = input("Digite 1 para confirmar a alteração\n Digite 0 para negar a alteração")
                     if decisao == "1":
                           Item_a_mudar['Senha'] = Nova_senha
                           Controle_de_fluxo+=1
                   elif vezes_feita == 4:
                         Controle_de_fluxo+=1
                   vezes_feita+=1
    menu()
def menu():
       limpatela()
       print("""
                𝐃𝐢𝐠𝐢𝐭𝐞 𝟏 𝐩𝐚𝐫𝐚 𝐯𝐞𝐫 𝐚𝐬 𝐋𝐨𝐣𝐚𝐬 𝐣á 𝐜𝐚𝐝𝐚𝐬𝐭𝐫𝐚𝐝𝐚𝐬

                𝐃𝐢𝐠𝐢𝐭𝐞 𝟐 𝐩𝐚𝐫𝐚 𝐯𝐞𝐫 𝐨𝐬 𝐏𝐫𝐨𝐝𝐮𝐭𝐨𝐬

                𝐃𝐢𝐠𝐢𝐭𝐞 𝟑 𝐩𝐚𝐫𝐚 𝐜𝐚𝐝𝐚𝐬𝐭𝐫𝐚𝐫 𝐮𝐦𝐚 𝐋𝐨𝐣𝐚
                
                𝐃𝐢𝐠𝐢𝐭𝐞 𝟒 𝐩𝐚𝐫𝐚 𝐦𝐮𝐝𝐚𝐫 𝐚𝐥𝐠𝐨
             
                Digite 5 para Apagar algo

                𝐃𝐢𝐠𝐢𝐭𝐞 𝟎 𝐩𝐚𝐫𝐚 𝐟𝐞𝐜𝐡𝐚𝐫 𝐨 𝐩𝐫𝐨𝐠𝐫𝐚𝐦𝐚""")
       decisao = int(input("\n:  "))
       if decisao == 1:
              limpatela()
              x = int(input("Digite 2 para ver as Lojas mas com a senha oculta\nDigite 4 para ver as lojas com as senhas juntos: "))
              if x==2:
               limpatela()
               ListarLojas(0)
              elif x ==4:
                    limpatela()
                    ListarLojas(3)
              else:
                    menu()
       elif decisao == 2:
              tudo = int(input("\nDigite 2 para ver todos os produtos por loja\nDigite 4 para ver os produtos de uma loja em específico:  "))
              if tudo == 2:
                     limpatela()
                     ListarLojas(1)
              elif tudo == 4:
                     limpatela()
                     ListarLojas(2)
              else:
                     menu()
       elif decisao == 3:
              limpatela()
              CadastroLoja()
       elif decisao ==4:
              o_que_fazer = int(input("\nDigite 2 para mudar o nome da loja\nDigite 4 para mudar a categoria da loja\nDigite 6 para mudar algo no produto\nDigite 8 para mudar a Senha: "))
              if o_que_fazer == 2:
                     limpatela()
                     Mudaritens(1)
              elif o_que_fazer == 4: 
                     limpatela()
                     Mudaritens(2)
              elif o_que_fazer == 6:
                     limpatela()
                     Mudaritens(3)
              elif o_que_fazer ==8:
                    limpatela()
                    Mudaritens(4)
              else:
                     menu()
       elif decisao == 0:
              Fim()
       elif decisao == 5:
              limpatela()
              o_que_fazer = int(input("\nDigite 2 para Apagar uma loja\nDigite 4 para Apagar produto de uma loja"))
              if o_que_fazer == 2:
                     limpatela()
                     Apagaritem(0)
              elif o_que_fazer == 4: 
                     limpatela()
                     Apagaritem(1)
              else:
               menu()
       else:
              menu()
def Fim():
       limpatela()
       print("""𝓕𝓲𝓶  𝓭𝓸 𝓟𝓻𝓸𝓰𝓻𝓪𝓶𝓪""")
def Apagaritem(x):
       if x == 0:
            posicao = 1
            for i in Lojas:
               print(f"{posicao} - Nome: {i['NomeLoja']}  -  Categoria: {i['Categoria_da_Loja']}")
               posicao+=1
            numerDalojaqueApagar =int(input("Digite o número da loja que você deseja apagar:  "))
            numerDalojaqueApagar -=1
            Senha_do_item = Lojas[numerDalojaqueApagar]
            nomeloja= Senha_do_item['NomeLoja']
            Senha_do_item = Senha_do_item['Senha']
            decisao = input("Digite 1 para confirmar\nDigite 0 para negar: ")
            if decisao == "1":
               sd = getpass(f"Digite a Senha da loja {nomeloja} # ")
               a = randint(3,5)
               a = Palavras_chaves[a]
               CheckSenha(Senha_do_item,sd,a)
               Lojas.pop(numerDalojaqueApagar)
            else:
                  print("Quem sabe")
       elif x == 1:
             posicao = 1
             for i in Lojas:
                   print(f"{posicao} - Nome: {i['NomeLoja']}") 
                   posicao+=1
             decisao =  int(input("Digite o número da Loja que você tem o produto que você deseja apagar:  ")) 
             decisao -=1
             y = Lojas[decisao]
             Senha_do_item = y['Senha']
             nomeloja = y['NomeLoja']
             print(f"{nomeloja}")
             input()
             y = y['Produtos_da_loja']
             posicao = 1
             for i in y:
                   preco = f"R$ {i['Valor']}"
                   preco = preco.replace('.',',').replace('_','.')
                   print(f"{posicao} - Nome: {i['Produto']} - Descrição: {i['Descricao']} - Preço: {preco}")
                   posicao+=1
             decisao =  int(input("Digite o número do produto que você deseja apagar:  ")) 
             decisao -=1
             Confirmar_ou_negar = input("Digite 1 para confirmar\nDigite 0 para negar: ")
             if Confirmar_ou_negar == "1":
               sd = getpass(f"Digite a Senha da loja {nomeloja} # ")
               a = randint(3,5)
               a = Palavras_chaves[a]
               CheckSenha(Senha_do_item,sd,a)
               y.pop(decisao)
             else:
                   print("Quem sabe")
       menu()
def CheckSenha(x,y,z):
       for i in range(0,3):
              if x ==y:
                    print(f"\nFoi {z} com sucesso !!!!")
                    input()
              elif x!=y and i == 0:
                    y = getpass("Senha errada\nVamos tentar novamente:  ")
              elif x!=y and i == 1: 
                      y = str(input("Senha errada\nVamos tentar novamente:  "))
              elif x!=y and i ==2:
                     x = x.upper()
                     y = y.upper()
                     if x == y:
                           print(f"\nFoi {z} com sucesso !!!!")
                           input() 
                     else:
                         print("\nNão foi possível continuar, por causa que você errou a senha três vezes")
                         input("\n")  

Lista_dos_Produtos = []
Lojas = []

""""Tudo aqui embaixo são dados de base para testes então pode ignorar com sucesso"""
nomes_lojas = ["Loja A", "Loja B", "Loja C"]
categorias_lojas = ["Eletrônicos", "Roupas", "Alimentos"]
produtosele = [
    {'Produto': 'Smartphone', 'Descricao': 'Smartphone de última geração', 'Valor': 2999.99},
    {'Produto': 'Notebook', 'Descricao': 'Notebook com 16GB de RAM e 512GB SSD', 'Valor': 4999.90},
    {'Produto': 'Fone de Ouvido', 'Descricao': 'Fone de ouvido sem fio com cancelamento de ruído', 'Valor': 799.99},
    {'Produto': 'Televisão', 'Descricao': 'Smart TV 4K de 55 polegadas', 'Valor': 3499.90},
    {'Produto': 'Câmera Digital', 'Descricao': 'Câmera digital com lente de 24MP', 'Valor': 1999.99}
]
produtosrou=[ {'Produto': 'Camiseta', 'Descricao': 'Camiseta de algodão', 'Valor': 49.90},
    {'Produto': 'Calça Jeans', 'Descricao': 'Calça jeans masculina', 'Valor': 129.90},
    {'Produto': 'Jaqueta', 'Descricao': 'Jaqueta de couro', 'Valor': 299.99},
    {'Produto': 'Tênis', 'Descricao': 'Tênis esportivo', 'Valor': 199.90},
    {'Produto': 'Vestido', 'Descricao': 'Vestido de verão', 'Valor': 89.90}]
produtosali = [{'Produto': 'Chocolate', 'Descricao': 'Chocolate ao leite', 'Valor': 5.50},
    {'Produto': 'Café', 'Descricao': 'Pacote de café moído 500g', 'Valor': 15.90},
    {'Produto': 'Arroz', 'Descricao': 'Pacote de arroz 1kg', 'Valor': 4.99},
    {'Produto': 'Feijão', 'Descricao': 'Pacote de feijão 1kg', 'Valor': 6.99},
    {'Produto': 'Leite', 'Descricao': 'Caixa de leite 1L', 'Valor': 3.49}]
Senhas = ["senha1segura!", "senha2forte@", "senha3complexa#"]
Palavras_chaves=("mudado","alterado","modificado","apagado","excluído","removido")
g = 9
x= 0
y = len(Senhas) - 1
"""
   print(y)
   input()

"""
a,b,c = categorias_lojas[0],categorias_lojas[1],categorias_lojas[2]
for i in nomes_lojas:
        f = randint(x,y)    
        if categorias_lojas[f] == a:
            Dados_da_Loja = {'NomeLoja': i , 'Categoria_da_Loja' : categorias_lojas[f] , 'Produtos_da_loja': produtosele, 'Senha' : Senhas[f]}
        elif categorias_lojas[f] == b:
            Dados_da_Loja = {'NomeLoja': i , 'Categoria_da_Loja' : categorias_lojas[f] , 'Produtos_da_loja': produtosrou , 'Senha' : Senhas[f]}
        elif categorias_lojas[f] == c:
            Dados_da_Loja = {'NomeLoja': i , 'Categoria_da_Loja' : categorias_lojas[f] , 'Produtos_da_loja': produtosali, 'Senha' : Senhas[f] }
        print(len(categorias_lojas))
        categorias_lojas.pop(f)
        Senhas.pop(f)
        y-=1
        Lojas.append(Dados_da_Loja)
del a,b,c,x,y,f,g,nomes_lojas,categorias_lojas,produtosele,produtosrou,produtosali,Senhas,Dados_da_Loja
menu()