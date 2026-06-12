import customtkinter as ctk
from tkinter import messagebox,Label
from tkvideo import tkvideo
from PIL import Image, ImageTk 
import os , ctypes , pygame, funções,dados, requests,bancodedados
#{'nome': nome, 'notafinal': maiorNota, 'situacao': situacao}
# ver para base https://www.youtube.com/watch?v=hIJ6sf0x3Yw&list=PL6KTZQDPGs5gZYtK9YblxA-Te9wQM8mdb
# Configuração de aparência global
#deixar com colunas https://youtu.be/YmXEckXauKc?si=LfXWyREmNNLDfdCQ
#pip install pillow customtkinter pygame requests tkvideo
#pip uninstall pillow customtkinter pygame requests tkvideo
ctk.set_appearance_mode("System") # "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue") 
# Temas: "blue", "green", "dark-blue"
try:
    pygame.init()
    pygame.mixer.init()
    #os.path.dirname(__file__) pegar o local do meu código que está rodando   ".." voltar um passo
    caminho_musica = os.path.join(os.path.dirname(__file__),'..','Reze.mp3')
    caminho_video = os.path.join(os.path.dirname(__file__),'..','Rezedance.mp4')
    pygame.mixer.music.load(caminho_musica)
except:
    pass #caso não tenha a musica e o vídeo
Dado = bancodedados.LigacaoComDadosSalvos()
if len(Dado) >= 1:
    ListarcomNome = Dado
elif len(dados.ListarcomNome)>=1:
    ListarcomNome = dados.ListarcomNome
elif len(dados.ListarcomNome)<1 and len(Dado)<1:
    ListarcomNome = []
else:
    #Somente para garantir
    ListarcomNome = []

def ChamarJanela():
    # Em CTK usamos CTk() em vez de Tk()
    Janela = ctk.CTk()
    Janela.geometry("1200x780")
    Janela.maxsize(1200,780)
    Janela.minsize(1200,780)
    Janela.title("Beta v0.2.1 - Modern Edition")
    # Agora configuramos as colunas 0, 1 e 2
    Janela.grid_columnconfigure((0, 1, 2), weight=1)

    # Agora configuramos as linhas 0, 1 e 2
    Janela.grid_rowconfigure((0, 1, 2), weight=1)
    
    diretorio_atual = os.path.dirname(__file__)
    
    # Gerenciamento de Ícone
    try:
        caminho_icone = os.path.join(diretorio_atual, "..", "makimaIcon.ico")
        Janela.iconbitmap(caminho_icone)
    except:
        pass # Caso o ícone não exista

    # Imagem de Fundo
    try:
        caminho_bg = os.path.join(diretorio_atual, "..", "Makima.jpg")
        img_bg = Image.open(caminho_bg)
        bg_image = ctk.CTkImage(light_image=img_bg, dark_image=img_bg, size=(1200, 780))
        bglabel = ctk.CTkLabel(Janela, image=bg_image, text="")
        bglabel.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        pass #Caso a imagem não existe
    # CTkImage é a forma moderna de lidar com imagens no CustomTkinter

    # Botões Estilizados
    btn_params = {
        "master": Janela, 
        "fg_color": "transparent", 
        "hover_color": "#120C4D",
        "border_width": 2,
        "text_color": "white",
        "width": 280,   
        "height": 150,
        "border_color": "white",
        "bg_color": "transparent",
        "corner_radius": 10
    }
    
    #(row=0, column=1, sticky="nsew", padx=10, pady=10)
    
    ctk.CTkButton(**btn_params, text="Adicionar Aluno", command=Adicionar).grid(row=0, column=0, padx=50, pady=50)
    ctk.CTkButton(**btn_params, text="Mostrar os Alunos", command=Mostrar).grid(row=0, column=1, padx=50, pady=50)
    ctk.CTkButton(**btn_params, text="Apagar o Aluno", command=Apagar).grid(row=0, column=2, padx=50, pady=50)
    
    ctk.CTkButton(**btn_params, text="Explicação", command=Explicacao).grid(row=1, column=0, columnspan=3,sticky="ew", padx=50, pady=50)
    
    ctk.CTkButton(**btn_params, text="Consultar", command=Consultar).grid(row=2, column=0, padx=50, pady=50)
    ctk.CTkButton(**btn_params, text="Alterar", command=Alterar).grid(row=2, column=1, padx=50, pady=50)

    """
    ctk.CTkButton(**btn_params, text="Adicionar Aluno", command=Adicionar, hover_color="Red").place(x=500, y=200)
    ctk.CTkButton(**btn_params, text="Mostrar os Alunos", command=Mostrar, hover_color="Red").place(x=660, y=200)
    ctk.CTkButton(**btn_params, text="Apagar o Aluno", command=Apagar, hover_color="Red").place(x=820, y=200)
    ctk.CTkButton(**btn_params, text="Explicação", command=Explicacao, hover_color="Red").place(x=500, y=250)
    ctk.CTkButton(**btn_params, text="Consultar", command=Consultar, hover_color="Red").place(x=660, y=250)
    ctk.CTkButton(**btn_params, text="Alterar", command=Alterar, hover_color="Red").place(x=820, y=250)
    """

    Janela.mainloop()

def CriarSubJanela(imagem, titulo):
    # CTkToplevel para subjanelas
    Janela = ctk.CTkToplevel()
    Janela.geometry("800x450")
    Janela.maxsize(800,450)
    Janela.minsize(800,450)
    Janela.title(titulo)
    Janela.grab_set() # Faz a janela ficar na frente da principal
    try:
        diretorio_atual = os.path.dirname(__file__)
        caminho_foto = os.path.join(diretorio_atual, "..", imagem)
        
        img_sub = Image.open(caminho_foto)
        bg_sub = ctk.CTkImage(light_image=img_sub, dark_image=img_sub, size=(800, 450))
        
        bglabel = ctk.CTkLabel(Janela, image=bg_sub, text="")
        bglabel.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        bglabel = ctk.CTkLabel(Janela, text="")
        bglabel.place(x=0, y=0, relwidth=1, relheight=1)
        pass #Caso a imagem não existe
    
    return Janela, bglabel

def Adicionar():
    JanelaSub, PanoDeFundo = CriarSubJanela("rias.jpg", "Isagi Yoichi")
    """
    configuracoes_Padroes= {
        "master": PanoDeFundo, 
        "fg_color": "transparent", 
        "text_color": "white",
        "width": 280,   
        "height": 150,
        "bg_color": "transparent",
        "corner_radius": 5
    }
    """
    config_base = {
    "master": JanelaSub,
    "text_color": "white",
    "fg_color": "transparent"
    }
    config_interativo = {
        **config_base,
        "width": 280,
        "height": 35, # 150 era muito alto, 35-40 é o padrão ideal
        "corner_radius": 5,
    }

    JanelaSub.grid_columnconfigure((0, 1), weight=1)
    JanelaSub.grid_rowconfigure((0, 1, 2), weight=1)
    
    ctk.CTkLabel(**config_base, text="Nome do Aluno: ").grid(row=0,column=0,padx=20, pady=20)
    ctk.CTkLabel(**config_base, text="Nota AV:").grid(row=1,column=0,padx=20, pady=20)
    ctk.CTkLabel(**config_base, text="Nota AVS:").grid(row=2,column=0,padx=20, pady=20)
    CaixaDeTexto = ctk.CTkEntry(**config_interativo, justify="center")
    CaixaDeTexto.grid(row=0,column=1,padx=20, pady=20)

    notaDaAV = ctk.CTkEntry(**config_interativo, justify="center")
    notaDaAV.grid(row=1,column=1,padx=20, pady=20)

    notaDaAVS = ctk.CTkEntry(**config_interativo, justify="center")
    notaDaAVS.grid(row=2,column=1,padx=20, pady=20)

    ctk.CTkButton(**config_interativo, hover_color= "#A7CA0A",border_width= 2,border_color="white",text="Enviar", 
                  command=lambda: funções.AdicionarNaLista(CaixaDeTexto.get(), notaDaAV.get(), 
                                                           notaDaAVS.get(),janela=JanelaSub)).grid(row=3,column=0,columnspan=2,padx=20, pady=20,sticky="ew")


def Mostrar():
    JanelaSub, PanoDeFundo = CriarSubJanela("reze.jpg", "Michael Kaiser")
    texto = funções.MostrarAlunos()
    config_base = {
    "master": JanelaSub,
    "text_color": "white",
    "fg_color": "transparent"
    }
    config_interativo = {
        **config_base,
        "width": 280,
        "height": 35, # 150 era muito alto, 35-40 é o padrão ideal
        "corner_radius": 5
    }
    
    JanelaSub.grid_columnconfigure((0, 1,2), weight=1)
    JanelaSub.grid_rowconfigure((0,1,2), weight=1)
    
    # Label com fundo para melhor leitura sobre a imagem
    ctk.CTkLabel(**config_base, text=texto, justify="center", 
                 corner_radius=25, width=300,height=300).grid(row=0,column=0,rowspan=3,columnspan=3)

def Apagar():
    JanelaSub, PanoDeFundo = CriarSubJanela("power.jpg", "Jinpachi Ego")
    config_base = {
    "master": JanelaSub,
    "text_color": "white",
    "fg_color": "transparent"
    }
    config_interativo = {
        **config_base,
        "width": 280,
        "height": 35, # 150 era muito alto, 35-40 é o padrão ideal
        "corner_radius": 5
    }
    botoes={
        **config_interativo,
         "hover_color": "#E9630A",
         "border_width": 2,
         "border_color":"white"
    }
    JanelaSub.grid_columnconfigure((0, 1,2), weight=1)
    JanelaSub.grid_rowconfigure((0,1,2), weight=1)
    ctk.CTkLabel(**config_base, text="Número para Apagar:" , justify="center").grid(row=0,column=0,padx=20,pady=20)
    
    CaixaDeTexto = ctk.CTkEntry(**config_interativo, justify="center")
    CaixaDeTexto.grid(row=0,column=1,padx=20,pady=20)

    lista_nomes = funções.ListarNomes()
    ctk.CTkLabel(**config_base, text=lista_nomes, justify="center" , 
                ).grid(row=1,column=0,columnspan=3,sticky="nsew",padx=20,pady=20)
    
    ctk.CTkButton(**botoes, text="Apagar", command=lambda: 
                  funções.ApagarNaLista(CaixaDeTexto.get(),janela=JanelaSub)).grid(row=2,column=0,columnspan=3)

def Explicacao():
    JanelaSub, PanoDeFundo = CriarSubJanela("A.jpg", "Rin Itoshi")
    botoes = {
    "master": JanelaSub,
    "text_color": "white",
    "fg_color": "transparent",
    "width": 280,
    "height": 35, # 150 era muito alto, 35-40 é o padrão ideal
    "corner_radius": 5,
    "hover_color": "#33DF11",
    "border_width": 2,
    "border_color":"white"
    }
    JanelaSub.grid_columnconfigure((0, 1,2), weight=1)
    JanelaSub.grid_rowconfigure((0,1,2,3,4), weight=1)
    # 1. Botão de Controle de Mídia (Row 0)
    lbvideo=Label(JanelaSub,text="Vídeo")
    lbvideo.grid(row=0,column=1,columnspan=2,rowspan=5)
    Video= tkvideo(caminho_video,lbvideo,loop=3)
    ControleMidia = ctk.CTkButton(**botoes , text="PLAY ▶")
    ControleMidia.configure(command=lambda: Midia(atributo=ControleMidia, tipo=".mp3"))
    ControleMidia.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    ControleVideo = ctk.CTkButton(**botoes , text="PLAY ▶")
    ControleVideo.configure(command=lambda: Midia(atributo=ControleVideo, tipo=".mp4",video=Video))
    ControleVideo.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # 2. Botão Ir para Site (Row 1)
    IrParaSite = ctk.CTkButton(**botoes , text="Ir para um site com a explicação", 
                            command=lambda: funções.AbrirNavegador(url="https://shre.ink/projetodepython"))
    IrParaSite.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

    # 4. Botão Gera Relatório (Movido para Row 4)
    GeraRelatorio = ctk.CTkButton(**botoes , text="Gera relatório .txt", 
                                command=lambda: funções.GerarRelatorio(tipo=".txt")) 
    GeraRelatorio.grid(row=4, column=0, padx=10, pady=10, sticky="ew")




def Consultar():
    JanelaSub,PanoDeFundo = CriarSubJanela("B.jpg", "Satorou Gojo")
    botoes = {
    "master": JanelaSub,
    "text_color": "white",
    "fg_color": "transparent",
    "width": 280,
    "height": 35, # 150 era muito alto, 35-40 é o padrão ideal
    "corner_radius": 5,
    "hover_color": "#E60CC8",
    "border_width": 2,
    "border_color":"white"
    }
    config_base = {
    "master": JanelaSub,
    "text_color": "white",
    "fg_color": "transparent"
    }
    config_interativo = {
        **config_base,
        "width": 280,
        "height": 35, # 150 era muito alto, 35-40 é o padrão ideal
        "corner_radius": 5
    }
    JanelaSub.grid_columnconfigure((0, 1,2), weight=1)
    JanelaSub.grid_rowconfigure((0,1,2), weight=1)
    ctk.CTkLabel(**config_base,text="Digite o Nome de Quem você quer consultar: ").grid(row=0,column=0,padx=20,pady=20)
    nome = ctk.CTkEntry(**config_interativo,justify="center")
    nome.grid(row=0,column=1,columnspan=2,padx=20,pady=20,sticky="nsew")
    ctk.CTkButton(**botoes, text="Enviar", 
                  command=lambda: funções.ConsultarNaLista(nome=nome.get(),janela=JanelaSub)).grid(
                      row=2,column=0,columnspan=3,padx=20,pady=20)

def Alterar():
    JanelaSub,PanoDeFundo = CriarSubJanela("C.jpg", "DIE WITH A SMILE「AMV」")
    # --- NOVA LABEL: nomes_id (Canto Esquerdo) ---
    # Ocupando a lateral esquerda
    texto= funções.ListarNomes()
    botoes = {
    "master": JanelaSub,
    "text_color": "white",
    "fg_color": "transparent",
    "width": 280,
    "height": 35, # 150 era muito alto, 35-40 é o padrão ideal
    "corner_radius": 5,
    "hover_color": "#E60CC8",
    "border_width": 2,
    "border_color":"white"
    }
    config_base = {
    "master": JanelaSub,
    "text_color": "white",
    "fg_color": "transparent"
    }
    config_interativo = {
        **config_base,
        "width": 280,
        "height": 35, # 150 era muito alto, 35-40 é o padrão ideal
        "corner_radius": 5
    }
    JanelaSub.grid_columnconfigure((0, 1,2), weight=1)
    JanelaSub.grid_rowconfigure((0,1,2,3,4,5), weight=1)
    ctk.CTkLabel(**config_base, text=texto,corner_radius=5, width=100).grid(row=0,column=0,columnspan=2,padx=20,pady=20)

    # --- LINHA 1 (Y=20): ID ---
    # Ajustei o x para 120 para dar espaço à nova label
    ctk.CTkLabel(**config_base, text="Digite o ID:  ", corner_radius=5).grid(
        row=1,column=0,padx=20,pady=20)
    id_aluno = ctk.CTkEntry(**config_interativo,justify="center")
    id_aluno.grid(row=1,column=1,columnspan=2,padx=20,pady=20)

    # --- LINHA 2 (Y=70): Nome ---
    ctk.CTkLabel(**config_base, text="Nome do Aluno: ", corner_radius=5).grid(
        row=2,column=0,padx=20,pady=20)
    CaixaDeTexto = ctk.CTkEntry(**config_interativo,justify="center")
    CaixaDeTexto.grid(row=2,column=1,columnspan=2,padx=20,pady=20)

    # --- LINHA 3 (Y=120): Nota AV ---
    ctk.CTkLabel(**config_base, text="Nota AV: ",corner_radius=5).grid(
        row=3,column=0,padx=20,pady=20)
    notaDaAV = ctk.CTkEntry(**config_interativo,justify="center")
    notaDaAV.grid(row=3,column=1,columnspan=2,padx=20,pady=20)

    # --- LINHA 4 (Y=170): Nota AVS ---
    ctk.CTkLabel(**config_base, text="Nota AVS:", corner_radius=5).grid(
        row=4,column=0,padx=20,pady=20)
    notaDaAVS = ctk.CTkEntry(**config_interativo,justify="center")
    notaDaAVS.grid(row=4,column=1,columnspan=2,padx=20,pady=20)

    # --- BOTÃO (Ajustado para o novo alinhamento) ---
    ctk.CTkButton(**botoes, text="Enviar", 
                command=lambda: funções.MudarNaLista(posicao=id_aluno.get(), nome=CaixaDeTexto.get(), 
                                                     av=notaDaAV.get(), avs=notaDaAVS.get(), janela=JanelaSub)).grid(row=5,column=0,columnspan=3,sticky="ew",padx=20,pady=20)



def Midia(atributo="Quem Eu vou mexer",tipo="tipo do arquivo que eu vou mexer",video="Se tem"):
       try:
            if tipo == ".mp3":
                texto = atributo.cget('text')
                if texto == "PLAY ▶":
                    atributo.configure(text="|◁ II ▷| STOP ⏹",fg_color="red")
                    #ínicio do Áudio
                    pygame.mixer.music.play(-1)
                    video.play()
                elif texto == "|◁ II ▷| PLAY ▶":
                    atributo.configure(text="|◁ II ▷| STOP ⏹",fg_color="red")
                    #Voltar aonde parou
                    pygame.mixer.music.unpause()
                    video.play()
                elif texto == "|◁ II ▷| STOP ⏹":
                    atributo.configure(text="|◁ II ▷| PLAY ▶",fg_color="green")
                    #Pausar o áudio
                    pygame.mixer.music.pause()
            elif tipo == ".mp4":
                video.play()
       except:
            pass #caso não tenha a musica e o vídeo
if __name__ == "__main__":
    ChamarJanela()
    funções.GerarRelatorio(tipo=".py")