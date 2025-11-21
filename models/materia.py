import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Materia:
    def __init__(self, id, user_id, nome, descricao= None):
        self.id = id
        self.user_id = user_id
        self.nome = nome
        self.descricao = descricao

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "nome": self.nome,
            "descricao": self.descricao
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            user_id=data["user_id"],
            nome=data["nome"],
            descricao=data.get("descricao")
        )


class MateriaModel:
    FILE_PATH = os.path.join(DATA_DIR, 'materias.json')

    def __init__(self):
        self.materias = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Materia(**item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(
                [m.to_dict() for m in self.materias],
                f,
                indent=4,
                ensure_ascii=False
            )

    def get_all(self):
        return self.materias

    def get_by_id(self, materia_id: int):
        return next((m for m in self.materias if m.id == materia_id), None)

    def add_materia(self, materia: Materia):
        self.materias.append(materia)
        self._save()

    def update_materia(self, updated_materia: Materia):
        for i, materia in enumerate(self.materias):
            if materia.id == updated_materia.id:
                self.materias[i] = updated_materia
                self._save()
                break

    def delete_materia(self, materia_id: int):
        self.materias = [m for m in self.materias if m.id != materia_id]
        self._save()