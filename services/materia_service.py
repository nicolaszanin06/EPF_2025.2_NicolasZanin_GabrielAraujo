from bottle import request
from models.materia import MateriaModel, Materia

class MateriaService:
    def __init__(self):
        self.model = MateriaModel()

    def list_all(self):
        return self.model.get_all()

    def get_by_id(self, materia_id: int):
        return self.model.get_by_id(materia_id)

    def save(self):
        materias = self.model.get_all()
        last_id = max((m.id for m in materias), default=0)
        new_id = last_id + 1

        user_id = int(request.forms.get('user_id'))
        name = request.forms.get('nome')
        description = request.forms.get('descricao')

        materia = Materia(id=new_id, user_id=user_id, name=name, description=description)

        self.model.add_materia(materia)

    def update(self, materia: Materia):
        materia.name = request.forms.get('nome')
        materia.description = request.forms.get('descricao')

        self.model.update_materia(materia)

    def delete(self, materia_id: int):
        self.model.delete_materia(materia_id)
