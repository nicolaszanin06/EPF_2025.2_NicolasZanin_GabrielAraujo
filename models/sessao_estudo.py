import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class SessaoEstudo:
    def __init__(self, id, user_id, materia_id, topico_id, data, duracao_minutos, notas = None):
        self.id = id
        self.user_id = user_id
        self.materia_id = materia_id
        self.topico_id = topico_id
        self.data = data
        self.duracao_minutos = duracao_minutos
        self.notas = notas

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "materia_id": self.materia_id,
            "topico_id": self.topico_id,
            "data": self.data,
            "duracao_minutos": self.duracao_minutos,
            "notas": self.notas
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            user_id=data["user_id"],
            materia_id=data["materia_id"],
            topico_id=data["topico_id"],
            data=data["data"],
            duracao_minutos=data["duracao_minutos"],
            notas=data.get("notas")
        )
    
class SessaoEstudoModel:
    FILE_PATH = os.path.join(DATA_DIR, 'sessoes_estudo.json')

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
