import dados, beta2,bancodedados
from tkinter import messagebox
from os import system , getlogin
from datetime import datetime
#{'nome': nome, 'notafinal': maiorNota, 'situacao': situacao}
ZeroTwo = "Não né filhão"
def MostrarAlunos():
    texto=""
    x=1
    for  i in beta2.ListarcomNome:
        texto += f"{x} - O Aluno {i['nome']} | Maior Nota: {i['notafinal']:.1f} | {i['situacao']}\n"
        x+=1
    return texto

def AdicionarNaLista(nome, av, avs,janela="n/a"):
    global ZeroTwo
    try: 
        texto = ""
        av = float(str(av).replace(',', '.'))
        avs = float(str(avs).replace(',', '.'))
        if av<=10 and av>=0 and avs>=0 and avs<=10:
            maiorNota = max(av, avs)
            situacao = "Aprovado" if maiorNota >= 6 else "Reprovado"
        elif av>avs and av<=10 and av>=0:
            maiorNota = av
            situacao = "Aprovado" if maiorNota >= 6 else "Reprovado"
        elif avs>av and avs<=10 and avs>=0:
            maiorNota = avs
            situacao = "Aprovado" if maiorNota >= 6 else "Reprovado"
        else:
            texto = ZeroTwo
            int(texto)
        
        beta2.ListarcomNome.append({'nome': nome, 'notafinal': maiorNota, 'situacao': situacao})
        #print(beta2.ListarcomNome)
        BancodeDados(nome=nome,notafinal=maiorNota,situacao=situacao,acao="Criar")
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")

        janela.destroy()
    except ValueError:
        if texto == ZeroTwo:
            messagebox.showinfo("Sério","Digite um valor para av ou para avs que seja" 
                                "\nMenor ou igual a 10  \nOu \nMaior ou igual 0\n" \
            "Pelo menos em um deles")
        else:
            messagebox.showerror("Erro", "Use números válidos (ex: 7.5)")

#uma mostrar padrão
def ListarNomes():
    return "\n".join([f"{x+1} - {i['nome']}" for x, i in enumerate(beta2.ListarcomNome)])

def ApagarNaLista(id,janela="n/a"):
   
    try:
        idx = int(id) - 1
        nome = beta2.ListarcomNome[idx]['nome']
        if 0 <= idx < len(beta2.ListarcomNome):
            beta2.ListarcomNome.pop(idx) 
            messagebox.showinfo("Sucesso", "Apagado com sucesso!")
            BancodeDados(acao="Apagar",nome=nome)
            janela.destroy()
        else:
            messagebox.showwarning("Aviso", "ID não encontrado")
    except ValueError:
        messagebox.showerror("Erro", "Use um número inteiro")

def AbrirNavegador(url="www.gooogle.com"):
    system(f"start {url}")

def ConsultarNaLista(nome="n/a",janela="n/a"):
    achados = []
    for i in beta2.ListarcomNome:
        if nome.upper() == i['nome'].upper():
            #Vai aprender uma lista
            achados.append([i['nome'],i['situacao']])
    x=1
    texto=''
    for i in achados:
        texto+=f"{x} ---- {i[0]}  ---- {i[1]}\n"
        x+=1
    if len(achados)>0:
        messagebox.showinfo("Resultados da Consulta",texto)
        janela.destroy()
    else:
        messagebox.showerror("Não tem", "Não foi achado ninguém")

def MudarNaLista(posicao=0,av=0.1,avs=0.1,nome="Fulano",janela="n/a"):
    #1 nome  3 notafinal&situal 4 full valor novo vem em lista e campo também
    global ZeroTwo
    try:
        posicao=int(posicao)
        if posicao <= len(beta2.ListarcomNome):
                posicao=posicao-1
                maiorNota = float(beta2.ListarcomNome[posicao]['notafinal'])
                Mudanca=[1,2,3]
                notas=0
                #Variável para verficar se tanto a av e avs são maior que 10
                verficar=0
                texto = ""
                MudouNota=False
                MudouNome=False
                NomeAntigo = beta2.ListarcomNome[posicao]['nome']
                if av != "":
                    av=float(f"{float(av.replace(',', '.')):.1f}")
                    if av<=10:
                        notas+=1
                        if av > maiorNota:
                            beta2.ListarcomNome[posicao]['notafinal'] = av
                            beta2.ListarcomNome[posicao]['situacao'] = "Aprovado" if av>=6 else "Reprovado"
                            Mudanca[1]=beta2.ListarcomNome[posicao]['notafinal']
                            Mudanca[2]=beta2.ListarcomNome[posicao]['situacao']
                            MudouNota=True
                    else:
                        verficar+=1
                if avs !="":
                    avs=float(f"{float(avs.replace(',', '.')):.1f}")
                    if avs<=10:
                        notas+=1
                        if avs > maiorNota:
                            beta2.ListarcomNome[posicao]['notafinal'] = avs
                            beta2.ListarcomNome[posicao]['situacao'] = "Aprovado" if avs>=6 else "Reprovado"
                            Mudanca[1]=beta2.ListarcomNome[posicao]['notafinal']
                            Mudanca[2]=beta2.ListarcomNome[posicao]['situacao']
                            MudouNota=True
                        #Força atualazição após colocar no campo da av e da avs
                        if notas >=2:
                            if av >= avs:
                                beta2.ListarcomNome[posicao]['notafinal'] = av
                                beta2.ListarcomNome[posicao]['situacao'] = "Aprovado" if av>=6 else "Reprovado"
                                Mudanca[1]=beta2.ListarcomNome[posicao]['notafinal']
                                Mudanca[2]=beta2.ListarcomNome[posicao]['situacao']
                                MudouNota=True
                            else:
                                beta2.ListarcomNome[posicao]['notafinal'] = avs
                                beta2.ListarcomNome[posicao]['situacao'] = "Aprovado" if avs>=6 else "Reprovado"
                                Mudanca[1]=beta2.ListarcomNome[posicao]['notafinal']
                                Mudanca[2]=beta2.ListarcomNome[posicao]['situacao']
                                MudouNota=True
                    else:
                        verficar+=1
                        if verficar == 2:
                            texto = ZeroTwo
                            int(texto)
                            

                if nome !="":
                    beta2.ListarcomNome[posicao]['nome'] = nome
                    Mudanca[0]=beta2.ListarcomNome[posicao]['nome']
                    MudouNome=True
                if MudouNome and MudouNota:
                    contador = 4
                    campos=['nome','notafinal','situacao']
                elif MudouNome:
                    contador = 1
                    campos=['nome']
                elif MudouNota:
                    contador = 3
                    campos=['notafinal','situacao']
                messagebox.showinfo("Sucesso", "Alterado com sucesso!")
                BancodeDados(acao="Alterar",nome=NomeAntigo,campo=[contador,Mudanca,campos])
        else:
           controle= messagebox.askyesno("ID errado", "Você digitou uma posição que não existe ainda,deseja criar ?")
           if controle:
               nome="Fulando" if nome=="" else nome
               av=0.1 if av=="" else av
               avs=0.1 if avs=="" else avs
               AdicionarNaLista(nome=nome,av=av,janela=janela,avs=avs)

    except ValueError:
        if texto == ZeroTwo:
            messagebox.showinfo("Confia","Claro que você tirou mais que 10 na Av e Avs, menos de zero em ambos eu aceito")
        else:
         messagebox.showerror("Campo de Número se usa número", "Sabe o que são Números?")
    janela.destroy()

def GerarRelatorio(tipo=".html"):
    user = getlogin()
    data = f"{datetime.now().strftime('%d/%m/%Y')}"
    if tipo == ".txt":
         with open("Relatório.txt", "w+", encoding="utf-8") as blueLock:
            contador=1
            texto=f"Relatório da turma feito no dia {data} , pelo {user}\n"
            mediadaTurma=0
            for i in beta2.ListarcomNome:
                mediadaTurma+=i['notafinal']
                texto+= f"{contador} - Nome: {i['nome']} - Sua maior nota: {i['notafinal']:.1f} - {i['situacao']}\n"
                contador+=1
            texto+= f"A média da turma no geral foi de {mediadaTurma/len(beta2.ListarcomNome):.1f} , turma {'APROVADO' if mediadaTurma/len(beta2.ListarcomNome)>=6 else 'REPROVADO'}\n"
            blueLock.write(texto)
    elif tipo == ".py":
        with open("dados.py", "w+" , encoding="utf-8") as Kaiser:
            contador = 1
            texto = ""
            mediadaTurma=0
            for i in beta2.ListarcomNome:
                mediadaTurma+=i['notafinal']
                if contador == 1 :
                    texto = f"{{'nome': '{i['nome']}', 'notafinal': {i['notafinal']}, 'situacao': '{i['situacao']}'}}\n"
                else:
                    texto += f", {{'nome': '{i['nome']}', 'notafinal': {i['notafinal']}, 'situacao': '{i['situacao']}'}}\n"
                contador+=1
            # O segredo está nas aspas simples em '%H:%M:%S'
            Kaiser.write(f"# Foi modificado no dia {data} às {datetime.now().strftime('%H:%M:%S')} pelo {user}\n"
                 f"ListarcomNome = [{texto}]\n"
                 f"mediadaTurmaDefinitiva = {mediadaTurma:.1f}")
def BancodeDados(acao='nenhuma',nome="fulano",notafinal=float(1),situacao="Seila",campo="n/a"):
            if acao == "Criar":
                bancodedados.Criar(nome=nome,notafinal=notafinal,situacao=situacao)
            if acao == "Apagar":
                bancodedados.Apagar(nome=nome)
            if acao == "Alterar":
                bancodedados.Alterar(nome=nome,campo=campo)

            
