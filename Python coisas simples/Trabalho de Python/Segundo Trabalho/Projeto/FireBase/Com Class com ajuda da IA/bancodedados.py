import json
import requests
from tkinter import messagebox

from aluno import Aluno

url = "https://makima-deusa-default-rtdb.firebaseio.com/"


class RepositorioFirebase:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/") + "/"

    def criar(self, aluno: Aluno) -> int:
        r = requests.post(f"{self.base_url}Alunos/.json", data=json.dumps(aluno.to_dict()))
        return int(r.status_code)

    def listar(self) -> list[Aluno]:
        r = requests.get(f"{self.base_url}/.json")
        data = r.json() or {}
        alunos = data.get("Alunos") or {}
        out: list[Aluno] = []
        for _id, payload in alunos.items():
            if payload:
                out.append(Aluno.from_dict(payload))
        return out

    def apagar_por_nome(self, nome: str) -> int:
        r = requests.get(f"{self.base_url}/.json")
        data = r.json() or {}
        alunos = data.get("Alunos") or {}

        for _id, payload in alunos.items():
            if str(payload.get("nome", "")).strip().upper() == str(nome).strip().upper():
                d = requests.delete(f"{self.base_url}Alunos/{_id}/.json")
                return int(d.status_code)
        return 404

    # campo = [contador, Mudanca, campos]
    def alterar_por_nome(self, nome: str, campo) -> int:
        r = requests.get(f"{self.base_url}/.json")
        data = r.json() or {}
        alunos = data.get("Alunos") or {}

        for _id, payload in alunos.items():
            if str(payload.get("nome", "")).strip().upper() == str(nome).strip().upper():
                status = 0

                if campo[0] == 1:
                    mudar = {campo[2][0]: campo[1][0]}
                    status = requests.patch(
                        f"{self.base_url}Alunos/{_id}/.json", data=json.dumps(mudar)
                    ).status_code

                elif campo[0] == 3:
                    y = 1
                    for x in campo[2]:
                        mudar = {x: campo[1][y]}
                        status = requests.patch(
                            f"{self.base_url}Alunos/{_id}/.json", data=json.dumps(mudar)
                        ).status_code
                        y += 1

                elif campo[0] == 4:
                    y = 0
                    for x in campo[2]:
                        mudar = {x: campo[1][y]}
                        status = requests.patch(
                            f"{self.base_url}Alunos/{_id}/.json", data=json.dumps(mudar)
                        ).status_code
                        y += 1

                return int(status)

        return 404


_repo = RepositorioFirebase(url)


# --------- Funções antigas (NÃO removidas) ----------
def Criar(nome="fulano", notafinal=float(1), situacao="situacao"):
    status = _repo.criar(Aluno(nome=nome, notafinal=notafinal, situacao=situacao))
    if status in (200, 201):
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso, banco de dados!")
    else:
        messagebox.showwarning("Aviso", f"Verificar o banco de dados (status {status})")


def Apagar(nome="nome"):
    status = _repo.apagar_por_nome(nome)
    if status == 200:
        messagebox.showinfo("Sucesso", "Aluno apagado com sucesso, banco de dados!")
    elif status == 404:
        messagebox.showwarning("Aviso", "Aluno não encontrado no banco de dados")
    else:
        messagebox.showwarning("Aviso", f"Verificar o banco de dados (status {status})")


def Alterar(nome="nome", campo=[1, "Valor Novo", "campo"]):
    status = _repo.alterar_por_nome(nome, campo)
    if status in (200, 201):
        messagebox.showinfo("Sucesso", "Aluno teve os dados alterados com sucesso, banco de dados!")
    elif status == 404:
        messagebox.showwarning("Aviso", "Aluno não encontrado no banco de dados")
    else:
        messagebox.showwarning("Aviso", "Verificar o banco de dados")


def LigacaoComDadosSalvos():
    # Mantém o retorno como lista de dicts pra não quebrar seu resto do código
    return [a.to_dict() for a in _repo.listar()]


def teste():
    Dados = LigacaoComDadosSalvos()
    return Dados