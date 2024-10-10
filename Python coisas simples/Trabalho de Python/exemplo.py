import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import teste
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
        
        categoria=("Roupa","Eletrônicos","Alimentos","Tudo")
        self.var = tk.StringVar(value=categoria[3])
        c = 0
        for i in categoria:
            self.r = tk.Radiobutton(master,text=i,variable=self.var,value=i)
            self.r.grid(row=2,column=c,pady=10)
            c+=1

        self.cadastrar_button = tk.Button(master, text="Cadastrar Produto", command=self.cadastrar_produto, width=20, height=2)
        self.cadastrar_button.grid(row=3, column=2, pady=10, padx=5)

        self.visualizar_button = tk.Button(master, text="Visualizar Produtos", command=self.visualizar_produtos, width=20, height=2)
        self.visualizar_button.grid(row=3, column=0, columnspan=2, pady=10, padx=5) 
        self.eletrônicos= 6
        self.alimentos = 11
        produtosrou= [
    {'Produto': 'Camiseta', 'Descricao': 'Camiseta de algodão', 'Valor': '49,90'},
    {'Produto': 'Calça Jeans', 'Descricao': 'Calça jeans masculina', 'Valor': '129,90'},
    {'Produto': 'Jaqueta', 'Descricao': 'Jaqueta de couro', 'Valor': '299,99'},
    {'Produto': 'Tênis', 'Descricao': 'Tênis esportivo', 'Valor': '199,90'},
    {'Produto': 'Vestido', 'Descricao': 'Vestido de verão', 'Valor': '89,90'}
] 
        produtosele = [
    {'Produto': 'Smartphone', 'Descricao': 'Smartphone de última geração', 'Valor': '2999,99'},
    {'Produto': 'Notebook', 'Descricao': 'Notebook com 16GB de RAM e 512GB SSD', 'Valor': '4999,90'},
    {'Produto': 'Fone de Ouvido', 'Descricao': 'Fone de ouvido sem fio com cancelamento de ruído', 'Valor': '799,99'},
    {'Produto': 'Televisão', 'Descricao': 'Smart TV 4K de 55 polegadas', 'Valor': '3499,90'},
    {'Produto': 'Câmera Digital', 'Descricao': 'Câmera digital com lente de 24MP', 'Valor': '1999,99'}
]
        produtosali = [
    {'Produto': 'Chocolate', 'Descricao': 'Chocolate ao leite', 'Valor': '5,50'},
    {'Produto': 'Café', 'Descricao': 'Pacote de café moído 500g', 'Valor': '15,90'},
    {'Produto': 'Arroz', 'Descricao': 'Pacote de arroz 1kg', 'Valor': '4,99'},
    {'Produto': 'Feijão', 'Descricao': 'Pacote de feijão 1kg', 'Valor': '6,99'},
    {'Produto': 'Leite', 'Descricao': 'Caixa de leite 1L', 'Valor': '3,49'}
]
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
        categoria = self.var.get()
        if produto and preco and descricao and categoria and categoria !="Tudo" :
            valor = preco
            descricao = {'Produto': produto, 'Descricao': descricao, 'Valor': valor}
            self.produto_entry.delete(0, tk.END)
            self.preco_entry.delete(0, tk.END)
            self.descricao_entry.delete(0, tk.END)
            if categoria == "Roupa":
                self.produtos.insert(self.eletrônicos -1,descricao)
                self.eletrônicos+=1
                self.alimentos+=1
            elif categoria == "Eletrônicos":
                self.produtos.insert(self.alimentos - 1,descricao)
                self.alimentos+=1
            elif categoria == "Alimentos":
                self.produtos.append(descricao)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        elif categoria=="Tudo":
            messagebox.showwarning("Notice", "Não é possível efetuar o cadastro com a opção Tudo selecionada")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def visualizar_produtos(self):
        produtos_list = self.produtos
        o_que_mostra = self.var.get()
        if o_que_mostra == "Tudo":
            x = 1
            y = 1
            for i in produtos_list:
                troca = f"{i['Valor']}"
                i['Valor'] = troca.replace('.','').replace(',','.')
                preco = f"{float(i['Valor']):_.2f}"
                i['Valor'] = preco.replace('.',',').replace('_','.')
                if x == 1:
                    x = f"Roupas\n{y}- {i['Produto']}: \nR${i['Valor']}\nDescrição: {i['Descricao']}\n"
                elif y == self.eletrônicos:
                    x=x+f"\nEletrônicos\n{y}- {i['Produto']}: \nR${i['Valor']}\nDescrição: {i['Descricao']}\n"
                elif y == self.alimentos:
                    x=x+f"\nAlimentos\n{y}- {i['Produto']}: \nR${i['Valor']}\nDescrição: {i['Descricao']}\n"
                else:
                    x = x + f"{y}- {i['Produto']}: \nR${i['Valor']}\nDescrição: {i['Descricao']}\n"
                y+=1
            messagebox.showinfo("Produtos Cadastrados", x)
        elif o_que_mostra == "Eletrônicos":
            y = 1
            texto = "Eletrônicos\n"
            for i in range(self.eletrônicos-1,self.alimentos-1):
                x = produtos_list[i]
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
            for i in range(0,self.eletrônicos-1):
                x = produtos_list[i]
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
            for i in range(self.alimentos - 1 , len(produtos_list)):
                x = produtos_list[i]
                troca = f"{x['Valor']}"
                x['Valor'] = troca.replace('.','').replace(',','.')
                preco = f"{float(x['Valor']):_.2f}"
                x['Valor'] = preco.replace('.',',').replace('_','.')
                texto = texto + f"{y}- {x['Produto']}: \nR${x['Valor']}\nDescrição: {x['Descricao']}\n"
                y+=1
            messagebox.showinfo("Produtos Cadastrados", texto)
                
        else:
            messagebox.showinfo("Produtos Cadastrados", "Nenhum produto cadastrado.")

if __name__ == "__main__":
    resultado = messagebox.askyesnocancel("Confirmation", "Você deseja usar uma interface gráfica? ")
    if resultado is True:
      root = tk.Tk()
      root.geometry("800x800")
      # Definir o tamanho máximo e mínimo da janela
      root.minsize(800, 800)
      root.maxsize(800, 800)
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
      url = 'https://www.mundodeportivo.com/alfabeta/hero/2022/11/Makima.jpg?width=1200'
      response = requests.get(url)
      img_data = response.content
      img = Image.open(BytesIO(img_data))
      img = img.resize((800,800), Image.LANCZOS)
      photo = ImageTk.PhotoImage(img)
      # Criar um label e adicionar a imagem de fundo
      background_label = tk.Label(root, image=photo)
      background_label.place(relwidth=1, relheight=1)
      loja = LojaShopping(root)
      root.mainloop()
    elif resultado is False:
        teste.menu()

""""
precisa dar pip install requests e pip install pillow e depois dar pip uninstall requests e pip uninstall pillow
"""