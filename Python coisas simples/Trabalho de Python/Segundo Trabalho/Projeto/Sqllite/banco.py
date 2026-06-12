import sqlite3
from tkinter import messagebox

# Inicia a conexão com o banco SQLite e garante que a estrutura de tabelas exista
def comecar():
    global conexao, cursor
    conexao = sqlite3.connect("Meu_banco.db")
    cursor = conexao.cursor()
    CriarTabela(conexao,cursor)

def CriarTabela(conexao,cursor):
    cursor.execute("""
CREATE TABLE IF NOT EXISTS TB_ALUNO (
    alu_id INTEGER PRIMARY KEY AUTOINCREMENT,
    alu_nome TEXT NOT NULL,
    alu_sim1 FLOAT DEFAULT 0.0,
    alu_sim2 FLOAT DEFAULT 0.0,
    alu_av FLOAT NOT NULL,
    alu_avs FLOAT DEFAULT 0.0,
    alu_situacao TEXT NOT NULL,
    alu_notafinal FLOAT NOT NULL
)
""")
    conexao.commit()
def adicionar(Dados):
        global cursor,conexao
        aluno = Dados
        # Simplificado para evitar erros de atributos inexistentes
        cursor.execute("INSERT INTO TB_ALUNO (alu_nome, alu_sim1, alu_sim2, alu_av, alu_avs, alu_situacao, alu_notafinal) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       (aluno.nome, aluno.simulado1, aluno.simulado2, aluno.av, aluno.avs, aluno.situacao, aluno.notafinal))

        conexao.commit()
     

def listar():
    global cursor
    cursor.execute("SELECT alu_id, alu_nome, alu_notafinal, alu_situacao FROM TB_ALUNO")
    mostrar = f"{'='*110}\n Todos Alunos \n{'='*110}\n"
    mostrar += "-"*100 + "\n"
    for linha in cursor.fetchall():
        espaco = " "
        mostrar += f"Matrícula: {linha[0]:05d}{espaco*3}|| Nome: {linha[1]:<30}{espaco*3}|| Nota: {linha[2]:<5.1f}{espaco*3}|| Situação: {linha[3]}\n"
    mostrar += "-"*100
    
    return mostrar

# Atualiza campos específicos e força o recálculo automático da média e situação
def mudar(quem, campo, novoValor):
    global cursor, conexao
    
    # 1. Atualizar individualmente cada campo fornecido pelo usuário
    for idx, nome_campo_usuario in enumerate(campo):
        # Mapeia o nome simplificado vindo da interface para a coluna real do banco
        mapa_colunas = {
            "nome": "alu_nome",
            "simulado 1": "alu_sim1",
            "simulado 2": "alu_sim2",
            "av": "alu_av",
            "avs": "alu_avs"
        }
        
        coluna_real = mapa_colunas.get(nome_campo_usuario)
        
        if coluna_real:
            valor = novoValor[idx]
            # Se for nota, converte para float, se for nome, mantém string
            if coluna_real != "alu_nome":
                valor = float(valor) if valor != "" else 0.0
            
            # Executa a atualização do campo digitado
            cursor.execute(f"UPDATE TB_ALUNO SET {coluna_real} = ? WHERE alu_id = ?", (valor, quem))
            conexao.commit()

    # 2. Recalcular a Nota Final e Situação com base nas regras de negócio
    # Buscamos os dados atualizados do aluno para garantir o cálculo correto
    cursor.execute("SELECT alu_sim1, alu_sim2, alu_av, alu_avs FROM TB_ALUNO WHERE alu_id = ?", (quem,))
    dados_aluno = cursor.fetchone()
    
    if dados_aluno:
        sim1 = float(dados_aluno[0] or 0)
        sim2 = float(dados_aluno[1] or 0)
        av = float(dados_aluno[2] or 0)
        avs = float(dados_aluno[3] or 0)
        
        # Regra da faculdade: A VS substitui a AV se for maior
        maior_prova = avs if avs > av else av
        
        # Cálculo da nota final (Simulado 1 + Simulado 2 + Maior Prova)
        notafinal = sim1 + sim2 + maior_prova
        if notafinal > 10.0:
            notafinal = 10.0
            
        # Define a situação do aluno
        situacao = "Aprovado" if notafinal >= 6.0 else "Reprovado"
        
        # Atualiza as colunas de resultado final no banco de dados
        cursor.execute(
            "UPDATE TB_ALUNO SET alu_notafinal = ?, alu_situacao = ? WHERE alu_id = ?",
            (notafinal, situacao, quem)
        )
        conexao.commit()

# Realiza a busca dos dados do aluno para confirmação visual antes de deletar
def apagar(quem):
    global cursor,conexao
    cursor.execute("SELECT alu_id, alu_nome FROM TB_ALUNO WHERE alu_id = ?",(quem,))
    for i in cursor.fetchall():
        informacoes = i
    # Formatação visual do ID para exibição com 5 dígitos (ex: 00001)
    if len(str(informacoes[0]))<2:
        texto = f"0000{str(informacoes[0])}"
    elif len(str(informacoes[0]))<3:
        texto = f"0000{str(informacoes[0])}"
    elif len(str(informacoes[0]))<4:
        texto = f"0000{str(informacoes[0])}"
    elif len(str(informacoes[0]))<5:
        texto = f"0000{str(informacoes[0])}"
    confirmacao = messagebox.askyesno("Confirmação de Apagamento", f"Você deseja confirmar a exclusão do Aluno {informacoes[1]}, com a Matrícula {texto}")
    if confirmacao:
        apagarDeFato(quem)
    else:
        messagebox.showinfo("Sucesso","Cancelado a exclusão do Aluno com sucesso")

def apagarDeFato(quem):
      cursor.execute("DELETE FROM TB_ALUNO WHERE alu_id = ?", (quem,))
      conexao.commit()
      messagebox.showinfo("Sucesso","Aluno apagado com sucesso")

# Realiza buscas filtradas: Ação 1 busca por nome (LIKE), Ação 2 busca por situação (Aprovado/Reprovado)
def consultar(acao,nome,situacao):
    global cursor
    Rias = "="*20
    resultado = ""
    if acao == 1:
        nome = f"%{nome}%"
        cursor.execute("select alu_id, alu_nome from tb_aluno where alu_nome like ?",(nome,))
        resultado =f"{Rias}\nAlunos achados\n{Rias}"
        resultado+="\n"+"-"*20+"\n"
        
        for Marin in cursor.fetchall():
            resultado+=f"Matrícula: {Marin[0]:05d} || Nome: {Marin[1]}\n"
        resultado+="-"*20
    
    elif acao == 2:
        cursor.execute("select alu_id, alu_nome, alu_notafinal, alu_situacao from tb_aluno where alu_situacao = ?",(nome,))
        resultado = f"{Rias}\nAlunos achados\n{Rias}\n"
        resultado += "-"*20 + "\n"
        for ZeroTwo in cursor.fetchall():
            resultado += f"Matrícula: {ZeroTwo[0]:05d} || Nome: {ZeroTwo[1]} || Nota: {ZeroTwo[2]} || Situação: {ZeroTwo[3]}\n"
        resultado += "-"*20
       
    return resultado
