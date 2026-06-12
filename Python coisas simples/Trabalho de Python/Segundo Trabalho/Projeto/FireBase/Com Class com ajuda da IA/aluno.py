from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    notafinal: float
    situacao: str

    def to_dict(self) -> dict:
        return {"nome": self.nome, "notafinal": float(self.notafinal), "situacao": self.situacao}

    @staticmethod
    def from_dict(d: dict) -> "Aluno":
        return Aluno(
            nome=str(d.get("nome", "")),
            notafinal=float(d.get("notafinal", 0)),
            situacao=str(d.get("situacao", "")),
        )