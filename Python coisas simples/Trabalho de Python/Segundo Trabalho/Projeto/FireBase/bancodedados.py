import dados,funções,requests,json
from tkinter import messagebox
#apenas essa quatras "bibliotecas" , apenas o resquests e o json é de fato uma biblioteca
#demais são arquivos
#Aqui vai pegar o link do banco de dados do firebase
"""
    200 (OK): Tudo deu certo.
    201 (Created): Sucesso e algo foi criado (comum em POST).
    204 (No Content): Deu certo, mas o servidor não devolveu nenhum conteúdo (comum em DELETE).
    301 (Moved Permanently): A URL mudou permanentemente.
    302 (Found/Found): A URL mudou temporariamente.
"""
url = "https://makima-deusa-default-rtdb.firebaseio.com/"

#Criando um aluno no banco de dados
# as chaves usadas {'nome' , 'notafinal' e 'situacao'} 'notafinal' está no tipo number
#é dumps e não dump
"""
exemplo = {'nome':"Naruto",'notafinal':9.9 , 'situacao':"Aprovado"}
requisicao = requests.post(f"{url}Alunos/.json" , data=json.dumps(exemplo))
print(requisicao)
print(requisicao.text)

"""
"""
#pegando e editando
exemplo = {'nome':"Gohan"}
requisicao = requests.get(f'{url}/.json')
#torna em dics tipo py
dic_requisicao = requisicao.json()
#pega apenas a parte que está em Alunos
dic_requisicao =dic_requisicao['Alunos']
#rodar por cada id que o aluno tem
for i in dic_requisicao:
    #pegar o dics / dados do aluno x
    aluno = dic_requisicao[f'{i}']
    print(aluno['nome'])
    #mudar o nome do aluno x
    if aluno['nome'] == "Goku":
        requests.patch(f'{url}Alunos/{i}/.json', data=json.dumps(exemplo))
"""
"""
requisicao = requests.get(f'{url}/.json')
#torna em dics tipo py
dic_requisicao = requisicao.json()
#pega apenas a parte que está em Alunos
dic_requisicao =dic_requisicao['Alunos']
for i in dic_requisicao:
    nome = dic_requisicao[f'{i}']
    if nome['nome'] == "Naruto":
        requests.delete(f'{url}Alunos/{i}/.json')
"""

def Criar(nome="fulano",notafinal=float(1),situacao="situacao"):
    AlunoNovo = {'nome': nome, 'notafinal' : notafinal , 'situacao': situacao}
    PedidoDeCriacao = requests.post(f'{url}Alunos/.json' , data=json.dumps(AlunoNovo))
    Confirmacao = PedidoDeCriacao.status_code
    try:
        Confirmacao = int(Confirmacao)
        if Confirmacao == 200:
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso, banco de dados!")
    except:
        messagebox.showwarning("Aviso","Verficar o banco de dados")
def Apagar(nome="nome"):
    Pedido = requests.get(f'{url}/.json')
    Pedido = Pedido.json()
    PedidoDeApagar = Pedido['Alunos']
    for i in PedidoDeApagar:
        QuemApagar = PedidoDeApagar[f'{i}']
        if QuemApagar['nome'].upper() == nome.upper():
            Deletar = requests.delete(f'{url}Alunos/{i}/.json')
            Confirmacao = Deletar.status_code
            try:
                Confirmacao = int(Confirmacao)
                if Confirmacao == 200:
                    messagebox.showinfo("Sucesso", "Aluno Apagado com sucesso, banco de dados!")
            except:
                messagebox.showwarning("Aviso","Verficar o banco de dados")
            break
            
#1 nome  3 notafinal&situal 4 full valor novo vem em lista e campo também
def Alterar(nome="nome",campo=[1,"Valor Novo","campo"]):
    Pedido = requests.get(f'{url}/.json')
    Pedido = Pedido.json()
    PedidoDeAlterar = Pedido['Alunos']
    status=0
    for i in PedidoDeAlterar:
        QuemMudar = PedidoDeAlterar[f'{i}']
        if QuemMudar['nome'].strip().upper() == nome.strip().upper():
            if campo[0] == 1:
                Mudar = {campo[2][0]: campo[1][0]}
                fazer = requests.patch(f'{url}Alunos/{i}/.json', data=json.dumps(Mudar))
                status = fazer.status_code 
                break
            elif campo[0] == 3:
                y =1
                for x in campo[2]:
                    Mudar = {x: campo[1][y] }
                    fazer = requests.patch(f'{url}Alunos/{i}/.json', data=json.dumps(Mudar))
                    status = fazer.status_code 
                    y+=1
                break
            elif campo[0]==4:
                y=0
                for x in campo[2]:
                    Mudar = {x : campo[1][y] }
                    fazer = requests.patch(f'{url}Alunos/{i}/.json', data=json.dumps(Mudar))
                    status = fazer.status_code 
                    y+=1
                break

    status = int(status)
    if status == 200:
             messagebox.showinfo("Sucesso", "Aluno teve os dados alterado com sucesso, banco de dados!")
    else:
             messagebox.showwarning("Aviso","Verficar o banco de dados")

def LigacaoComDadosSalvos():
    ListaComDadosDoBancoDeDadosFireBase = []
    #Pegar os dados mas no tipo .json
    pedido = requests.get(f'{url}/.json')
    #Tentar transforma no tipo python
    pedido = pedido.json()
    #Tentar pegar apenas o campos do Alunos
    pedido = pedido['Alunos']
    for i in pedido:
        Chaves = pedido[f'{i}']
        Salva = {'nome': Chaves['nome'] , 'notafinal': Chaves['notafinal'], 'situacao': Chaves['situacao']}
        ListaComDadosDoBancoDeDadosFireBase.append(Salva)
    return ListaComDadosDoBancoDeDadosFireBase
def teste():
    Dados = LigacaoComDadosSalvos()
    return Dados



            


