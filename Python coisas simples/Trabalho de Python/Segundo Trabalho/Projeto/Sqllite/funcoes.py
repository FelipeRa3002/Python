import  banco
from tkinter import messagebox

# Valida se a nota inserida é um número e se está dentro dos limites (0-1 para simulados, 0-10 para provas)
def verficarnota(x,y):
    try:
        x = float(x)
        controle = False
        if y <=2:
            controle = True if x>=0 and x<=1 else False
        elif y >=3:
            controle = True if x>=0 and x<=10 else False
        if controle:
            return round(x,1)
        else:
            return "Limite"
    except:
        return None

# Classe que encapsula os dados do aluno e as regras de negócio para cálculo de média e situação
class Aluno: 
    def __init__(self,nome,simulado1,simulado2,av,avs):
            self.nome = nome
            self.simulado1 = simulado1
            self.simulado2 = simulado2
            self.av = av
            self.avs = avs
            # Regra: Nota Final é Simulado 1 + Simulado 2 + a maior nota entre AV e AVS
            self.notafinal = self.simulado1 + self.simulado2 + max(self.av,self.avs)
            # Garante que a nota máxima não ultrapasse 10
            self.notafinal = 10 if self.notafinal>=10 else self.notafinal
            self.situacao = "Aprovado" if self.notafinal>=6 else "Reprovado"

# Processa a adição de um aluno, validando todas as notas antes de instanciar o objeto Aluno e salvar
def adicionar(nome,simulado1,simulado2,av,avs,janela):
    criacao = True
    lista = {
        "simulado1": simulado1,
        "simulado2": simulado2,
        "av": av,
        "avs": avs
    }
    notas_okay = {}
    x=1
    # Loop para validar individualmente cada nota enviada pela interface
    for i , valor in lista.items():
        novanotas = verficarnota(valor,x)
        if novanotas is None:
            criacao = False
            messagebox.showwarning("Erro!!!!","Você digitou algum diferente que número", parent=janela)
            break
        elif novanotas == "Limite":
            criacao = False
            messagebox.showinfo("Aviso",f"Você digitou um valor que é menor que zero ou superior ao limite da nota máxima {1 if x <= 2 else 10}\nFoi no campo {i}",parent=janela)
            break
        else:
            notas_okay[i] = novanotas
        x+=1
    if criacao:
        aluno = Aluno(nome, notas_okay["simulado1"], notas_okay["simulado2"], notas_okay["av"], notas_okay["avs"])
        banco.adicionar(Dados=aluno)
        janela.destroy()

def mostrar():
    return banco.listar()
    
# Filtra quais campos o usuário deseja alterar e encaminha para a atualização no banco
def alterar(quem,nome,simulado1,simulado2,av,avs,janela):
    opcoes = ["nome", "simulado 1", "simulado 2", "av", "avs"]
    entrada = [nome, simulado1, simulado2, av, avs]
    
    campos = []
    valornovo = []
    
    # Varre o que foi digitado e filtra o que não estiver vazio
    for idx, valor in enumerate(entrada):
        if valor.strip() != "":
            campos.append(opcoes[idx])
            valornovo.append(valor.strip())
            
    # Se o usuário digitou algo, chama a função do banco que criamos acima
    if campos:
        banco.mudar(quem=quem, campo=campos, novoValor=valornovo)
        
    # Fecha a subjanela após alterar
    janela.destroy()

# Gerencia a exclusão do aluno por ID, fechando as janelas de interface relacionadas
def apagar(janela,idAluno):
    try:
        idAluno = int(idAluno)
        banco.apagar(quem=idAluno)
        janela[0].destroy()
        janela[1].destroy()
        return "Sucesso"
    except:
        return "Erro ao apagar aluno"
    
# Intermedia a consulta entre a interface e o banco de dados
def consultar(janela_busca, entrada,acao):
    nome= "padrão"
    situacao = "padrão"
    texto = banco.consultar(acao=acao,nome=entrada,situacao=situacao)
    janela_busca.destroy()
    return texto
    
    
