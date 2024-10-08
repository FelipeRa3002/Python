import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import teste
class LojaShopping:
    def __init__(self, master):
        self.primeiravez=1
        self.master = master
        master.title("Loja de Shopping")
        self.produtos = []

        self.label = tk.Label(master, text="Produto")
        self.label.grid(row=0, column=0)

        self.label2 = tk.Label(master, text="Preço")
        self.label2.grid(row=0, column=1)
        self.label3 = tk.Label(master, text="Descrição")
        self.label3.grid(row=0, column=2)
        self.produto_entry = tk.Entry(master)
        self.produto_entry.grid(row=1, column=0)

        self.preco_entry = tk.Entry(master)
        self.preco_entry.grid(row=1, column=1)

        self.descricao_entry = tk.Entry(master)
        self.descricao_entry.grid(row=1, column=2)

        self.cadastrar_button = tk.Button(master, text="Cadastrar Produto", command=self.cadastrar_produto, width=20, height=2)
        self.cadastrar_button.grid(row=2, column=2, pady=10, padx=5)

        self.visualizar_button = tk.Button(master, text="Visualizar Produtos", command=self.visualizar_produtos, width=20, height=2)
        self.visualizar_button.grid(row=2, column=0, columnspan=2, pady=10, padx=5) 
        produtosrou=[ {'Produto': 'Camiseta', 'Descricao': 'Camiseta de algodão', 'Valor': 49.90},
    {'Produto': 'Calça Jeans', 'Descricao': 'Calça jeans masculina', 'Valor': 129.90},
    {'Produto': 'Jaqueta', 'Descricao': 'Jaqueta de couro', 'Valor': 299.99},
    {'Produto': 'Tênis', 'Descricao': 'Tênis esportivo', 'Valor': 199.90},
    {'Produto': 'Vestido', 'Descricao': 'Vestido de verão', 'Valor': 89.90}]  
        produtosele = [
    {'Produto': 'Smartphone', 'Descricao': 'Smartphone de última geração', 'Valor': 2999.99},
    {'Produto': 'Notebook', 'Descricao': 'Notebook com 16GB de RAM e 512GB SSD', 'Valor': 4999.90},
    {'Produto': 'Fone de Ouvido', 'Descricao': 'Fone de ouvido sem fio com cancelamento de ruído', 'Valor': 799.99},
    {'Produto': 'Televisão', 'Descricao': 'Smart TV 4K de 55 polegadas', 'Valor': 3499.90},
    {'Produto': 'Câmera Digital', 'Descricao': 'Câmera digital com lente de 24MP', 'Valor': 1999.99}
]
        produtosali = [{'Produto': 'Chocolate', 'Descricao': 'Chocolate ao leite', 'Valor': 5.50},
    {'Produto': 'Café', 'Descricao': 'Pacote de café moído 500g', 'Valor': 15.90},
    {'Produto': 'Arroz', 'Descricao': 'Pacote de arroz 1kg', 'Valor': 4.99},
    {'Produto': 'Feijão', 'Descricao': 'Pacote de feijão 1kg', 'Valor': 6.99},
    {'Produto': 'Leite', 'Descricao': 'Caixa de leite 1L', 'Valor': 3.49}]
        for i in produtosrou:  
             self.produtos.append(i)
        for i in produtosele:
            self.produtos.append(i)
        for i in produtosali:
            self.produtos.append(i)
        
    def cadastrar_produto(self):
        produto = self.produto_entry.get()
        preco = self.preco_entry.get()
        descricao = self.descricao_entry.get()
        if produto and preco and descricao:
            valor = float(preco)
            descricao = {'Produto': produto, 'Descricao': descricao, 'Valor': valor}
            self.produtos.append(descricao)
            self.produto_entry.delete(0, tk.END)
            self.preco_entry.delete(0, tk.END)
            self.descricao_entry.delete(0, tk.END)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def visualizar_produtos(self):
        produtos_list = self.produtos
        if produtos_list:
            x = 1
            y = 1
            for i in produtos_list:
                if self.primeiravez >1:
                    troca = f"{i['Valor']}"
                    i['Valor'] = troca.replace('.','').replace(',','.')
                    preco = f"{float(i['Valor']):_.2f}"
                    i['Valor'] = preco.replace('.',',').replace('_','.')
                else:
                    preco = f"{float(i['Valor']):_.2f}"
                    i['Valor'] = preco.replace('.',',').replace('_','.')
                if x == 1:
                    x = f"Roupas\n{i['Produto']}: \nR${i['Valor']}\nDescrição: {i['Descricao']}\n"
                elif y == 6:
                    x=x+f"\nEletrônicos\n{i['Produto']}: \nR${i['Valor']}\nDescrição: {i['Descricao']}\n"
                elif y == 11:
                    x=x+f"\nAlimentos\n{i['Produto']}: \nR${i['Valor']}\nDescrição: {i['Descricao']}\n"
                else:
                    x = x + f"{i['Produto']}: \nR${i['Valor']}\nDescrição: {i['Descricao']}\n"
                y+=1
                self.primeiravez+=1
            messagebox.showinfo("Produtos Cadastrados", x)
        else:
            messagebox.showinfo("Produtos Cadastrados", "Nenhum produto cadastrado.")

if __name__ == "__main__":
    resultado = messagebox.askyesnocancel("Confirmation", "Você deseja usar uma interface gráfica? ")
    if resultado is True:
      root = tk.Tk()
      root.geometry("400x400")
      url = 'https://th.bing.com/th/id/OIP.n_KuHxQWUNrI57iYK1ffCgHaHa?w=1024&h=1024&rs=1&pid=ImgDetMain'
      # Baixar a imagem
      response = requests.get(url)
      img_data = response.content
      # Carregar a imagem
      img = Image.open(BytesIO(img_data))
      img = img.resize((100, 100), Image.LANCZOS) 
      photo = ImageTk.PhotoImage(img)
      # Definir o ícone
      root.iconphoto(False, photo)
      loja = LojaShopping(root)
      root.mainloop()
    elif resultado is False:
        teste.menu()

""""
precisa dar pip install requests e pip install pillow e depois dar pip uninstall requests e pip uninstall pillow
"""