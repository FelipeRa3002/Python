from datetime import datetime
from os import system , getlogin
import dados
""""
 Aqui vão ficar a funções que o corpo.py vai chamar para o código funcionar e também as mudanças da
 variaveis que estão em dados.py 
 input("Pressione Enter para continuar...")
 ({'nome':nome,'nota1':nota1,'nota2':nota2,'media':media,'situação':situacao},)
 \007 faz som
 url para a página do projeto é 
 https://encurtador.com.br/gKJl
 
 https://shre.ink/projetodepython

 https://felipera3002.github.io/Python/Python%20coisas%20simples/Trabalho%20de%20Python/Segundo%20Trabalho/Explica%C3%A7%C3%B5es/Texto%20para%20colocar%20em%20um%20poss%C3%ADvel%20site/index.html
"""
def TrocardoArquivoDados():
    try:
        system('move "%USERPROFILE%\Downloads\dados.py" .')
    except:
        system('mv ~/Downloads/dados.py .')

if len(dados.listadaTurma) > 0 :
    dados.mediadaTurmaDefinitiva=float(dados.mediadaTurmaDefinitiva)/len(dados.listadaTurma)
mediadaTurma=float(dados.mediadaTurmaDefinitiva)
def limpa():
    system("cls")
def Check(x,y):
    if x == 'int':
        try : return bool(int(y))
        except ValueError: return False
def Inclusao():
    global mediadaTurma
    limpa()
    print("Aqui você vai digitar os dados do aluno que você deseja incluir")
    nome = input("\033[35mDigite o nome do Aluno: \033[0m") 
    nota1 = float(input("\033[35mDigite a nota que o Aluno tirou na primeira prova: \033[0m"))
    nota2 = float(input("\033[35mDigite a nota que o Aluno tirou na segunda prova: \033[0m"))
    media = (nota1+nota2)/2
    situacao = "\033[34mAPROVADO\033[0m" if media>=6 else "\033[31mREPROVADO\033[0m"
    mediadaTurma+=media
    conteudo = {'nome':nome,'nota1':nota1,'nota2':nota2,'media':media,'situação':situacao}
    dados.listadaTurma.append(conteudo)
    input("Pressione Enter para continuar...")

def Consultar():
    global mediadaTurma
    limpa()
    print(
        """
        𝚅𝚘𝚌ê 𝚝𝚎𝚖 𝚍𝚞𝚊𝚜 𝚘𝚙çõ𝚎𝚜 𝚍𝚎 𝚌𝚘𝚗𝚜𝚞𝚕𝚝𝚊𝚛 
        𝟷 - 𝙿𝚎𝚕𝚘 𝚗𝚘𝚖𝚎
        𝟸 - 𝙰𝚙𝚛𝚘𝚟𝚊𝚍𝚘 𝚘𝚞 𝚁𝚎𝚙𝚛𝚘𝚟𝚊𝚍𝚘
        """
          )
    try:
        desicao = int(input("\033[94mDigite o número que representa a ação que você deseja realizar: \033[0m"))
    except ValueError:
        controleDeFluxo = False
        while controleDeFluxo == False:
            limpa()
            print(
                """
                𝚅𝚘𝚌ê 𝚝𝚎𝚖 𝚍𝚞𝚊𝚜 𝚘𝚙çõ𝚎𝚜 𝚍𝚎 𝚌𝚘𝚗𝚜𝚞𝚕𝚝𝚊𝚛 
                𝟷 - 𝙿𝚎𝚕𝚘 𝚗𝚘𝚖𝚎
                𝟸 - 𝙰𝚙𝚛𝚘𝚟𝚊𝚍𝚘 𝚘𝚞 𝚁𝚎𝚙𝚛𝚘𝚟𝚊𝚍𝚘
                """
          )
            print("Número inteiro, conjunto real, sabe irmão 1 2 3 4.... e não letras")
            desicao =input("\033[94mDigite o número que representa a ação que você deseja realizar: \033[0m")
            controleDeFluxo = Check(x="int",y=desicao)
            if controleDeFluxo:
                desicao = int(desicao)


        
    listadeNome = []
    if desicao == 1:
        nome = input("Digite o nome do Aluno: ")
        for i in dados.listadaTurma:
            listadeNome.append(i['nome'])
        if nome in listadeNome:
            for i in dados.listadaTurma:
                if nome == i['nome']:
                    print(f"O aluno {i['nome']} , tirou {i['nota1']:.1f} na primeira prova e na segunda prova tirou {i['nota2']:.1f} . A sua média foi de {i['media']:.1f} e ele foi {i['situação']}")
        else:
            print("Não tem um aluno com esse nome")

    elif desicao == 2:
        x=1
        texto= ""
        situacao = input("\033[94mDesejar ver os Aprovado ou Reprovado: \033[0m").lower()
        if situacao in ("aprovado","reprovado"):
            situacao = "\033[34mAPROVADO\033[0m" if situacao=="aprovado" else "\033[31mREPROVADO\033[0m"
        for i in dados.listadaTurma:
            if i['situação'].lower() in ("aprovado","reprovado"):
                i['situação'] = "\033[34mAPROVADO\033[0m" if i['situação'].lower()=="aprovado" else "\033[31mREPROVADO\033[0m"
        for i in dados.listadaTurma:
            if situacao.upper() == i['situação'].upper():
                texto+= f"{x} - {i['nome']}\n"
                x+=1
        print(f"""
            Teve {x} alunos {situacao}
            ==========================
            {texto}
            ==========================
            a média da turma foi de {mediadaTurma/len(dados.listadaTurma):.1f}
            """)
    
    else:
        print("\007Opção não válida")
    input("Pressione Enter para continuar...")

def Relatorio(x):
    global mediadaTurma
    user = getlogin()
    data = f"{datetime.now().strftime('%d/%m/%Y')}"
    if x == "txt":
        with open("Relatório.txt", "w+", encoding="utf-8") as blueLock:
            contador=1
            texto=f"Relatório da turma feito no dia {data} , pelo {user}\n"
            for i in dados.listadaTurma:
                texto+= f"{contador} - Nome: {i['nome']} - Sua nota da AV: {i['nota1']:.1f} e na AVS: {i['nota2']:.1f} - {i['situação']} com média de {i['media']:.1f}\n"
                contador+=1
            texto+= f"A média da turma no geral foi de {mediadaTurma/len(dados.listadaTurma):.1f} , turma {'APROVADO' if mediadaTurma/len(dados.listadaTurma)>=6 else 'REPROVADO'}\n"
            blueLock.write(texto)
    if x == "python":
        with open("dados.py", "w+" , encoding="utf-8") as Kaiser:
            contador = 1
            texto = ""
            for i in dados.listadaTurma:
                if contador == 1 :
                    texto = f"{{'nome': '{i['nome']}', 'nota1': {i['nota1']}, 'nota2': {i['nota2']}, 'media': {i['media']}, 'situação': '{i['situação']}'}}"
                else:
                    texto += f", {{'nome': '{i['nome']}', 'nota1': {i['nota1']}, 'nota2': {i['nota2']}, 'media': {i['media']}, 'situação': '{i['situação']}'}}"
                contador+=1
            # O segredo está nas aspas simples em '%H:%M:%S'
            Kaiser.write(f"# Foi modificado no dia {data} às {datetime.now().strftime('%H:%M:%S')} pelo {user}\nlistadaTurma = [{texto}]\nmediadaTurmaDefinitiva= {mediadaTurma:.1f}")


def AtualizarDado():
  global mediadaTurma
  limpa()
  print("Aqui você vai atualizar o dado de algum aluno")
  contador = 1
  for i in dados.listadaTurma:
    print(f"{contador} - {i['nome']}")
    contador+=1
  desicao=int(input("Digite o número que representa o nome do aluno que você deseja mudar: "))
  index = desicao - 1
  print("Digite 1 para mudar nome\nDigite 2 para mudar a nota 1\nDigite 3 para mudar a nota 2")
  desicao=int(input("Digite o número que representa o nome do aluno que você deseja mudar: "))
  if desicao == 1:
      novoNome = input(f"Digite um novo nome para {dados.listadaTurma[index]['nome']}: ")
      dados.listadaTurma[index]['nome']=novoNome
  elif desicao == 2:
      novaNotadaAV = float(input("\033[94mDigite a nova nota pra primeira prova: \033[0m"))
      dados.listadaTurma[index]['nota1']=novaNotadaAV
      media = float(dados.listadaTurma[index]['media'])
      mediadaTurma-=media
      novaMedia= (float(dados.listadaTurma[index]['nota1'])+ float(dados.listadaTurma[index]['nota2']))/2
      dados.listadaTurma[index]['media'] = novaMedia
      mediadaTurma+=novaMedia
      situacao = "\033[34mAPROVADO\033[0m" if novaMedia>=6 else "\033[31mREPROVADO\033[0m"
      dados.listadaTurma[index]['situação'] = situacao
  elif desicao == 3:
      novaNotadaAVs = float(input("\033[94mDigite a nova nota pra segunda prova: \033[0m"))
      dados.listadaTurma[index]['nota2']=novaNotadaAVs
      media = float(dados.listadaTurma[index]['media'])
      mediadaTurma-=media
      novaMedia= (float(dados.listadaTurma[index]['nota1'])+ float(dados.listadaTurma[index]['nota2']))/2
      dados.listadaTurma[index]['media'] = novaMedia
      mediadaTurma+=novaMedia
      situacao = "\033[34mAPROVADO\033[0m" if novaMedia>=6 else "\033[31mREPROVADO\033[0m"
      dados.listadaTurma[index]['situação'] = situacao
  input("Pressione Enter para continuar...")

def Apagar(x):
    global mediadaTurma
    limpa()
    if x == 0:
        print("Aqui você vai apagar um aluno")
        contador = 1
        for i in dados.listadaTurma:
            print(f"{contador} - {i['nome']}")
            contador+=1
        desicao=int(input("Digite o número que representa o nome do aluno que você deseja apagar: "))
        index = desicao - 1
        dadosTemp = dados.listadaTurma[index]
        dados.listadaTurma.pop(index)
        print(f"O Aluno {dadosTemp['nome']} foi apagado")
        mediaApagada = dadosTemp['media']
        mediadaTurma-= mediaApagada
    if x == 1:
        desicao = input("Tem certeza que quer apagar tudo: [S/N]").upper()
        if desicao in ("S","SIM"):
            dados.listadaTurma.clear()
            mediadaTurma = 0
        elif desicao in ("NÃO","NAO","N"):
            print("\033[95mAonde você comprou o teclado não vendia coragem também?\n \nO lugar mais seguro da cidade é na frente da sua mira.\033[0m")

    input("Pressione Enter para continuar...")

def MostraSite():
    try:
        system("start https://shre.ink/projetodepython")
    except:
        system("xdg-open https://shre.ink/projetodepython")
def Menu():
    global mediadaTurma
    while True:
        limpa()
        print(
            """
            ===================== 𝓜𝓮𝓷𝓾 𝓟𝓻𝓲𝓷𝓬𝓲𝓹𝓪𝓵 ===================== 
            1)𝓘𝓷𝓬𝓵𝓾𝓼𝓪̃𝓸 
            2)𝓒𝓸𝓷𝓼𝓾𝓵𝓽𝓪𝓻 
            3)𝓡𝓮𝓵𝓪𝓽𝓸𝓻𝓲𝓸 
            4)𝓐𝓽𝓾𝓪𝓵𝓲𝔃𝓪𝓻 𝓭𝓪𝓭𝓸𝓼 
            5)𝓔𝔁𝓬𝓵𝓾𝓲𝓻 𝓪𝓵𝓾𝓷𝓸𝓼 
            6)𝓔𝔁𝓬𝓵𝓾𝓲𝓻 𝓽𝓾𝓭𝓸
            7)Mostrar o Site
            8)Atualizar o arquivo dados.py 
            9)𝓢𝓪𝓲𝓻
            """
        )
        try:
                desicao = int(input("\033[94mDigite o número que representa a ação que você deseja realizar: \033[0m"))
        except ValueError:
                controleDeFluxo = False
                controleDeReacao = 1
                while controleDeFluxo == False:
                    limpa()
                    print(
                         """
                            ===================== 𝓜𝓮𝓷𝓾 𝓟𝓻𝓲𝓷𝓬𝓲𝓹𝓪𝓵 ===================== 
                            1)𝓘𝓷𝓬𝓵𝓾𝓼𝓪̃𝓸 
                            2)𝓒𝓸𝓷𝓼𝓾𝓵𝓽𝓪𝓻 
                            3)𝓡𝓮𝓵𝓪𝓽𝓸𝓻𝓲𝓸 
                            4)𝓐𝓽𝓾𝓪𝓵𝓲𝔃𝓪𝓻 𝓭𝓪𝓭𝓸𝓼 
                            5)𝓔𝔁𝓬𝓵𝓾𝓲𝓻 𝓪𝓵𝓾𝓷𝓸𝓼 
                            6)𝓔𝔁𝓬𝓵𝓾𝓲𝓻 𝓽𝓾𝓭𝓸
                            7)Mostrar o Site
                            8)Atualizar o arquivo dados.py 
                            9)𝓢𝓪𝓲𝓻
                         """
                        )
                    if controleDeReacao <=10:
                        print("Número inteiro, conjunto real, sabe irmão 1 2 3 4.... e não letras")
                    elif controleDeReacao>10 and controleDeReacao <20:
                        print(f"""\033[31m
                                Olha, papo reto: você realmente sabe o que é um número inteiro? 
                                Porque do jeito que a coisa vai, tô começando a achar que você faltou a essa aula no primário. 😂
                                na tentativa de número 20 eu vou parar. estamos na tentativa de número {controleDeReacao}
                            \033[0m""")
                    else:
                        desicao = 0
                        break
                    desicao =input("\033[94mDigite o número que representa a ação que você deseja realizar: \033[0m")
                    controleDeFluxo = Check(x="int",y=desicao)
                    if controleDeFluxo:
                        desicao = int(desicao)
                    controleDeReacao+=1
        if desicao == 0:
            limpa()
            print("Eu Avisei")
            system("start https://www.youtube.com/watch?v=MxRvYKxCswE")
            return "sair"
            break
        elif desicao == 1:
            Inclusao()
        elif desicao == 2:
            Consultar()
        elif desicao == 3:
            Relatorio(x="txt")
        elif desicao == 4:
            AtualizarDado()
        elif desicao == 5:
            Apagar(x=0)
        elif desicao == 6:
            Apagar(x=1)
        elif desicao == 7:
            MostraSite()
            Relatorio(x="python")
            break
        elif desicao == 8:
            Relatorio(x="python")
            TrocardoArquivoDados()
            return "reiniciar"
            break
        elif desicao == 9:
            Relatorio(x="python")
            return "sair"
            break


   
