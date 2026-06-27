from datetime import datetime
from os import system , getlogin
import dados, corpo
try:
    global Panel, Table, print, Console, Confirm
    from rich.panel import Panel
    from rich.table import Table
    from rich import print 
    from rich.console import Console
    from rich.prompt import Confirm
except (ImportError, ModuleNotFoundError):  
    print("O módulo rich não está instalado, vamos instalar ele agora, aguarde...")
    system("pip install rich")
    print("O módulo rich foi instalado com sucesso, roda o código novamente para ele funcionar")
    quit()
console = Console()
""""
 precisa instalar o rich para o código funcionar, caso não tenha instalado, digite no terminal: 
 -------------------------------------------------------------------------------------------------
 pip install rich
 -------------------------------------------------------------------------------------------------
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

# Move o arquivo dados.py baixado para a pasta atual do projeto.
def TrocardoArquivoDados():
    try:
        system('move "%USERPROFILE%\Downloads\dados.py" .')
    except:
        system('mv ~/Downloads/dados.py .')

if len(dados.listadaTurma) > 0 :
    dados.mediadaTurmaDefinitiva=float(dados.mediadaTurmaDefinitiva)/len(dados.listadaTurma)
mediadaTurma=0

# Limpa a tela do terminal no Windows e, como alternativa, em outros sistemas.
def limpa():
    system("cls")

# Valida entradas numéricas e permite parar o fluxo com "parar" ou "break".
def Check(x,y):
    if x == 'int':
        try : return bool(int(y))
        except ValueError: return 'parar' if y.lower() == 'parar' or y.lower() == 'break' else False

# Inclui um novo aluno na lista e atualiza a média da turma.
def Inclusao():
    global mediadaTurma
    limpa()
    print("Aqui você vai digitar os dados do aluno que você deseja incluir")
    nome = input("\033[35mDigite o nome do Aluno: \033[0m") 
    nota1 = float(input("\033[35mDigite a nota que o Aluno tirou na primeira prova: \033[0m"))
    nota2 = float(input("\033[35mDigite a nota que o Aluno tirou na segunda prova: \033[0m"))
    media = (nota1+nota2)/2
    print(media)
    input("Pressione Enter para continuar...")
    situacao = "\033[34mAPROVADO\033[0m" if media>=6 else "\033[31mREPROVADO\033[0m"
    mediadaTurma+=media
    conteudo = {'nome':nome,'nota1':nota1,'nota2':nota2,'media':media,'situação':situacao}
    dados.listadaTurma.append(conteudo)
    input("Pressione Enter para continuar...")


# Consulta alunos por nome ou por situação.
def Consultar():
    global mediadaTurma
    limpa()
    print(
       panel := Panel(
                "𝟷 - 𝙿𝚎𝚕𝚘 𝚗𝚘𝚖𝚎 \n𝟸 - 𝙰𝚙𝚛𝚘𝚟𝚊𝚍𝚘 𝚘𝚞 𝚁𝚎𝚙𝚛𝚘𝚟𝚊𝚍𝚘",
                title="[bold red]𝙾𝚙çõ𝚎𝚜 𝚍𝚎 𝚌𝚘𝚗𝚜𝚞𝚕𝚝𝚊[/]",
                subtitle="[bold yellow]𝚅𝚘𝚌ê 𝚝𝚎𝚖 𝚍𝚞𝚊𝚜 𝚘𝚙çõ𝚎𝚜 𝚍𝚎 𝚌𝚘𝚗𝚜𝚞𝚕𝚝𝚊𝚛[/]"
          ) 
          )
    try:
        desicao = int(input("\033[94mDigite o número que representa a ação que você deseja realizar: \033[0m"))
    except ValueError:
        controleDeFluxo = False
        while controleDeFluxo == False:
            limpa()
            print(panel)
            print("Número inteiro, conjunto real, sabe irmão 1 2 3 4.... e não letras")
            desicao =input("\033[94mDigite o número que representa a ação que você deseja realizar: \033[0m")
            controleDeFluxo = Check(x="int",y=desicao)
            if controleDeFluxo == True:
                desicao = int(desicao)
            elif controleDeFluxo == 'parar':
                #um meio de parar o código, caso o usuário digite parar ou break.
                quit()


        
    listadeNome = []
    if desicao == 1:
        nome = input("Digite o nome do Aluno: ")
        for i in dados.listadaTurma:
            listadeNome.append(i['nome'])
        """
        Aqui em baixo vai verficar se o nome que o usuário digitou está na lista de nomes, se estiver, vai mostrar as informações do aluno, 
        se não estiver, vai mostrar uma mensagem dizendo que não tem um aluno com esse nome
        """
        if nome in listadeNome:
            tabela= Table()
            tabela.add_column("Nome", justify="center", style="green", no_wrap=True)
            tabela.add_column("Nota 1", justify="center", style="blue", no_wrap=True)
            tabela.add_column("Nota 2", justify="center", style="blue", no_wrap=True)
            tabela.add_column("Média", justify="center", style="magenta", no_wrap=True)
            tabela.add_column("Situação", justify="center", style="cyan", no_wrap=True)
            x=0
            for i in dados.listadaTurma:
                if nome.lower() in i['nome'].lower():
                    x+=1
                    nome_para_tabela = i['nome'].capitalize()
                    if i["situação"].lower() == "Aprovado".lower():
                        situacao_para_tabela = f"[green]{i['situação']}[/]"
                        if i['media'] >= 8:
                            media_para_tabela = f"[bold dark_blue]{i['media']}[/]"
                        else:
                            media_para_tabela = f"[blue]{i['media']}[/]"
                    elif i["situação"].lower() == "Reprovado".lower():
                        situacao_para_tabela = f"[red]{i['situação']}[/]"
                        if i['media'] <= 3:
                            media_para_tabela = f"[bold dark_red]{i['media']}[/]"
                        else:
                            media_para_tabela = f"[red]{i['media']}[/]"
                     
                    if i['nota1'] >= 8:
                        nota1_para_tabela = f"[bold dark_blue]{i['nota1']}[/]"
                    elif i['nota1'] >= 6:
                        nota1_para_tabela = f"[blue]{i['nota1']}[/]"
                        """
                    Não vai ter problema de colocar >=6 no elif, porque se for maior ou igual a 8, ele vai entrar no if,
                    e se for menor que 8, ele vai entrar no elif, então não vai ter problema de colocar >=6 no elif.
                    exemplo se for 9, mesmo que seja maior que 6, ele vai entrar no if, e não vai entrar no elif,
                    o elif só vai ser executado se o if ou elif anterior for falso
                        """
                    elif i['nota1'] <= 3:
                        nota1_para_tabela = f"[bold dark_red]{i['nota1']}[/]"
                    elif i['nota1'] <= 5:
                        nota1_para_tabela = f"[red]{i['nota1']}[/]"
                    
                    #Aqui vai fazer a mesma coisa que fez com a nota1, mas com a nota2
                    if i['nota2'] >= 8:
                        nota2_para_tabela = f"[bold dark_blue]{i['nota2']}[/]"
                    elif i['nota2'] >= 6:
                        nota2_para_tabela = f"[blue]{i['nota2']}[/]"
                        """
                    Não vai ter problema de colocar >=6 no elif, porque se for maior ou igual a 8, ele vai entrar no if,
                    e se for menor que 8, ele vai entrar no elif, então não vai ter problema de colocar >=6 no elif.
                    exemplo se for 9, mesmo que seja maior que 6, ele vai entrar no if, e não vai entrar no elif,
                    o elif só vai ser executado se o if ou elif anterior for falso
                        """
                    elif i['nota2'] <= 3:
                        nota2_para_tabela = f"[bold dark_red]{i['nota2']}[/]"
                    elif i['nota2'] <= 5:
                        nota2_para_tabela = f"[red]{i['nota2']}[/]"
                    
                    #Aqui vai adicionar uma linha na tabela com as informações do aluno
                    #tabela(nome, nota 1, nota 2, média, situação)
                    tabela.add_row(nome_para_tabela, nota1_para_tabela, nota2_para_tabela, media_para_tabela, situacao_para_tabela)
                    
            #Aqui eu crio um painel, pra mostrar os dados achados.
            texto = Panel(
                        tabela,
                        title=f"[bold yellow]Lista de Alunos com {nome} no seu nome[/]",
                        subtitle=f"[bold yellow]A média da turma foi de {mediadaTurma:.1f} e tem {x} alunos com {nome} no seu nome[/]"
                    )
                    
            #Aqui eu mostro o painel com as informações do aluno
            print(texto)
    
                    
        else:
            print(f"Não tem um aluno com {nome} no seu nome")

    elif desicao == 2:
        x=1
        situacao = input("\033[94mDesejar ver os Aprovado ou Reprovado: \033[0m").lower()
        if situacao in ("aprovado","reprovado"):
            """
            for i in dados.listadaTurma:
                if i['situação'].lower() in ("aprovado","reprovado"):
                    i['situação'] = "[i blue]APROVADO[/]" if i['situação'].lower()=="aprovado" else "[i red]REPROVADO[/]"
            """
            tabela = Table()
            tabela.add_column("Número", justify="center", style="cyan", no_wrap=True)
            tabela.add_column("Nome", justify="center", style="green", no_wrap=True)
            for i in dados.listadaTurma:
                if situacao.upper() == i['situação'].upper():
                    tabela.add_row(str(x), i['nome'].capitalize())
                    x+=1
            situacao = "[i blue]APROVADO[/]" if situacao=="aprovado" else "[i red]REPROVADO[/]"
            texto = Panel(
                tabela,
                title=f"[bold yellow]Lista de Alunos {situacao}[/]",
                #x-1 porque o contador começa em 1 e não em 0, então sempre vai contar um a mais do que realmente tem
                subtitle=f"[bold yellow]A média da turma foi de {mediadaTurma:.1f} e tem {x-1} alunos que foi {situacao}[/]"
            )
            print(texto)
        
    else:
        print("\007Opção não válida")
    input("Pressione Enter para continuar...")


# Gera relatório em texto ou atualiza o arquivo dados.py com o estado atual.
def Relatorio(x):
    global mediadaTurma
    user = getlogin()
    data = f"{datetime.now().strftime('%d/%m/%Y')}"
    if x == "txt":
        with open("Relatório.txt", "w+", encoding="utf-8") as blueLock:
            contador=1
            tabela = Table(title="Alunos da turma")
            tabela.add_column("Número", justify="center", style="cyan", no_wrap=True)
            tabela.add_column("Nome", justify="center", style="green", no_wrap=True)
            tabela.add_column("AV", justify="center", style="blue", no_wrap=True)
            tabela.add_column("AVS", justify="center", style="blue", no_wrap=True)
            tabela.add_column("Média", justify="center", style="magenta", no_wrap=True)
            tabela.add_column("Situação", justify="center", style="cyan", no_wrap=True)
            for i in dados.listadaTurma:
                tabela.add_row(str(contador), i['nome'].capitalize(), str(i['nota1']), str(i['nota2']), str(i['media']), i['situação'].capitalize())
                contador+=1
            texto= f"A média da turma no geral foi de {mediadaTurma:.1f} , turma {'[i blue]APROVADO[/]' if mediadaTurma>=6 else '[i red]REPROVADO[/]'}"
            texto = Panel(
                tabela,
                title=f"[bold yellow]Relatório da turma feito no dia {data} , pelo {user}[/]",
                subtitle=f"[bold yellow]{texto}[/]"
            )
            global console
            console_export = Console(record=True)
            console_export.print(texto)
            limpa()
            texto = console_export.export_text()
            blueLock.write(texto)
    if x == "python":
        with open("dados.py", "w+" , encoding="utf-8") as Kaiser:
            contador = 1
            texto = ""
            for i in dados.listadaTurma:
                if contador == 1 :
                    texto = f"\n {{'nome': '{i['nome'].capitalize()}', 'nota1': {i['nota1']}, 'nota2': {i['nota2']}, 'media': {i['media']}, 'situação': '{i['situação'].capitalize()}'}} #Está na possição {contador-1}\n,"
                else:
                    texto += f" {{'nome': '{i['nome'].capitalize()}', 'nota1': {i['nota1']}, 'nota2': {i['nota2']}, 'media': {i['media']}, 'situação': '{i['situação'].capitalize()}'}} #Está na possição {contador-1}\n,"
                contador+=1
            # O segredo está nas aspas simples em '%H:%M:%S'
            texto = texto[:-1]  # Remove a última vírgula
            mediadaTurma = 0
            divisor = 0
            for i in dados.listadaTurma:
                mediadaTurma+=float(i['media'])
                divisor+=1
            #mediadaTurma = mediadaTurma/divisor if divisor > 0 else 0.0
            Kaiser.write(f"# Foi modificado no dia {data} às {datetime.now().strftime('%H:%M:%S')} pelo {user}\nlistadaTurma = [{texto}\n]\nmediadaTurmaDefinitiva= {mediadaTurma:.1f}")



# Atualiza o nome, a nota 1 ou a nota 2 de um aluno já cadastrado.
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


# Remove um aluno específico ou apaga toda a lista, dependendo do modo recebido.
def Apagar(x):
    global mediadaTurma
    limpa()
    if x == 0:
        print("Aqui você vai apagar um aluno")
        contador = 0
        tabela = Table(title="Lista de Alunos")
        tabela.add_column("Número", justify="center", style="cyan", no_wrap=True)
        tabela.add_column("Nome", justify="center", style="green", no_wrap=True)
        for i in dados.listadaTurma:
            tabela.add_row(str(contador), i['nome'].capitalize())
            contador+=1
        print(tabela)
        desicao=int(console.input(":broom::x: Digite o número que representa o nome do aluno que você deseja apagar: "))
        index = desicao
        dadosTemp = dados.listadaTurma[index]
        dados.listadaTurma.pop(index)
        print(f"O Aluno {dadosTemp['nome']} foi apagado :negative_squared_cross_mark:")
        mediaApagada = dadosTemp['media']
        mediadaTurma-= mediaApagada
    if x == 1:
        resposta = Confirm.ask("Você deseja continuar com a instalação?")
        if resposta:
            dados.listadaTurma.clear()
            mediadaTurma = 0
        else:
            print("[bold black]onde você comprou o teclado não vendia coragem também?[/]\n \n[italic orange3]O lugar mais seguro da cidade é na frente da[/] [i pink1]sua mira. 🎯🔫[/]")

    input("Pressione Enter para continuar...")


# Abre o site do projeto no navegador padrão.
def MostraSite():
    try:
        system("start https://shre.ink/projetodepython")
    except:
        system("xdg-open https://shre.ink/projetodepython")


# Exibe todos os alunos em uma tabela resumida.
def listar():
    limpa()
    tabela = Table(title="Lista de Alunos")
    tabela.add_column("Número", justify="center", style="cyan", no_wrap=True)
    tabela.add_column("Nome", justify="center", style="green", no_wrap=True)
    tabela.add_column("Média", justify="center", style="magenta", no_wrap=True)
    tabela.add_column("Situação", justify="center", style="blue", no_wrap=True)
    contador = 1
    for i in dados.listadaTurma:
        if i["situação"] == "Aprovado":
            x = f"[green]{i['situação']}[/]"
            if i['media'] >= 9:
                z = f"[bold dark_blue]{i['media']}[/]"
            else:
                z = f"[blue]{i['media']}[/]"
        elif i["situação"] == "Reprovado":
            x = f"[red]{i['situação']}[/]"
            if i['media'] <= 3:
                z = f"[bold dark_red]{i['media']}[/]"
            else:
                z = f"[red]{i['media']}[/]"
        tabela.add_row(str(contador), i['nome'].capitalize(), z, x)
        contador+=1
    print(tabela)
    input("Pressione Enter para continuar...")


# Menu principal: mantém a aplicação em loop e chama a ação escolhida.
def Menu():
    global mediadaTurma
    """
    Aqui a mediaadaTurma vai receber o valor da mediadaTurmaDefinitiva, que já está dividido pelo tamanho da lista, 
    então não precisa dividir de novo, porque se não vai dar um valor errado
    """
    mediadaTurma = dados.mediadaTurmaDefinitiva
    menu = Panel(
            """
            ========================================== 
            1)[bold purple]𝓘𝓷𝓬𝓵𝓾𝓼𝓪̃𝓸[/]
            2)[bold magenta]𝓒𝓸𝓷𝓼𝓾𝓵𝓽𝓪𝓻[/]
            3)[bold cyan]Listar[/]
            4)[bold yellow]𝓐𝓽𝓾𝓪𝓵𝓲𝔃𝓪𝓻 𝓭𝓪𝓭𝓸𝓼[/]
            5)[bold red]𝓔𝔁𝓬𝓵𝓾𝓲𝓻 𝓪𝓵𝓾𝓷𝓸𝓼[/]
            6)[bold blue]𝓔𝔁𝓬𝓵𝓾𝓲𝓻 𝓽𝓾𝓭𝓸[/]
            7)[bold green]𝓢𝓪𝓲𝓻 e ver o site[/]
            8)[bold white]Atualizar o arquivo de dados[/]
            9)[bold red]𝓢𝓪𝓲𝓻 e salvar[/]
            10)[bold yellow]Gerar relatório em txt e sair[/]
            ========================================== 
            """,
            title="[bold red]𝓜𝓮𝓷𝓾 𝓟𝓻𝓲𝓷𝓬𝓲𝓹𝓪𝓵[/bold red]",
            subtitle="[bold yellow]Escolha uma das opções acima[/bold yellow]"
        )
    while True:
        limpa()
        print(menu)
        try:
                desicao = int(input("\033[94mDigite o número que representa a ação que você deseja realizar: \033[0m"))
        except ValueError:
                controleDeFluxo = False
                controleDeReacao = 1
                while controleDeFluxo == False:
                    limpa()
                    print(menu)
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
            listar()
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
        elif desicao == 10:
            Relatorio(x="txt")
            return "sair"
            break
        """
        elif desicao == 11:
            return "sair"
            break
        parada secreta, para eu usando enquato estou testando o código, 
        para não ter que ficar digitando 9 para sair e salvar, eu só digito 11 e ele sai e não salva
        """

   
