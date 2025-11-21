import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class SessaoEstudo:
    def __init__(self, id, id_usuario, id_materia, topico_id, data, duracao, notas = None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_materia = id_materia
        self.topico_id = topico_id
        self.data = data
        self.duracao = duracao
        self.notas = notas

    def to_dict(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_materia": self.id_materia,
            "topico_id": self.topico_id,
            "data": self.data,
            "duracao": self.duracao,
            "notas": self.notas
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            id_usuario=data["id_usuario"],
            id_materia=data["id_materia"],
            topico_id=data["topico_id"],
            data=data["data"],
            duracao=data["duracao"],
            notas=data.get("notas")
        )
    
class SessaoEstudoModel:
    FILE_PATH = os.path.join(DATA_DIR, 'sessao_estudo.json')

    def __init__(self):
        self.sessoes = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [SessaoEstudo(**item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(
                [s.to_dict() for s in self.sessoes],
                f,
                indent=4,
                ensure_ascii=False
            )

    def get_all(self):
        return self.sessoes

    def get_by_id(self, sessao_id: int):
        return next((s for s in self.sessoes if s.id == sessao_id), None)

    def add_sessao(self, sessao: SessaoEstudo):
        self.sessoes.append(sessao)
        self._save()

    def update_sessao(self, updated_sessao: SessaoEstudo):
        for i, sessao in enumerate(self.sessoes):
            if sessao.id == updated_sessao.id:
                self.sessoes[i] = updated_sessao
                self._save()
                break

    def delete_sessao(self, sessao_id: int):
        self.sessoes = [s for s in self.sessoes if s.id != sessao_id]
        self._save()
