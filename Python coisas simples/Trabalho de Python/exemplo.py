import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import teste
def chamarJanela():
      global root
      root = tk.Tk()
      root.geometry("800x600")
      # Definir o tamanho máximo e mínimo da janela
      root.minsize(800, 600)
      root.maxsize(800, 600)
      url = 'https://th.bing.com/th/id/OIP.n_KuHxQWUNrI57iYK1ffCgHaHa?w=1024&h=1024&rs=1&pid=ImgDetMain'
      # Baixar a imagem
      response = requests.get(url)
      img_data = response.content
      # Carregar a imagem
      img = Image.open(BytesIO(img_data))
      img = img.resize((400, 100), Image.LANCZOS) 
      photo = ImageTk.PhotoImage(img)
      # Definir o ícone
      root.iconphoto(False, photo)
      url = 'https://www.mundodeportivo.com/alfabeta/hero/2022/11/Makima.jpg?width=1200'
      response = requests.get(url)
      img_data = response.content
      img = Image.open(BytesIO(img_data))
      img = img.resize((800,600), Image.LANCZOS)
      photo = ImageTk.PhotoImage(img)
      # Criar um label e adicionar a imagem de fundo
      background_label = tk.Label(root, image=photo)
      background_label.place(relwidth=1, relheight=1)
      loja = LojaShopping(root)
      root.mainloop()
class LojaShopping:
    def __init__(self, master):
        self.master = master
        master.title("Loja de Shopping")
        self.produtos = []

        self.label = tk.Label(master, text="Produto", width=20,bg="black",fg="white")
        self.label.grid(row=0, column=0)

        self.label2 = tk.Label(master, text="Preço", width=20,bg="black",fg="white")
        self.label2.grid(row=0, column=1,padx=100)
        self.label3 = tk.Label(master, text="Descrição", width=20,bg="black",fg="white")
        self.label3.grid(row=0, column=2)

        self.produto_entry = tk.Entry(master,width=30,fg="red",highlightbackground="red", highlightcolor="black", highlightthickness=4)
        self.produto_entry.grid(row=1, column=0,pady=10)

        self.preco_entry = tk.Entry(master, width=30,fg="green",highlightbackground="gold", highlightcolor="khaki", highlightthickness=4)
        self.preco_entry.grid(row=1, column=1,pady=10)

        self.descricao_entry = tk.Entry(master, width=30,fg="blue",highlightbackground="darkturquoise", highlightcolor="darkorange", highlightthickness=4)
        self.descricao_entry.grid(row=1, column=2,pady=10)
        
        self.categoria=("Roupa","Eletrônicos","Alimentos","Tudo")
        self.var = tk.StringVar(value=self.categoria[3])
        c = 0
        for i in self.categoria:
            self.r = tk.Radiobutton(master,text=i,variable=self.var,value=i)
            self.r.grid(row=2,column=c,pady=10)
            c+=1

        self.cadastrar_button = tk.Button(master, text="Cadastrar Produto", command=self.cadastrar_produto, width=20, height=2)
        self.cadastrar_button.grid(row=3, column=2, pady=10, padx=5)

        self.visualizar_button = tk.Button(master, text="Visualizar Produtos", command=self.visualizar_produtos, width=20, height=2)
        self.visualizar_button.grid(row=3, column=0, columnspan=2, pady=10, padx=5)
        self.Mudar_button = tk.Button(master, text="Mudar para sem interface gráfica", command=self.Fechar, width=30, height=2)
        self.Mudar_button.grid(row=4, column=0, columnspan=4, pady=10, padx=5) 
        self.Apagar_button = tk.Button(master, text="Apagar produto", command=self.Apagar, width=30, height=2)
        self.Apagar_button.grid(row=4, column=2, columnspan=4, pady=10, padx=5) 
        produtosrou = [
    {'Produto': 'Camiseta', 'Descricao': 'Camiseta de algodão', 'Valor': '49,90', 'Categoria': "Roupa"},
    {'Produto': 'Calça Jeans', 'Descricao': 'Calça jeans masculina', 'Valor': '129,90', 'Categoria': "Roupa"},
    {'Produto': 'Jaqueta', 'Descricao': 'Jaqueta de couro', 'Valor': '299,99', 'Categoria': "Roupa"},
    {'Produto': 'Tênis', 'Descricao': 'Tênis esportivo', 'Valor': '199,90', 'Categoria': "Roupa"},
    {'Produto': 'Vestido', 'Descricao': 'Vestido de verão', 'Valor': '89,90', 'Categoria': "Roupa"},
    {'Produto': 'Boné', 'Descricao': 'Boné de aba reta', 'Valor': '39,90', 'Categoria': "Roupa"},
    {'Produto': 'Meia', 'Descricao': 'Meia de algodão', 'Valor': '9,90', 'Categoria': "Roupa"},
    {'Produto': 'Cinto', 'Descricao': 'Cinto de couro', 'Valor': '69,90', 'Categoria': "Roupa"},
    {'Produto': 'Saia', 'Descricao': 'Saia plissada', 'Valor': '79,90', 'Categoria': "Roupa"},
    {'Produto': 'Blusa', 'Descricao': 'Blusa de seda', 'Valor': '149,90', 'Categoria': "Roupa"}
]

        produtosele = [
    {'Produto': 'Smartphone', 'Descricao': 'Smartphone de última geração', 'Valor': '2999,99', 'Categoria': "Eletrônicos"},
    {'Produto': 'Notebook', 'Descricao': 'Notebook com 16GB de RAM e 512GB SSD', 'Valor': '4999,90', 'Categoria': "Eletrônicos"},
    {'Produto': 'Fone de Ouvido', 'Descricao': 'Fone de ouvido sem fio com cancelamento de ruído', 'Valor': '799,99', 'Categoria': "Eletrônicos"},
    {'Produto': 'Televisão', 'Descricao': 'Smart TV 4K de 55 polegadas', 'Valor': '3499,90', 'Categoria': "Eletrônicos"},
    {'Produto': 'Câmera Digital', 'Descricao': 'Câmera digital com lente de 24MP', 'Valor': '1999,99', 'Categoria': "Eletrônicos"},
    {'Produto': 'Tablet', 'Descricao': 'Tablet com tela de 10 polegadas', 'Valor': '1299,99', 'Categoria': "Eletrônicos"},
    {'Produto': 'Smartwatch', 'Descricao': 'Relógio inteligente com monitoramento cardíaco', 'Valor': '899,99', 'Categoria': "Eletrônicos"},
    {'Produto': 'Drone', 'Descricao': 'Drone com câmera 4K', 'Valor': '2499,90', 'Categoria': "Eletrônicos"},
    {'Produto': 'Caixa de Som', 'Descricao': 'Caixa de som Bluetooth', 'Valor': '499,99', 'Categoria': "Eletrônicos"},
    {'Produto': 'E-Reader', 'Descricao': 'Leitor de livros digitais', 'Valor': '599,99', 'Categoria': "Eletrônicos"}
]

        produtosali = [
        {'Produto': 'Chocolate', 'Descricao': 'Chocolate ao leite', 'Valor': '5,50', 'Categoria': "Alimentos"},
        {'Produto': 'Café', 'Descricao': 'Pacote de café moído 500g', 'Valor': '15,90', 'Categoria': "Alimentos"},
        {'Produto': 'Arroz', 'Descricao': 'Pacote de arroz 1kg', 'Valor': '4,99', 'Categoria': "Alimentos"},
        {'Produto': 'Feijão', 'Descricao': 'Pacote de feijão 1kg', 'Valor': '6,99', 'Categoria': "Alimentos"},
        {'Produto': 'Leite', 'Descricao': 'Caixa de leite 1L', 'Valor': '3,49', 'Categoria': "Alimentos"},
        {'Produto': 'Macarrão', 'Descricao': 'Pacote de macarrão 500g', 'Valor': '3,99', 'Categoria': "Alimentos"},
        {'Produto': 'Azeite', 'Descricao': 'Garrafa de azeite 500ml', 'Valor': '19,90', 'Categoria': "Alimentos"},
        {'Produto': 'Biscoito', 'Descricao': 'Pacote de biscoito recheado', 'Valor': '2,50', 'Categoria': "Alimentos"},
        {'Produto': 'Suco', 'Descricao': 'Caixa de suco 1L', 'Valor': '4,99', 'Categoria': "Alimentos"},
        {'Produto': 'Pão', 'Descricao': 'Pacote de pão de forma', 'Valor': '6,99', 'Categoria': "Alimentos"}
]
        for i in produtosrou:  
             self.produtos.append(i)
        for i in produtosele:
            self.produtos.append(i)
        for i in produtosali:
            self.produtos.append(i)
    def Fechar(self):
        root.destroy() 
        teste.menu()  
    def cadastrar_produto(self):
        produto = self.produto_entry.get()
        preco = self.preco_entry.get()
        descricao = self.descricao_entry.get()
        categoria = self.var.get()
        if produto and preco and descricao and categoria and categoria !="Tudo" :
            valor = preco
            descricao = {'Produto': produto, 'Descricao': descricao, 'Valor': valor, 'Categoria': categoria}
            self.produto_entry.delete(0, tk.END)
            self.preco_entry.delete(0, tk.END)
            self.descricao_entry.delete(0, tk.END)
            y=0
            for i in self.produtos:
                if i['Categoria'] == categoria:
                    self.produtos.insert(y,descricao)
                    break
                y+=1
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        elif categoria=="Tudo":
            messagebox.showwarning("Notice", "Não é possível efetuar o cadastro com a opção Tudo selecionada")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def visualizar_produtos(self):
        produtos_list = self.produtos
        o_que_mostra = self.var.get()
        if o_que_mostra == "Tudo":
            self.eletrônicos,self.alimentos=0,0
            x = 1
            y = 1
            for i in produtos_list:
                troca = f"{i['Valor']}"
                i['Valor'] = troca.replace('.','').replace(',','.')
                preco = f"{float(i['Valor']):_.2f}"
                i['Valor'] = preco.replace('.',',').replace('_','.')
                if x == 1:
                    x = f"Roupas\n{y}- {i['Produto']}: \nR${i['Valor']}\nDescrição: {i['Descricao']}\n"
                elif self.eletrônicos == 0 and i['Categoria'] == "Eletrônicos":
                    x=x+f"\nEletrônicos\n{y}- {i['Produto']}: \nR${i['Valor']}\nDescrição: {i['Descricao']}\n"
                    self.eletrônicos =1
                elif  self.alimentos == 0 and i['Categoria'] == "Alimentos":
                    x=x+f"\nAlimentos\n{y}- {i['Produto']}: \nR${i['Valor']}\nDescrição: {i['Descricao']}\n"
                    self.alimentos =1
                else:
                    x = x + f"{y}- {i['Produto']}: \nR${i['Valor']}\nDescrição: {i['Descricao']}\n"
                y+=1
            messagebox.showinfo("Produtos Cadastrados", x)
        elif o_que_mostra == "Eletrônicos":
            y = 1
            texto = "Eletrônicos\n"
            for i in produtos_list:
                if i['Categoria'] == "Eletrônicos":
                    x = i
                    troca = f"{x['Valor']}"
                    x['Valor'] = troca.replace('.','').replace(',','.')
                    preco = f"{float(x['Valor']):_.2f}"
                    x['Valor'] = preco.replace('.',',').replace('_','.')
                    texto = texto + f"{y}- {x['Produto']}: \nR${x['Valor']}\nDescrição: {x['Descricao']}\n"
                    y+=1
            messagebox.showinfo("Produtos Cadastrados", texto)

        elif o_que_mostra == "Roupa":
            y = 1
            texto = "Roupas\n"
            for i in produtos_list:
                if i['Categoria'] == "Roupa":
                    x = i
                    troca = f"{x['Valor']}"
                    x['Valor'] = troca.replace('.','').replace(',','.')
                    preco = f"{float(x['Valor']):_.2f}"
                    x['Valor'] = preco.replace('.',',').replace('_','.')
                    texto = texto + f"{y}- {x['Produto']}: \nR${x['Valor']}\nDescrição: {x['Descricao']}\n"
                    y+=1
            messagebox.showinfo("Produtos Cadastrados", texto)
        
        elif o_que_mostra == "Alimentos":
            y = 1
            texto = "Alimentos\n"
            for i in produtos_list:
                if i['Categoria'] == "Alimentos":
                    x = i
                    troca = f"{x['Valor']}"
                    x['Valor'] = troca.replace('.','').replace(',','.')
                    preco = f"{float(x['Valor']):_.2f}"
                    x['Valor'] = preco.replace('.',',').replace('_','.')
                    texto = texto + f"{y}- {x['Produto']}: \nR${x['Valor']}\nDescrição: {x['Descricao']}\n"
                    y+=1
            messagebox.showinfo("Produtos Cadastrados", texto)
                
        else:
            messagebox.showinfo("Produtos Cadastrados", "Nenhum produto cadastrado.")
    
    def Apagar(self):
        trupa = ("label","label2","label3","produto_entry","preco_entry","descricao_entry","cadastrar_button","Mudar_button","visualizar_button","Apagar_button")
        for i in trupa:
           eval(f"self.{i}.destroy()")
           
        self.label = tk.Label(self.master, text="Número do produto que você deseja apagar", width=42,bg="black",fg="white")
        self.label.grid(row=0, column=0)
        self.entreyapagar = tk.Entry(self.master,width=4)
        self.entreyapagar.grid(row=1,column=0)
        self.botao = tk.Button(self.master,text="Apagar",command=self.ApagarProduto,width=30, height=2)
        self.botao.grid(row=3, column=0, columnspan=2, pady=10, padx=5)
        self.botao2 = tk.Button(self.master,text="Voltar",command=self.ChamarNovaJanela,width=30, height=2)
        self.botao2.grid(row=3, column=3, columnspan=2, pady=10, padx=5)
        posicao = 1
        texto = 1
        for i in self.produtos:
            if texto == 1:
                texto = f"{posicao} - {i['Produto']}"
            else:
                texto = texto + f"\n{posicao} - {i['Produto']}"
            posicao+=1
        self.label2 = tk.Label(self.master, text=texto, width=50,bg="black",fg="white")
        self.label2.grid(row=4, column=0)
    def ApagarProduto(self):
        Numero_que_apagar = self.entreyapagar.get()
        try:
            Numero_que_apagar = int(Numero_que_apagar)
            self.produtos.pop(Numero_que_apagar-1)
            self.ChamarNovaJanela()
        except ValueError:
            "self.Apagar()"
        except IndexError:
            "self.Apagar()"
        else:
            self.Apagar()
    def ChamarNovaJanela(self):
        lista = ("label","entreyapagar","botao","label2","botao2")
        for i in lista:
            eval(f"self.{i}.destroy()")
        self.label = tk.Label(self.master, text="Produto", width=20,bg="black",fg="white")
        self.label.grid(row=0, column=0)

        self.label2 = tk.Label(self.master, text="Preço", width=20,bg="black",fg="white")
        self.label2.grid(row=0, column=1,padx=100)
        self.label3 = tk.Label(self.master, text="Descrição", width=20,bg="black",fg="white")
        self.label3.grid(row=0, column=2)

        self.produto_entry = tk.Entry(self.master,width=30,fg="red",highlightbackground="red", highlightcolor="black", highlightthickness=4)
        self.produto_entry.grid(row=1, column=0,pady=10)

        self.preco_entry = tk.Entry(self.master, width=30,fg="green",highlightbackground="gold", highlightcolor="khaki", highlightthickness=4)
        self.preco_entry.grid(row=1, column=1,pady=10)

        self.descricao_entry = tk.Entry(self.master, width=30,fg="blue",highlightbackground="darkturquoise", highlightcolor="darkorange", highlightthickness=4)
        self.descricao_entry.grid(row=1, column=2,pady=10)
        self.cadastrar_button = tk.Button(self.master, text="Cadastrar Produto", command=self.cadastrar_produto, width=20, height=2)
        self.cadastrar_button.grid(row=3, column=2, pady=10, padx=5)

        self.visualizar_button = tk.Button(self.master, text="Visualizar Produtos", command=self.visualizar_produtos, width=20, height=2)
        self.visualizar_button.grid(row=3, column=0, columnspan=2, pady=10, padx=5)
        self.Mudar_button = tk.Button(self.master, text="Mudar para sem interface gráfica", command=self.Fechar, width=30, height=2)
        self.Mudar_button.grid(row=4, column=0, columnspan=4, pady=10, padx=5) 
        self.Apagar_button = tk.Button(self.master, text="Apagar produto", command=self.Apagar, width=30, height=2)
        self.Apagar_button.grid(row=4, column=2, columnspan=4, pady=10, padx=5) 

if __name__ == "__main__":
    resultado = messagebox.askyesnocancel("Confirmation", "Você deseja usar uma interface gráfica? ")
    if resultado is True:
      chamarJanela()
    elif resultado is False:
        teste.menu()

""""
precisa dar pip install requests e pip install pillow e depois dar pip uninstall requests e pip uninstall pillow
"""