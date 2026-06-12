from tkinter import messagebox
from tkinter import *
import funcoes, banco
"""
cores: #210C21 ; #212121 ; #0A211E ; #21180A
"""
def Inicio():
    # Inicializa a conexão com o banco de dados e cria as tabelas se não existirem
    banco.comecar()
    janela = Tk()
    janela.geometry("1200x780")
    janela.title("Gerenciamento de Alunos")
    janela.config(bg="#0A211E")
    # Configura o redimensionamento proporcional das colunas e linhas do grid
    janela.grid_columnconfigure((0, 1, 2, 3,4,5), weight=1)
    janela.grid_rowconfigure((0, 1, 2), weight=1)
    # Dicionário de configuração estética padrão para os botões da tela principal
    config_base = {
   'master':janela,
    'fg': "#210C21",          
    'bg':"SystemButtonFace", 
    'width':35,             
    'height':2,             
    'bd':2,                 
    'relief':"solid",        
    'highlightbackground':"#21180A", 
    'highlightcolor':"#21180A",
    'activebackground': "#21180A",
    }
    # Instancia os botões do menu principal usando o desempacotamento do dicionário config_base
    adicionar = Button(**config_base,text="Adicionar Aluno",command=Adicionar).grid(row=0,column=0, columnspan=1)
    mostrar = Button(**config_base,text="Mostrar Alunos", command=Mostrar).grid(row=0,column=2, columnspan=1)
    apagar = Button(**config_base,text="Apagar Aluno", command=Apagar).grid(row=0,column=4, columnspan=1)
    consultar = Button(**config_base,text="Consultar Aluno", command=Consultar).grid(row=1,column=0, columnspan=1)
    modificar = Button(**config_base,text="Modificar Aluno", command=Alterar).grid(row=1,column=2, columnspan=1)
    janela.mainloop()

# Cria e retorna uma janela secundária padronizada para as funcionalidades do sistema
def SubJanela():
    janela = Toplevel()
    janela.geometry("800x450")
    janela.config(bg="#041C1F")
    janela.grid_columnconfigure((0, 1, 2, 3,4,5), weight=1)
    janela.grid_rowconfigure((0, 1, 2), weight=1)
    return janela

# Interface para o formulário de cadastro de novo aluno
def Adicionar():
    janela = SubJanela()
    janela.title("Adicionar Aluno")
    config_base = {
   'master':janela,
    'fg': "#210C21",          
    'bg':"SystemButtonFace",                  
    }
    # Especialização da configuração para botões de confirmação (verde)
    config_botao={
        **config_base,
       'bg' : "#104103",
       'width':35,             
        'height':2,             
        'bd':2,
    }
    #Label é um texto que eu posso mostrar na janela
    Label(**config_base, text="Nome do Aluno: ").grid(row=0, column=0)
    #Entry é um campo de texto que o usuário vai escreve algo
    ent_nome = Entry(**config_base)
    ent_nome.grid(row=0, column=1)

    Label(**config_base, text="Nota do Simulado 1: ").grid(row=0, column=3)
    ent_sim1 = Entry(**config_base)
    ent_sim1.grid(row=0, column=4)

    Label(**config_base, text="Nota do Simulado 2: ").grid(row=1, column=0)
    ent_sim2 = Entry(**config_base)
    ent_sim2.grid(row=1, column=1)

    Label(**config_base, text="Nota da AV: ").grid(row=1, column=3)
    ent_av = Entry(**config_base)
    ent_av.grid(row=1, column=4)

    Label(**config_base, text="Nota da AVS: ").grid(row=2, column=0)
    ent_avs = Entry(**config_base)
    ent_avs.grid(row=2, column=1)

    # Botão que coleta os dados das Entries e envia para a lógica de validação/inserção
    enviar = Button(**config_botao, text="Enviar", 
                    command=lambda: funcoes.adicionar(
                        nome=ent_nome.get(), 
                        simulado1=ent_sim1.get(), 
                        simulado2=ent_sim2.get(), 
                        av=ent_av.get(), 
                        avs=ent_avs.get(), 
                        janela=janela))
    enviar.grid(row=3,column=2, columnspan=2, sticky="nsew")
    
# Interface que exibe a listagem textual de todos os alunos cadastrados
def Mostrar():
    janela = SubJanela()
    janela.geometry("900x450")
    janela.title("Mostrar Alunos")
    config_base = {
   'master':janela,
    'fg': "#210C21",          
    'bg':"SystemButtonFace",                  
    }
    mostrar = Text(**config_base,width=400 , height=200)
    mostrar.pack(padx=10, pady=10)
    
    # Obtém a string formatada do banco de dados e insere no widget de texto
    dados_alunos = funcoes.mostrar()
    if dados_alunos:
        mostrar.insert("1.0", dados_alunos)

# Interface para exclusão de alunos baseada na matrícula
def Apagar():
    janela = SubJanela()
    janela.title("Apagar Aluno") 
    config_base = {
   'master':janela,
    'fg': "#210C21",          
    'bg':"SystemButtonFace",                  
    }
    janela2 = SubJanela()
    janela2.title("Apagar Aluno") 
    config_base2 = {
   'master':janela2,
    'fg': "#210C21",          
    'bg':"SystemButtonFace",                  
    }
    # Estilo visual para ação crítica (vermelho)
    config_botao={
        **config_base2,
       'bg' : "#690404", 
       'width':35,             
        'height':2,           
        'bd':2,
    }
    Label(**config_base, text=funcoes.mostrar()).grid(row=0, column=0, columnspan=1, rowspan=2)
    Label(**config_base2, text="Digite a Matrícula do Aluno que você deseja apagar: ").grid(row=0, column=3)
    
    ent_id = Entry(**config_base2)
    ent_id.grid(row=0, column=4)

    # Função interna para gerenciar a chamada de exclusão e tratamento de erros de input
    def miniapagar(resultado,janela,idAluno):
        matricula = idAluno.get()
        resultado = funcoes.apagar(janela=janela,idAluno=matricula)
        if resultado == "Erro ao apagar aluno":
            messagebox.showerror("Erro ao apagar aluno","Matrícula não encontrada ou você não digitou um número válido")
        

    enviar = Button(**config_botao, text="Apagar", command=lambda: miniapagar(resultado=None, janela=[janela, janela2], idAluno=ent_id))
    enviar.grid(row=3,column=3, columnspan=2, sticky="nsew", padx=10, pady=10)

# Interface de busca que permite filtrar por nome ou por situação acadêmica
def Consultar():
    # Callback que processa o resultado da busca e exibe em uma nova janela de resposta
    def miniconsultar(janela,entrada,acao):
            texto_resultado = funcoes.consultar(janela_busca=janela, entrada=entrada,acao=acao)
            janela_res = SubJanela()
            janela_res.title("Resultado da Consulta")
            Label(janela_res, text=texto_resultado, fg="#210C21", 
                  bg="SystemButtonFace", 
                  justify="left").pack(padx=20, pady=20)
    # Diálogo inicial para definir o tipo de filtro desejado
    opcao = messagebox.askyesno("Escolha opção", "Aperta Sim para consultar por nome ou Não para consultar por situação")
    if opcao:
        janela = SubJanela()
        janela.title("Consultar Aluno") 
        config_base = {
   'master':janela,
    'fg': "#210C21",          
    'bg':"SystemButtonFace",                  
    }   
        config_botao={
        **config_base,
       'bg' : "#104103",
       'width':35,             
        'height':2,             
        'bd':2,
    }
        Label(**config_base, text="Nome do Aluno: ").grid(row=0, column=0)
        entrada_consulta = Entry(**config_base)
        entrada_consulta.grid(row=0, column=1)
        enviar = Button(**config_botao, text="Enviar", command=lambda: miniconsultar(janela=janela,entrada=entrada_consulta.get(),acao=1))
        enviar.grid(row=3,column=2, columnspan=2, sticky="nsew",padx=10, pady=10)
        
    # Caso a busca seja por situação (Aprovado/Reprovado), utiliza Radiobuttons
    else:
        janela = SubJanela()
        janela.title("Consultar Aluno") 
        config_base = {
   'master':janela,
    'fg': "#210C21",          
    'bg':"SystemButtonFace",                  
    }   
        config_botao={
        **config_base,
       'bg' : "#104103",
       'width':35,             
        'height':2,             
        'bd':2,
    }
        Label(**config_base, text="Escolhar uma das situações").grid(row=0, column=0)
        valor_para_opcao = StringVar()
        Radiobutton(**config_base,text="Aprovado",variable=valor_para_opcao
                    , value="Aprovado").grid(row=1,column=0)
        Radiobutton(**config_base,text="Reprovado",variable=valor_para_opcao
                    , value="Reprovado").grid(row=1,column=1)
        Button(**config_botao,text="Enviar",
               command=lambda: miniconsultar(janela=janela,entrada=valor_para_opcao.get(),acao=2)).grid(row=3,column=2,columnspan=2
                                                          ,padx=10,pady=10)

# Interface para modificação de dados de um aluno já existente
def Alterar():
    alunos = TodosAlunos()
    janela = SubJanela()
    janela.title("Modifica Dados")
    config_base = {
   'master':janela,
    'fg': "#210C21",          
    'bg':"SystemButtonFace",                  
    }
    config_botao={
        **config_base,
       'bg' : "#104103",
       'width':35,             
        'height':2,             
        'bd':2,
    }
    Label(**config_base, text="Matrícula do Aluno: ").grid(row=0, column=0)
    mat_aluno = Entry(**config_base)
    mat_aluno.grid(row=0, column=1)
    Label(**config_base, text="novo nome para Aluno: ").grid(row=1, column=0)
    ent_nome = Entry(**config_base)
    ent_nome.grid(row=1, column=1)

    Label(**config_base, text="Nova nota para Simulado 1: ").grid(row=1, column=2)
    ent_sim1 = Entry(**config_base)
    ent_sim1.grid(row=1, column=3)

    Label(**config_base, text="Nova nota para Simulado 2: ").grid(row=1, column=4)
    ent_sim2 = Entry(**config_base)
    ent_sim2.grid(row=1, column=5)

    Label(**config_base, text="Nova nota para AV: ").grid(row=2, column=0)
    ent_av = Entry(**config_base)
    ent_av.grid(row=2, column=1)

    Label(**config_base, text="Nova nota para AVS: ").grid(row=2, column=2)
    ent_avs = Entry(**config_base)
    ent_avs.grid(row=2, column=3)

    # Envia os dados para a função de alteração que tratará apenas os campos preenchidos
    enviar = Button(**config_botao, text="Alterar", 
                    command=lambda: funcoes.alterar(
                        quem = mat_aluno.get(),
                        nome=ent_nome.get(), 
                        simulado1=ent_sim1.get(), 
                        simulado2=ent_sim2.get(), 
                        av=ent_av.get(), 
                        avs=ent_avs.get(), 
                        janela=janela))
    enviar.grid(row=3,column=2, columnspan=2, sticky="nsew")

# Janela auxiliar que serve apenas para listar as matrículas durante processos de edição/exclusão
def TodosAlunos():
        janela = SubJanela()
        janela.title("Todos Alunos") 
        config_base = {
   'master':janela,
    'fg': "#210C21",          
    'bg':"SystemButtonFace",                  
    }   
        config_botao={
        **config_base,
       'bg' : "#104103",
       'width':35,             
        'height':2,             
        'bd':2,
    }
        Label(**config_base, text=funcoes.mostrar()).grid(row=0, column=0, columnspan=1, rowspan=2)
        return janela

if __name__ == "__main__":
    Inicio()
