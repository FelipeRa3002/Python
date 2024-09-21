from random import uniform,randrange
from os import system
import datetime
#Um código simples de Cadastro de Aluno e suas notas,e ver se ele foi aprovado ou não. também pode cadastrar um professor.
def limpa():
    system("cls")
def CadastroAluno():
    nome = str(input("Qual é o nome do Aluno: "))
    p1= float(input("Qual foi a sua nota na primeira prova: "))
    p2= float(input("Qual foi a sua nota na segunda prova: "))
    media = (p1+p2)/2
    honesto = True if media <=10.0 and media>=0 else False
    while honesto == False:
        motivo = "superior a 10" if media>10 else "inferior a 0"
        print(f"Não possível que você tenha uma média que seja {motivo}")
        p1= float(input("Qual foi a sua nota na primeira prova: "))
        p2= float(input("Qual foi a sua nota na segunda prova: "))
        media = (p1+p2)/2
        honesto = True if media <=10.0 and media>=0 else False
    situacao = "Aprovado" if media>= 6.0 else "Não Aprovado"
    DadosAlunos = {"Nome":nome, "Primeira Prova":p1, "Segunda Prova":p2,"Media":media,"Situacao":situacao}
    ListaAlunos.append(DadosAlunos)
def LeituiraCadastro():
    posicao = 1
    x= 0
    Aprovados = 0
    NaoAprovados = 0
    mediaTurma = 0
    limpa()
    for i in ListaAlunos:
        print(f"{posicao} - {i['Nome']}  :  Notas provas Primeira: {i['Primeira Prova']:.1f} Segunda: {i['Segunda Prova']:.1f} . A média do {i['Nome']} é de {i['Media']:.1f} e portanto o Aluno foi {i['Situacao']}")
    
        if i["Situacao"] == "Aprovado":
          Aprovados += 1
        else:
          NaoAprovados += 1
    
        posicao = posicao +1
        mediaTurma = mediaTurma + i["Media"]
        x=x+1
    mediaTurma = mediaTurma / float(x)
    palavraaprovado = "Aprovados" if Aprovados>1 else "Aprovado"
    palavranaoaprovado = "Não Aprovados" if NaoAprovados>1 else "Não Aprovado"
    print(f"\nA Média da Turma foi de {mediaTurma:.1f}, a turma deve {Aprovados} alunos {palavraaprovado} e {NaoAprovados} alunos {palavranaoaprovado}")
def LeituiraProfessor():
    limpa()
    posicao = 1
    for i in ListaProfessor:
        print(f"{posicao} - {i['Nome']} è Professor de {i['Disciplina']}, tem {i['Idade']} anos e sua média como professor é de {i['Media']:.1f}")
        posicao=posicao+1
    continua()
def continua():
       fazer_novamente=str(input("\nVocê deseja continua\n Se sim digite [S/SIM]\n Se não digite [N/NAO]:\n")).upper()
       if fazer_novamente == "S" or fazer_novamente == "SIM" or fazer_novamente == "SI"  or fazer_novamente == "YES":
            menu()
       else:
           limpa()
           print("""𝓕𝓲𝓶  𝓭𝓸 𝓟𝓻𝓸𝓰𝓻𝓪𝓶𝓪""")
def CadastroProfessor():
    y = 1 
    limpa()
    nome = input("Qual è seu Nome: ")
    Ano_de_nascimento = int(input("Qual o Ano que você nasceu : "))
    x = datetime.datetime.now()
    idade = x.year - Ano_de_nascimento
    menordeidade = False if idade >= 18 and idade <65 else True
    while menordeidade:
        motivo = "deu que você tem menos que 18 anos" if idade <18 else "no Brasil a idade da aposentadoria é  de 65"
        print(f"Infelizmente não foi possível continuar o Cadastro pois {motivo},mas eu vou te dar uma segunda caso você tenha digita o ano errado")
        Ano_de_nascimento = int(input("Qual o Ano que você nasceu : "))
        x = datetime.datetime.now()
        idade = x.year - Ano_de_nascimento
        menordeidade = False if idade >= 18 and idade <65 else True
        if idade <18 or idade>=65:
            print("Infelizmente não será possível fazer o seu cadastro")
            input()
            y = 2
            menordeidade = False
    limpa()
    if y == 2:
        menu()
    else:
      posicao = 1
      for i in disciplinas_ti:
          print(f"{posicao} - {i}")
          posicao = posicao + 1
      materia = int(input("Digite o número que corresponde a disciplina que você vai dar aula: "))
      materia = disciplinas_ti[materia - 1]
      cr = float(input("Qual o seu CR(Coeficiente de Rendimento) no final da Faculdade: "))
      honesto = True if cr<=10 else False
      while honesto == False :
          limpa()
          print("Erro!!!!!! Você digitou um valor maior que 10 no CR. Vamos tenta novamente.")
          cr = float(input("Qual o seu CR(Coeficiente de Rendimento) no final da Faculdade: "))
          honesto = True if cr<=10 else False
      DadosProfessor={"Nome":nome,"Idade":idade,"Media":cr,"Disciplina":materia}
      ListaProfessor.append(DadosProfessor)
      menu()

def menu() :
    limpa()
    print("""
            ▌│█║▌║▌║ Menu ║▌║▌║█│▌
           ==============================================
           𝟎 - 𝐏𝐚𝐫𝐚 𝐒𝐚𝐢𝐫 𝐝𝐨 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐚
           𝟏 - 𝐏𝐚𝐫𝐚 𝐂𝐚𝐝𝐚𝐬𝐭𝐫𝐨 𝐝𝐞 𝐀𝐥𝐮𝐧𝐨𝐬 𝐞 𝐍𝐨𝐭𝐚𝐬
           𝟐- 𝐏𝐚𝐫𝐚 𝐋𝐞𝐢𝐭𝐮𝐫𝐚 𝐝𝐨𝐬 𝐀𝐥𝐮𝐧𝐨𝐬 𝐣á 𝐜𝐚𝐝𝐚𝐬𝐭𝐫𝐚𝐝𝐨
           3 - 𝒫𝒶𝓇𝒶 𝒞𝒶𝒹𝒶𝓈𝓉𝓇𝑜 𝒹𝑒 𝓊𝓂 𝓅𝓇𝑜𝒻𝑒𝓈𝓈𝑜𝓇
           4 - 𝒫𝒶𝓇𝒶 𝓋𝑒𝓇 𝑜𝓈 𝓅𝓇𝑜𝒻𝑒𝓈𝓈𝑜𝓇𝑒𝓈 𝒿𝒶 𝒸𝒶𝒹𝒶𝓈𝓉𝓇𝒶𝒹𝑜𝓈
           ===============================================
""")
    decisao = input("""𝓞 𝓺𝓾𝓮̂ 𝓿𝓸𝓬𝓮̂ 𝓺𝓾𝓮𝓻 𝓯𝓪𝔃𝓮𝓻:  """)
    if decisao == "1":
       limpa()
       CadastroAluno()
       menu()
    elif decisao == "2":
       limpa()
       LeituiraCadastro()
       fazer_novamente=str(input("\nVocê deseja continua\n Se sim digite [S/SIM]\n Se não digite [N/NAO]:\n")).upper()
       if fazer_novamente == "S" or fazer_novamente == "SIM" or fazer_novamente == "SI"  or fazer_novamente == "YES":
            menu()
       else:
           limpa()
           print("""𝓕𝓲𝓶  𝓭𝓸 𝓟𝓻𝓸𝓰𝓻𝓪𝓶𝓪""")
    elif decisao == "0" or decisao == "o" or decisao == "O":
        limpa()
        print("""𝓕𝓲𝓶  𝓭𝓸 𝓟𝓻𝓸𝓰𝓻𝓪𝓶𝓪""")
    elif decisao == "3" :
        CadastroProfessor()
    elif decisao == "4" :
        LeituiraProfessor()
    else:
        menu()
ListaAlunos = []
ListaProfessor = []
disciplinas_ti = [ "Introdução à Programação", "Algoritmos e Estruturas de Dados", "Sistemas Operacionais","Banco de Dados",
    "Redes de Computadores","Engenharia de Software","Desenvolvimento Web","Inteligência Artificial","Segurança da Informação",
    "Computação em Nuvem"]
nomes = ["Felipe", "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor"]
for i in nomes:
    fazer = randrange(1,10)
    fazer = fazer %2
    if fazer == 0:
        nome = i
        p1 = uniform(0,10)
        p2 = uniform(0,10)
        media = (p1+p2)/2
        honesto = True if media <=10.0 else False
        while honesto == False:
          p1= uniform(0,10)
          p2= uniform(0,10)
          media = (p1+p2)/2
          honesto = True if media <=10.0 else False
        situacao = "Aprovado" if media>= 6.0 else "Não Aprovado"
        DadosAlunos = {"Nome":nome, "Primeira Prova":p1, "Segunda Prova":p2,"Media":media,"Situacao":situacao}
        ListaAlunos.append(DadosAlunos)
    elif fazer == 1:
        nome = i
        p1 = uniform(0,10)
        p2 = uniform(0,10)
        media = (p1+p2)/2
        honesto = True if media <=10.0 and media >=6.0 else False
        while honesto == False:
          p1= uniform(0,10)
          p2= uniform(0,10)
          media = (p1+p2)/2
          honesto = True if media <=10.0 and media >=6.0 else False
        x = len(disciplinas_ti)
        idade = randrange(18,65)
        posicao = randrange(0,x)
        materia = disciplinas_ti[posicao]
        if materia == " " or materia == "":
           posicao = randrange(0,x)
           materia = disciplinas_ti[posicao] 
        DadosProfessor = {"Nome":nome,"Idade":idade,"Media":media,"Disciplina":materia}
        ListaProfessor.append(DadosProfessor)

        

menu()
