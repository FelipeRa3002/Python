import customtkinter as ctk
from tkinter import Label
from tkvideo import tkvideo
from PIL import Image
import os
import pygame

import bancodedados
import funções

try:
    import dados
except Exception:
    class dados:
        ListarcomNome = []

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

pygame.init()
pygame.mixer.init()

caminho_musica = os.path.join(os.path.dirname(__file__), "..","..","..","..", "Reze.mp3")
caminho_video = os.path.join(os.path.dirname(__file__), "..","..","..","..", "Rezedance.mp4")
try:
    pygame.mixer.music.load(caminho_musica)
except Exception:
    pass

# carrega do Firebase no início
Dado = bancodedados.LigacaoComDadosSalvos()
if len(Dado) >= 1:
    dados.ListarcomNome = Dado
elif not hasattr(dados, "ListarcomNome") or dados.ListarcomNome is None:
    dados.ListarcomNome = []

# compatibilidade
ListarcomNome = dados.ListarcomNome


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x780")
        self.maxsize(1200, 780)
        self.minsize(1200, 780)
        self.title("Beta v0.2.1 - Modern Edition")

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self._montar_background()
        self._montar_botoes()

    def _montar_background(self):
        diretorio_atual = os.path.dirname(__file__)

        try:
            caminho_icone = os.path.join(diretorio_atual, "..","..","..","..", "makimaIcon.ico")
            self.iconbitmap(caminho_icone)
        except Exception:
            pass

        caminho_bg = os.path.join(diretorio_atual, "..","..","..","..", "Makima.jpg")
        img_bg = Image.open(caminho_bg)
        bg_image = ctk.CTkImage(light_image=img_bg, dark_image=img_bg, size=(1200, 780))
        bglabel = ctk.CTkLabel(self, image=bg_image, text="")
        bglabel.place(x=0, y=0, relwidth=1, relheight=1)

    def _montar_botoes(self):
        btn_params = {
            "master": self,
            "fg_color": "transparent",
            "hover_color": "#120C4D",
            "border_width": 2,
            "text_color": "white",
            "width": 280,
            "height": 150,
            "border_color": "white",
            "bg_color": "transparent",
            "corner_radius": 10,
        }

        ctk.CTkButton(**btn_params, text="Adicionar Aluno", command=self.adicionar).grid(row=0, column=0, padx=50, pady=50)
        ctk.CTkButton(**btn_params, text="Mostrar os Alunos", command=self.mostrar).grid(row=0, column=1, padx=50, pady=50)
        ctk.CTkButton(**btn_params, text="Apagar o Aluno", command=self.apagar).grid(row=0, column=2, padx=50, pady=50)

        ctk.CTkButton(**btn_params, text="Explicação", command=self.explicacao).grid(
            row=1, column=0, columnspan=3, sticky="ew", padx=50, pady=50
        )

        ctk.CTkButton(**btn_params, text="Consultar", command=self.consultar).grid(row=2, column=0, padx=50, pady=50)
        ctk.CTkButton(**btn_params, text="Alterar", command=self.alterar).grid(row=2, column=1, padx=50, pady=50)

    def criar_subjanela(self, imagem, titulo):
        Janela = ctk.CTkToplevel()
        Janela.geometry("800x450")
        Janela.maxsize(800, 450)
        Janela.minsize(800, 450)
        Janela.title(titulo)
        Janela.grab_set()

        diretorio_atual = os.path.dirname(__file__)
        caminho_foto = os.path.join(diretorio_atual, "..","..","..","..", imagem)

        img_sub = Image.open(caminho_foto)
        bg_sub = ctk.CTkImage(light_image=img_sub, dark_image=img_sub, size=(800, 450))

        bglabel = ctk.CTkLabel(Janela, image=bg_sub, text="")
        bglabel.place(x=0, y=0, relwidth=1, relheight=1)
        return Janela, bglabel

    # -------- telas ----------
    def adicionar(self):
        JanelaSub, _ = self.criar_subjanela("rias.jpg", "Isagi Yoichi")
        config_base = {"master": JanelaSub, "text_color": "white", "fg_color": "transparent"}
        config_interativo = {**config_base, "width": 280, "height": 35, "corner_radius": 5}

        JanelaSub.grid_columnconfigure((0, 1), weight=1)
        JanelaSub.grid_rowconfigure((0, 1, 2), weight=1)

        ctk.CTkLabel(**config_base, text="Nome do Aluno: ").grid(row=0, column=0, padx=20, pady=20)
        ctk.CTkLabel(**config_base, text="Nota AV:").grid(row=1, column=0, padx=20, pady=20)
        ctk.CTkLabel(**config_base, text="Nota AVS:").grid(row=2, column=0, padx=20, pady=20)

        CaixaDeTexto = ctk.CTkEntry(**config_interativo, justify="center")
        CaixaDeTexto.grid(row=0, column=1, padx=20, pady=20)

        notaDaAV = ctk.CTkEntry(**config_interativo, justify="center")
        notaDaAV.grid(row=1, column=1, padx=20, pady=20)

        notaDaAVS = ctk.CTkEntry(**config_interativo, justify="center")
        notaDaAVS.grid(row=2, column=1, padx=20, pady=20)

        ctk.CTkButton(
            **config_interativo,
            hover_color="#A7CA0A",
            border_width=2,
            border_color="white",
            text="Enviar",
            command=lambda: funções.AdicionarNaLista(CaixaDeTexto.get(), notaDaAV.get(), notaDaAVS.get(), janela=JanelaSub),
        ).grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

    def mostrar(self):
        JanelaSub, _ = self.criar_subjanela("reze.jpg", "Michael Kaiser")
        texto = funções.MostrarAlunos()
        config_base = {"master": JanelaSub, "text_color": "white", "fg_color": "transparent"}
        JanelaSub.grid_columnconfigure((0, 1, 2), weight=1)
        JanelaSub.grid_rowconfigure((0, 1, 2), weight=1)
        ctk.CTkLabel(**config_base, text=texto, justify="center", corner_radius=25, width=300, height=300).grid(
            row=0, column=0, rowspan=3, columnspan=3
        )

    def apagar(self):
        JanelaSub, _ = self.criar_subjanela("power.jpg", "Jinpachi Ego")
        config_base = {"master": JanelaSub, "text_color": "white", "fg_color": "transparent"}
        config_interativo = {**config_base, "width": 280, "height": 35, "corner_radius": 5}
        botoes = {**config_interativo, "hover_color": "#E9630A", "border_width": 2, "border_color": "white"}

        JanelaSub.grid_columnconfigure((0, 1, 2), weight=1)
        JanelaSub.grid_rowconfigure((0, 1, 2), weight=1)

        ctk.CTkLabel(**config_base, text="Número para Apagar:", justify="center").grid(row=0, column=0, padx=20, pady=20)
        CaixaDeTexto = ctk.CTkEntry(**config_interativo, justify="center")
        CaixaDeTexto.grid(row=0, column=1, padx=20, pady=20)

        lista_nomes = funções.ListarNomes()
        ctk.CTkLabel(**config_base, text=lista_nomes, justify="center").grid(
            row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=20
        )

        ctk.CTkButton(**botoes, text="Apagar", command=lambda: funções.ApagarNaLista(CaixaDeTexto.get(), janela=JanelaSub)).grid(
            row=2, column=0, columnspan=3
        )

    def explicacao(self):
        JanelaSub, _ = self.criar_subjanela("A.jpg", "Rin Itoshi")
        botoes = {
            "master": JanelaSub,
            "text_color": "white",
            "fg_color": "transparent",
            "width": 280,
            "height": 35,
            "corner_radius": 5,
            "hover_color": "#33DF11",
            "border_width": 2,
            "border_color": "white",
        }

        JanelaSub.grid_columnconfigure((0, 1, 2), weight=1)
        JanelaSub.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        lbvideo = Label(JanelaSub, text="Vídeo")
        lbvideo.grid(row=0, column=1, columnspan=2, rowspan=5)
        Video = tkvideo(caminho_video, lbvideo, loop=3)

        ControleMidia = ctk.CTkButton(**botoes, text="PLAY ▶")
        ControleMidia.configure(command=lambda: self.midia(atributo=ControleMidia, tipo=".mp3", video=Video))
        ControleMidia.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ControleVideo = ctk.CTkButton(**botoes, text="PLAY ▶")
        ControleVideo.configure(command=lambda: self.midia(atributo=ControleVideo, tipo=".mp4", video=Video))
        ControleVideo.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        IrParaSite = ctk.CTkButton(
            **botoes, text="Ir para um site com a explicação", command=lambda: funções.AbrirNavegador(url="https://shre.ink/projetodepython")
        )
        IrParaSite.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        GeraRelatorio = ctk.CTkButton(**botoes, text="Gera relatório .txt", command=lambda: funções.GerarRelatorio(tipo=".txt"))
        GeraRelatorio.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    def consultar(self):
        JanelaSub, _ = self.criar_subjanela("B.jpg", "Satorou Gojo")
        botoes = {
            "master": JanelaSub,
            "text_color": "white",
            "fg_color": "transparent",
            "width": 280,
            "height": 35,
            "corner_radius": 5,
            "hover_color": "#E60CC8",
            "border_width": 2,
            "border_color": "white",
        }
        config_base = {"master": JanelaSub, "text_color": "white", "fg_color": "transparent"}
        config_interativo = {**config_base, "width": 280, "height": 35, "corner_radius": 5}

        JanelaSub.grid_columnconfigure((0, 1, 2), weight=1)
        JanelaSub.grid_rowconfigure((0, 1, 2), weight=1)

        ctk.CTkLabel(**config_base, text="Digite o Nome de Quem você quer consultar: ").grid(row=0, column=0, padx=20, pady=20)
        nome = ctk.CTkEntry(**config_interativo, justify="center")
        nome.grid(row=0, column=1, columnspan=2, padx=20, pady=20, sticky="nsew")

        ctk.CTkButton(**botoes, text="Enviar", command=lambda: funções.ConsultarNaLista(nome=nome.get(), janela=JanelaSub)).grid(
            row=2, column=0, columnspan=3, padx=20, pady=20
        )

    def alterar(self):
        JanelaSub, _ = self.criar_subjanela("C.jpg", "DIE WITH A SMILE「AMV」")
        texto = funções.ListarNomes()

        botoes = {
            "master": JanelaSub,
            "text_color": "white",
            "fg_color": "transparent",
            "width": 280,
            "height": 35,
            "corner_radius": 5,
            "hover_color": "#E60CC8",
            "border_width": 2,
            "border_color": "white",
        }
        config_base = {"master": JanelaSub, "text_color": "white", "fg_color": "transparent"}
        config_interativo = {**config_base, "width": 280, "height": 35, "corner_radius": 5}

        JanelaSub.grid_columnconfigure((0, 1, 2), weight=1)
        JanelaSub.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        ctk.CTkLabel(**config_base, text=texto, corner_radius=5, width=100).grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        ctk.CTkLabel(**config_base, text="Digite o ID:  ", corner_radius=5).grid(row=1, column=0, padx=20, pady=20)
        id_aluno = ctk.CTkEntry(**config_interativo, justify="center")
        id_aluno.grid(row=1, column=1, columnspan=2, padx=20, pady=20)

        ctk.CTkLabel(**config_base, text="Nome do Aluno: ", corner_radius=5).grid(row=2, column=0, padx=20, pady=20)
        CaixaDeTexto = ctk.CTkEntry(**config_interativo, justify="center")
        CaixaDeTexto.grid(row=2, column=1, columnspan=2, padx=20, pady=20)

        ctk.CTkLabel(**config_base, text="Nota AV: ", corner_radius=5).grid(row=3, column=0, padx=20, pady=20)
        notaDaAV = ctk.CTkEntry(**config_interativo, justify="center")
        notaDaAV.grid(row=3, column=1, columnspan=2, padx=20, pady=20)

        ctk.CTkLabel(**config_base, text="Nota AVS:", corner_radius=5).grid(row=4, column=0, padx=20, pady=20)
        notaDaAVS = ctk.CTkEntry(**config_interativo, justify="center")
        notaDaAVS.grid(row=4, column=1, columnspan=2, padx=20, pady=20)

        ctk.CTkButton(
            **botoes,
            text="Enviar",
            command=lambda: funções.MudarNaLista(
                posicao=id_aluno.get(),
                nome=CaixaDeTexto.get(),
                av=notaDaAV.get(),
                avs=notaDaAVS.get(),
                janela=JanelaSub,
            ),
        ).grid(row=5, column=0, columnspan=3, sticky="ew", padx=20, pady=20)

    def midia(self, atributo, tipo, video=None):
        if tipo == ".mp3":
            texto = atributo.cget("text")
            if texto == "PLAY ▶":
                atributo.configure(text="|◁ II ▷| STOP ⏹", fg_color="red")
                try:
                    pygame.mixer.music.play(-1)
                except Exception:
                    pass
            elif texto == "|◁ II ▷| PLAY ▶":
                atributo.configure(text="|◁ II ▷| STOP ⏹", fg_color="red")
                try:
                    pygame.mixer.music.unpause()
                except Exception:
                    pass
            elif texto == "|◁ II ▷| STOP ⏹":
                atributo.configure(text="|◁ II ▷| PLAY ▶", fg_color="green")
                try:
                    pygame.mixer.music.pause()
                except Exception:
                    pass
        elif tipo == ".mp4":
            if video:
                video.play()


# -------- Funções antigas (mantidas) --------
_app_instance: App | None = None


def ChamarJanela():
    global _app_instance
    _app_instance = App()
    _app_instance.mainloop()


def CriarSubJanela(imagem, titulo):
    # compat: cria uma janela usando a instância atual
    if _app_instance is None:
        raise RuntimeError("App não iniciado. Chame ChamarJanela() primeiro.")
    return _app_instance.criar_subjanela(imagem, titulo)


def Adicionar():
    if _app_instance is None:
        raise RuntimeError("App não iniciado. Chame ChamarJanela() primeiro.")
    _app_instance.adicionar()


def Mostrar():
    if _app_instance is None:
        raise RuntimeError("App não iniciado. Chame ChamarJanela() primeiro.")
    _app_instance.mostrar()


def Apagar():
    if _app_instance is None:
        raise RuntimeError("App não iniciado. Chame ChamarJanela() primeiro.")
    _app_instance.apagar()


def Explicacao():
    if _app_instance is None:
        raise RuntimeError("App não iniciado. Chame ChamarJanela() primeiro.")
    _app_instance.explicacao()


def Consultar():
    if _app_instance is None:
        raise RuntimeError("App não iniciado. Chame ChamarJanela() primeiro.")
    _app_instance.consultar()


def Alterar():
    if _app_instance is None:
        raise RuntimeError("App não iniciado. Chame ChamarJanela() primeiro.")
    _app_instance.alterar()


def Midia(atributo="Quem Eu vou mexer", tipo="tipo do arquivo que eu vou mexer", video=None):
    if _app_instance is None:
        raise RuntimeError("App não iniciado. Chame ChamarJanela() primeiro.")
    _app_instance.midia(atributo=atributo, tipo=tipo, video=video)


if __name__ == "__main__":
    ChamarJanela()
    funções.GerarRelatorio(tipo=".py")