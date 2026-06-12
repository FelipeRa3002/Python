import customtkinter as ctk
from tkinter import messagebox,Label
from tkvideo import tkvideo
from PIL import Image, ImageTk 
import os , ctypes , pygame,requests,json,alunos


url = "https://makima-deusa-default-rtdb.firebaseio.com/"
class CriadorDeTurma:
    def __init__(self,nomeDoObejto,Professor,materia):
        self.Alunos = []
        self.Professor = Professor
        self.Material = materia

class CriaçãoDoBancoDeDados:
    def __init__(self,nomeDoBancodeDado):
        pass
def janelaPrincipal():
    Janela = ctk.CTk()
    Janela.geometry("1200x780")
    Janela.maxsize(1200,780)
    Janela.minsize(1200,780)
    Janela.title("Beta v0.1.1 com class")
     # Agora configuramos as colunas 0, 1 e 2
    Janela.grid_columnconfigure((0, 1, 2,3), weight=1)

    # Agora configuramos as linhas 0, 1 e 2
    Janela.grid_rowconfigure((0, 1, 2,3), weight=1)
    config_base = {
    "master": Janela,
    "text_color": "white"
    }
    config_interativo = {
        **config_base,
        "width": 280,
        "height": 35, # 150 era muito alto, 35-40 é o padrão ideal
        "corner_radius": 5,
    }
    Config_botoes ={
        **config_interativo,
        "border_width": 2,
        "border_color":"white"
    }
    NomeTurma = ctk.CTkLabel(**config_base,text="Nome para Turma").grid(row=0,column=0,padx=20,pady=20)
    NomeDoProfessor = ctk.CTkLabel(**config_base,text="Nome do Professor").grid(row=1,column=0,padx=20,pady=20)
    SenhaDoProfessor = ctk.CTkLabel(**config_base,text="Senha").grid(row=1,column=2,padx=20,pady=20)
    NomeDaMaterial = ctk.CTkLabel(**config_base,text="Nome da matéria").grid(row=2,column=0,padx=20,pady=20)
    # --- Entradas (Entries) para os campos ---
    # Nome da Turma
    NomeTurmaDigitado = ctk.CTkEntry(**config_interativo, placeholder_text="Digite o nome da turma")
    NomeTurmaDigitado.grid(row=0, column=1, padx=20, pady=20)

    # Nome do Professor
    NomeDoProfessorDigitado = ctk.CTkEntry(**config_interativo, placeholder_text="Digite o nome do professor")
    NomeDoProfessorDigitado.grid(row=1, column=1, padx=20, pady=20)

    # Senha do Professor 
    SenhaDoProfessorDigitada = ctk.CTkEntry(**config_interativo, placeholder_text="Digite a senha", show="*")
    SenhaDoProfessorDigitada.grid(row=1, column=3, padx=20, pady=20)

    # Nome da Matéria
    NomeDaMateriaDigitado = ctk.CTkEntry(**config_interativo, placeholder_text="Ex: Matemática")
    NomeDaMateriaDigitado.grid(row=2, column=1, padx=20, pady=20)
    print(f"Senha: {SenhaDoProfessorDigitada}")
    print(f"Professor: {NomeDoProfessorDigitado}")
    print(f"Turma: {NomeTurmaDigitado}")
    print(f"Materia: {NomeDaMateriaDigitado}")
    #Botões
    AbrirTurmas = ctk.CTkButton(**Config_botoes,text="Ver turmas que já existe",hover_color="#05E7DC",command= lambda: TurmasExiste(janela=Janela)).grid(row=3,column=0,columnspan=2,padx=20,pady=20,sticky="ew")
    CriaTurma = ctk.CTkButton(**Config_botoes,text="Criar", fg_color="#A7CA0A",hover_color="#30DA06",command= lambda: turmanova(senhadoprofessor=SenhaDoProfessorDigitada.get(),NomeDoProfessor=NomeDoProfessorDigitado.get(),NomeTurma=NomeTurmaDigitado.get(),NomeDaMateria=NomeDaMateriaDigitado.get()))
    CriaTurma.grid(row=3,column=2,columnspan=2,padx=20,pady=20,sticky="ew")
    Janela.mainloop()

def turmanova(senhadoprofessor,
        NomeDoProfessor,NomeTurma,
        NomeDaMateria):
    NDP = NomeDoProfessor
    SDP = senhadoprofessor
    M = NomeDaMateria 
    NomeDaTurma = NomeTurma 
    global url
    urllocal = url
    Unico = True
    tudo = requests.get(f'{urllocal}/.json')
    tudo = tudo.json()
    nomenovo = NomeDaTurma.replace(" ", "_")
    for i in tudo:
        nomeexite = i.replace(" ", "_")
        if nomeexite == nomenovo:
            Unico = False
    if Unico:  
        dados = {NomeDaTurma:
                {'Professor':{'nome': NDP,'senha':SDP,'materia':M},
                'Alunos': {'nome':"Fulano",'notafinal':10,'situacao':"Aprovado"}
                }
                }
        requests.patch(url=f'{urllocal}.json',data=json.dumps(dados))

def TurmasExiste(janela):
    Subjanela = ctk.CTkToplevel()
    Subjanela.geometry("800x520")
    Subjanela.maxsize(800,520)
    Subjanela.minsize(800,520)
    Subjanela.grab_set()
      # Agora configuramos as colunas 0, 1 e 2
    Subjanela.grid_columnconfigure((0, 1, 2,3), weight=1)

    # Agora configuramos as linhas 0, 1 e 2
    Subjanela.grid_rowconfigure((0, 1, 2,3), weight=1)
    url = "https://makima-deusa-default-rtdb.firebaseio.com/"
    tudo = requests.get(f'{url}/.json')
    tudo = tudo.json()
    linha = 0
    config_botoes = {
    "master": Subjanela,
    "text_color": "white",
    "width": 280,
    "height": 35, # 150 era muito alto, 35-40 é o padrão ideal
    "corner_radius": 5,
    "hover_color": "#A7CA0A",
    "border_width": 2,
    "border_color":"white"
    }
    """
    coluna = 0
    linha=0
    for nomeparabotoes in tudo:
        #linha
        nome_var = nomeparabotoes.replace(" ", "_")
        alunos= 0
        funcao = 'alunos.chamarjanelaturma'
        #nomedaturma,professor,nomedoobjeto,urlpersonalizada,janela
        try:
            dados = nomeparabotoes['Professor']
            botao = f"Botãopara{nome_var} = ctk.CTkButton(**config_botoes,text={nomeparabotoes},command= lambda: {funcao}(urlpersonalizada={nomeparabotoes},nomedaturma={nome_var},nomedoobjeto={nomeparabotoes},professor = {dados},janela=Subjanela))"
        except:
             dados = {'nome':'Teste','senha':1234}
             botao = f"Botãopara{nome_var} = ctk.CTkButton(**config_botoes,text={nomeparabotoes},command= lambda: {funcao}(urlpersonalizada={nomeparabotoes},nomedaturma={nome_var},nomedoobjeto={nomeparabotoes},professor = {dados},janela=Subjanela))"
        possicao = f".grid(row={linha},column={coluna},padx=20,pady=20,sticky='ew')"
        coluna+=1
        exec(botao + possicao)
        if coluna >= 4:
            coluna=0
            linha+=1
           
        if linha >= 3:
                break
        """
    linha = 0
    coluna = 0
    
    for nome_turma in tudo:
        # Tenta pegar os dados do professor com segurança
        dados_professor = tudo[nome_turma].get('Professor', {'nome': 'Teste', 'senha': 1234})
        
        # Criamos o botão diretamente sem usar exec()
        # O segredo do lambda: n=nome_turma, d=dados_professor salva o valor ATUAL da iteração
        btn = ctk.CTkButton(
            **config_botoes, 
            text=nome_turma,
            command=lambda n=nome_turma, d=dados_professor: alunos.chamarjanelaturma(
                urlpersonalizada=n, 
                nomedaturma=n, 
                nomedoobjeto=n, 
                professor=d, 
                janela=Subjanela
            )
        )
        btn.grid(row=linha, column=coluna, padx=20, pady=20, sticky="ew")

        coluna += 1
        if coluna >= 4:
            coluna = 0
            linha += 1
        
        if linha >= 3:
            break



       

janelaPrincipal()