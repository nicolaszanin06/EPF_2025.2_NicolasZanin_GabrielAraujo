from bottle import request
from models.topico import TopicoModel, Topico

class TopicoService:
    def __init__(self):
        self.model = TopicoModel()

    def list_all(self):
        return self.model.get_all()

    def get_by_id(self, topico_id: int):
        return self.model.get_by_id(topico_id)

    def save(self):
        topicos = self.model.get_all()
        last_id = max((t.id for t in topicos), default=0)
        new_id = last_id + 1

        materia_id = int(request.forms.get('materia_id'))
        titulo = request.forms.get('titulo')
        descricao = request.forms.get('descricao')

        topico = Topico(id=new_id, materia_id=materia_id, titulo=titulo, descricao=descricao)

        self.model.add_topico(topico)

    def update(self, topico: Topico):
        topico.titulo = request.forms.get('titulo')
        topico.descricao = request.forms.get('descricao')

        self.model.update_topico(topico)

    def delete(self, topico_id: int):
        self.model.delete_topico(topico_id)
