import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Topico:
    def __init__(self, id, id_materia, titulo, status, duracao_estimada, ordem):
        self.id = id
        self.id_materia = id_materia
        self.titulo = titulo
        self.status = status
        self.duracao_estimada = duracao_estimada
        self.ordem = ordem

    def to_dict(self):
        return {
            "id": self.id,
            "id_materia": self.id_materia,
            "titulo": self.titulo,
            "status": self.status,
            "duracao_estimada": self.duracao_estimada,
            "ordem": self.ordem
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            id_materia=data["id_materia"],
            titulo=data["titulo"],
            status=data["status"],
            duracao_estimada=data["duracao_estimada"],
            ordem=data["ordem"],
        )

class TopicoModel:
    FILE_PATH = os.path.join(DATA_DIR, 'topicos.json')

    def __init__(self):
        self.topicos = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Topico(**item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(
                [t.to_dict() for t in self.topicos],
                f,
                indent=4,
                ensure_ascii=False
            )

    def get_all(self):
        return self.topicos

    def get_by_id(self, topico_id: int):
        return next((t for t in self.topicos if t.id == topico_id), None)

    def add_topico(self, topico: Topico):
        self.topicos.append(topico)
        self._save()

    def update_topico(self, updated_topico: Topico):
        for i, topico in enumerate(self.topicos):
            if topico.id == updated_topico.id:
                self.topicos[i] = updated_topico
                self._save()
                break

    def delete_topico(self, topico_id: int):
        self.topicos = [t for t in self.topicos if t.id != topico_id]
        self._save()