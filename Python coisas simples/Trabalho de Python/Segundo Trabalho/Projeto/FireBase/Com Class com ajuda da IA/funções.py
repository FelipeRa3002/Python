from tkinter import messagebox
from os import system, getlogin
from datetime import datetime

import bancodedados

try:
    import dados
except Exception:
    class dados:
        ListarcomNome = []


ZeroTwo = "Não né filhão"


class Turma:
    def __init__(self, storage_module):
        self.storage = storage_module  # dados

    @property
    def lista(self):
        return self.storage.ListarcomNome

    def mostrar_alunos(self) -> str:
        texto = ""
        x = 1
        for i in self.lista:
            texto += f"{x} - O Aluno {i['nome']} | Maior Nota: {i['notafinal']:.1f} | {i['situacao']}\n"
            x += 1
        return texto

    def listar_nomes(self) -> str:
        return "\n".join([f"{x+1} - {i['nome']}" for x, i in enumerate(self.lista)])

    def adicionar(self, nome: str, av: str, avs: str):
        avf = float(str(av).replace(",", "."))
        avsf = float(str(avs).replace(",", "."))

        if not (0 <= avf <= 10) or not (0 <= avsf <= 10):
            raise ValueError("nota fora do intervalo")

        maior = max(avf, avsf)
        situacao = "Aprovado" if maior >= 6 else "Reprovado"

        self.lista.append({"nome": nome, "notafinal": maior, "situacao": situacao})
        bancodedados.Criar(nome=nome, notafinal=maior, situacao=situacao)

    def apagar_por_id(self, id_str: str):
        idx = int(id_str) - 1
        if not (0 <= idx < len(self.lista)):
            raise IndexError("ID inválido")

        nome = self.lista[idx]["nome"]
        self.lista.pop(idx)
        bancodedados.Apagar(nome=nome)

    def consultar(self, nome: str) -> list[tuple[str, str]]:
        achados = []
        for i in self.lista:
            if nome.strip().upper() == i["nome"].strip().upper():
                achados.append((i["nome"], i["situacao"]))
        return achados

    def mudar(self, posicao: str, nome: str, av: str, avs: str):
        pos = int(posicao) - 1
        if not (0 <= pos < len(self.lista)):
            raise IndexError("ID inválido")

        antigo_nome = self.lista[pos]["nome"]
        maior_atual = float(self.lista[pos]["notafinal"])

        Mudanca = [self.lista[pos]["nome"], self.lista[pos]["notafinal"], self.lista[pos]["situacao"]]
        MudouNome = False
        MudouNota = False

        # nome
        if nome != "":
            self.lista[pos]["nome"] = nome
            Mudanca[0] = nome
            MudouNome = True

        # notas: se algum campo veio preenchido, recalcula
        notas = []
        if av != "":
            notas.append(float(str(av).replace(",", ".")))
        if avs != "":
            notas.append(float(str(avs).replace(",", ".")))

        if notas:
            for n in notas:
                if n < 0 or n > 10:
                    raise ValueError("nota fora do intervalo")

            nova = max([maior_atual] + notas)
            if nova != maior_atual:
                self.lista[pos]["notafinal"] = float(f"{nova:.1f}")
                self.lista[pos]["situacao"] = "Aprovado" if nova >= 6 else "Reprovado"
                Mudanca[1] = self.lista[pos]["notafinal"]
                Mudanca[2] = self.lista[pos]["situacao"]
                MudouNota = True

        if MudouNome and MudouNota:
            contador = 4
            campos = ["nome", "notafinal", "situacao"]
        elif MudouNome:
            contador = 1
            campos = ["nome"]
        elif MudouNota:
            contador = 3
            campos = ["notafinal", "situacao"]
        else:
            return  # nada mudou

        bancodedados.Alterar(nome=antigo_nome, campo=[contador, Mudanca, campos])

    def gerar_relatorio(self, tipo: str):
        user = getlogin()
        data = f"{datetime.now().strftime('%d/%m/%Y')}"

        if tipo == ".txt":
            with open("Relatório.txt", "w+", encoding="utf-8") as f:
                contador = 1
                texto = f"Relatório da turma feito no dia {data} , pelo {user}\n"
                soma = 0

                for i in self.lista:
                    soma += i["notafinal"]
                    texto += (
                        f"{contador} - Nome: {i['nome']} - Sua maior nota: {i['notafinal']:.1f} - {i['situacao']}\n"
                    )
                    contador += 1

                media = (soma / len(self.lista)) if self.lista else 0
                texto += (
                    f"A média da turma no geral foi de {media:.1f} , turma "
                    f"{'APROVADO' if media >= 6 else 'REPROVADO'}\n"
                )
                f.write(texto)

        elif tipo == ".py":
            with open("dados.py", "w+", encoding="utf-8") as f:
                soma = 0
                itens = []
                for i in self.lista:
                    soma += i["notafinal"]
                    itens.append(
                        f"{{'nome': '{i['nome']}', 'notafinal': {i['notafinal']}, 'situacao': '{i['situacao']}'}}"
                    )
                f.write(
                    f"# Foi modificado no dia {data} às {datetime.now().strftime('%H:%M:%S')} pelo {user}\n"
                    f"ListarcomNome = [{', '.join(itens)}]\n"
                    f"mediadaTurmaDefinitiva = {soma:.1f}"
                )


_turma = Turma(dados)


# --------- Funções antigas (NÃO removidas) ----------
def MostrarAlunos():
    return _turma.mostrar_alunos()


def AdicionarNaLista(nome, av, avs, janela="n/a"):
    try:
        _turma.adicionar(nome, av, avs)
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        try:
            janela.destroy()
        except Exception:
            pass
    except ValueError:
        messagebox.showinfo(
            "Sério",
            "Digite notas válidas (0 a 10). Use vírgula ou ponto (ex: 7,5 ou 7.5).",
        )


def ListarNomes():
    return _turma.listar_nomes()


def ApagarNaLista(id, janela="n/a"):
    try:
        _turma.apagar_por_id(id)
        messagebox.showinfo("Sucesso", "Apagado com sucesso!")
        try:
            janela.destroy()
        except Exception:
            pass
    except ValueError:
        messagebox.showerror("Erro", "Use um número inteiro")
    except IndexError:
        messagebox.showwarning("Aviso", "ID não encontrado")


def AbrirNavegador(url="www.gooogle.com"):
    system(f"start {url}")


def ConsultarNaLista(nome="n/a", janela="n/a"):
    achados = _turma.consultar(nome)
    if achados:
        texto = ""
        for x, (n, s) in enumerate(achados, start=1):
            texto += f"{x} ---- {n}  ---- {s}\n"
        messagebox.showinfo("Resultados da Consulta", texto)
        try:
            janela.destroy()
        except Exception:
            pass
    else:
        messagebox.showerror("Não tem", "Não foi achado ninguém")


def MudarNaLista(posicao=0, av=0.1, avs=0.1, nome="Fulano", janela="n/a"):
    try:
        _turma.mudar(str(posicao), str(nome), str(av), str(avs))
        messagebox.showinfo("Sucesso", "Alterado com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "Notas devem ser de 0 a 10")
    except IndexError:
        messagebox.showwarning("Aviso", "ID não encontrado")
    finally:
        try:
            janela.destroy()
        except Exception:
            pass


def GerarRelatorio(tipo=".html"):
    _turma.gerar_relatorio(tipo)


def BancodeDados(acao="nenhuma", nome="fulano", notafinal=float(1), situacao="Seila", campo="n/a"):
    if acao == "Criar":
        bancodedados.Criar(nome=nome, notafinal=notafinal, situacao=situacao)
    if acao == "Apagar":
        bancodedados.Apagar(nome=nome)
    if acao == "Alterar":
        bancodedados.Alterar(nome=nome, campo=campo)