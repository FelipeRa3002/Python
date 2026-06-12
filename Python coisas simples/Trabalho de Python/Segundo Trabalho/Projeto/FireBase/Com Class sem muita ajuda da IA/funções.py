import requests,json
from tkinter import messagebox
from os import system , getlogin
from datetime import datetime
#{'nome': nome, 'notafinal': maiorNota, 'situacao': situacao}
class BancodeDados:
    ZeroTwo = "Não né filhão"
    listacomnome = []
    url = "https://makima-deusa-default-rtdb.firebaseio.com/"
    def __init__(self,urlcompleta:str):
        global url , listacomnome
        url = "https://makima-deusa-default-rtdb.firebaseio.com/"
        self.url = f'{url}{urlcompleta}/'
        listacomnome = []
        url_final = f'{self.url}/.json'
        pedido = requests.get(url_final)
        pedido = pedido.json()
        for i in pedido:
            valores = pedido[f'{i}']
            Salva = {'nome': valores['nome'] , 'notafinal': valores['notafinal'], 'situacao': valores['situacao']}
            listacomnome.append(Salva)
        pass
    def Adicionar(self,nome, av, avs,janela="n/a",nomedaturma=""):
        from alunos import Aluno
        global ZeroTwo , listacomnome
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
            alunoNovo = Aluno(nomedaturma=nomedaturma,nome=nome,nota=maiorNota,situacao=situacao)
            requisicao = requests.post(f"{self.url}Alunos/.json" , data=json.dumps(alunoNovo.__dict__))
            try: 
                Confirmacao = requisicao.status_code
                Confirmacao = int(Confirmacao)
                if Confirmacao == 200:
                    messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
                else: 
                    messagebox.showerror("Erro", "Falha ao salvar")
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao salvar: {e}")
            janela.destroy()
        except ValueError:
            if texto == ZeroTwo:
                messagebox.showinfo("Sério","Digite um valor para av ou para avs que seja" 
                                    "\nMenor ou igual a 10  \nOu \nMaior ou igual 0\n" \
                "Pelo menos em um deles")
            else:
                messagebox.showerror("Erro", "Use números válidos (ex: 7.5)")

    #uma mostrar padrão
    def ListarNomes(self):
        global listacomnome
        listacomnome = []
        url = self.url
        pedido = requests.get(f'{url}/.json')
        pedido = pedido.json()
        for i in pedido:
            valores = pedido[f'{i}']
            Salva = {'nome': valores['nome'] , 'notafinal': valores['notafinal'], 'situacao': valores['situacao']}
            listacomnome.append(Salva)
        return "\n".join([f"{x+1} - {i['nome']} --- Nota Final {float(i['notafinal']):.1f} ---- {i['situacao']}" for x, i in enumerate(listacomnome)])

    def ApagarNaLista(self,id,janela="n/a"):
        
        try:
            global listacomnome
            idx = int(id) - 1
            nome = listacomnome[idx]['nome']
            if 0 <= idx < len(listacomnome):
                listacomnome.pop(idx) 
                messagebox.showinfo("Sucesso", "Apagado com sucesso!")
                pedido = requests.get(f'{self.url}Alunos/.json')
                pedido = pedido.json()
                for i in pedido:
                    QuemApagar = pedido[f'{i}']
                    if QuemApagar['nome'].upper() == nome.upper():
                        Deletar = requests.delete(f'{self.url}Alunos/{i}/.json')
                        Confirmacao = Deletar.status_code
                        try:
                            Confirmacao = int(Confirmacao)
                            if Confirmacao == 200:
                                messagebox.showinfo("Sucesso", "Aluno Apagado com sucesso, banco de dados!")
                        except:
                            messagebox.showwarning("Aviso","Verficar o banco de dados")
                        break
                janela.destroy()
            else:
                messagebox.showwarning("Aviso", "ID não encontrado")
        except ValueError:
            messagebox.showerror("Erro", "Use um número inteiro")

    def AbrirNavegador(self,url="www.gooogle.com"):
        system(f"start {url}")

    def ConsultarNaLista(self,nome="n/a",janela="n/a"):
        global listacomnome
        listacomnome = []
        pedido = requests.get(f'{self.url}Alunos/.json')
        pedido = pedido.json()
        for i in pedido:
            valores = pedido[f'{i}']
            Salva = {'nome': valores['nome'] , 'notafinal': valores['notafinal'], 'situacao': valores['situacao']}
            listacomnome.append(Salva)
        achados = []
        for i in listacomnome:
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

    def MudarNaLista(self,posicao=0,av=0.1,avs=0.1,nome="Fulano",janela="n/a"):
        #1 nome  3 notafinal&situal 4 full valor novo vem em lista e campo também
        global ZeroTwo , listacomnome
        try:
            posicao=int(posicao)
            if posicao <= len(listacomnome):
                    posicao=posicao-1
                    maiorNota = float(listacomnome[posicao]['notafinal'])
                    Mudanca=[1,2,3]
                    notas=0
                    #Variável para verficar se tanto a av e avs são maior que 10
                    verficar=0
                    texto = ""
                    MudouNota=False
                    MudouNome=False
                    NomeAntigo = listacomnome[posicao]['nome']
                    if av != "":
                        av=float(f"{float(av.replace(',', '.')):.1f}")
                        if av<=10:
                            notas+=1
                            if av > maiorNota:
                                listacomnome[posicao]['notafinal'] = av
                                listacomnome[posicao]['situacao'] = "Aprovado" if av>=6 else "Reprovado"
                                Mudanca[1]=listacomnome[posicao]['notafinal']
                                Mudanca[2]=listacomnome[posicao]['situacao']
                                MudouNota=True
                        else:
                            verficar+=1
                    if avs !="":
                        avs=float(f"{float(avs.replace(',', '.')):.1f}")
                        if avs<=10:
                            notas+=1
                            if avs > maiorNota:
                                listacomnome[posicao]['notafinal'] = avs
                                listacomnome[posicao]['situacao'] = "Aprovado" if avs>=6 else "Reprovado"
                                Mudanca[1]=listacomnome[posicao]['notafinal']
                                Mudanca[2]=listacomnome[posicao]['situacao']
                                MudouNota=True
                            #Força atualazição após colocar no campo da av e da avs
                            if notas >=2:
                                if av >= avs:
                                    listacomnome[posicao]['notafinal'] = av
                                    listacomnome[posicao]['situacao'] = "Aprovado" if av>=6 else "Reprovado"
                                    Mudanca[1]=listacomnome[posicao]['notafinal']
                                    Mudanca[2]=listacomnome[posicao]['situacao']
                                    MudouNota=True
                                else:
                                    listacomnome[posicao]['notafinal'] = avs
                                    listacomnome[posicao]['situacao'] = "Aprovado" if avs>=6 else "Reprovado"
                                    Mudanca[1]=listacomnome[posicao]['notafinal']
                                    Mudanca[2]=listacomnome[posicao]['situacao']
                                    MudouNota=True
                        else:
                            verficar+=1
                            if verficar == 2:
                                texto = ZeroTwo
                                int(texto)
                                

                    if nome !="":
                        listacomnome[posicao]['nome'] = nome
                        Mudanca[0]=listacomnome[posicao]['nome']
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
                    #Alterar no banco de dados
                    url_final = f'{self.url}Alunos/.json'
                    Pedido = requests.get(url_final)
                    Pedido = Pedido.json()  
                    status=0
                    for i in Pedido:
                       QuemMudar = Pedido[f'{i}']
                       if QuemMudar['nome'].strip().upper() == nome.strip().upper():
                           if contador == 4:
                                y=0
                                for x in campos:
                                    Mudar = {f'{x}' : Mudanca[y] }
                                    fazer = requests.patch(f'{url}Alunos/{i}/.json', data=json.dumps(Mudar))
                                    status = fazer.status_code 
                                    y+=1
                                break
                           elif contador == 3:
                               y =1
                               for x in campos:
                                    Mudar = {f'{x}': Mudanca[y] }
                                    fazer = requests.patch(f'{url}Alunos/{i}/.json', data=json.dumps(Mudar))
                                    status = fazer.status_code 
                                    y+=1
                               break
                           elif contador == 1:
                                   Mudar = {f'{campos[0]}': Mudanca[0]}
                                   fazer = requests.patch(f'{url}Alunos/{i}/.json', data=json.dumps(Mudar))
                                   status = fazer.status_code 
                                   break
                
            try: 
                   
                    status = int(status)
                    if status == 200:
                                    messagebox.showinfo("Sucesso", "Aluno teve os dados alterado com sucesso, banco de dados!")
            except:
                                    messagebox.showwarning("Aviso","Verficar o banco de dados")
                    
                    
              
                    #BancodeDados(acao="Alterar",nome=NomeAntigo,campo=[contador,Mudanca,campos])
            """
            else:
             controle= messagebox.askyesno("ID errado", "Você digitou uma posição que não existe ainda,deseja criar ?")
            if controle:
                nome="Fulando" if nome=="" else nome
                av=0.1 if av=="" else av
                avs=0.1 if avs=="" else avs
                AdicionarNaLista(nome=nome,av=av,janela=janela,avs=avs)
            """
        except ValueError:
            if texto == ZeroTwo:
                messagebox.showinfo("Confia","Claro que você tirou mais que 10 na Av e Avs, menos de zero em ambos eu aceito")
            else:
             messagebox.showerror("Campo de Número se usa número", "Sabe o que são Números?")
        janela.destroy()

    def GerarRelatorio(self,tipo=".html"):
        user = getlogin()
        data = f"{datetime.now().strftime('%d/%m/%Y')}"
        listacomnome = []
        pedido = requests.get(f'{self.url}Alunos/.json')
        pedido = pedido.json()
        for i in pedido:
            valores = pedido[f'{i}']
            Salva = {'nome': valores['nome'] , 'notafinal': valores['notafinal'], 'situacao': valores['situacao']}
            listacomnome.append(Salva)
        if tipo == ".txt":
            with open("Relatório.txt", "w+", encoding="utf-8") as blueLock:
                contador=1
                texto=f"Relatório da turma feito no dia {data} , pelo {user}\n"
                mediadaTurma=0
                for i in listacomnome:
                    mediadaTurma+=i['notafinal']
                    texto+= f"{contador} - Nome: {i['nome']} - Sua maior nota: {i['notafinal']:.1f} - {i['situação']}\n"
                    contador+=1
                texto+= f"A média da turma no geral foi de {mediadaTurma/len(listacomnome):.1f} , turma {'APROVADO' if mediadaTurma/len(listacomnome)>=6 else 'REPROVADO'}\n"
                blueLock.write(texto)
        elif tipo == ".py":
            with open("dados.py", "w+" , encoding="utf-8") as Kaiser:
                contador = 1
                texto = ""
                mediadaTurma=0
                for i in listacomnome:
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
