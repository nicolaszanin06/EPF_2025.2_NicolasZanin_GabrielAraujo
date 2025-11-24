from bottle import request
from models.sessao_estudo import SessaoEstudoModel, SessaoEstudo

class StudySessionService:
    def __init__(self):
        self.model = SessaoEstudoModel()

    def list_all(self):
        return self.model.get_all()

    def get_by_id(self, sessao_id: int):
        return self.model.get_by_id(sessao_id)

    def save(self):
        sessoes = self.model.get_all()
        last_id = max((s.id for s in sessoes), default=0)
        new_id = last_id + 1

        user_id = int(request.forms.get('user_id'))
        materia_id = int(request.forms.get('materia_id'))
        topico_id = int(request.forms.get('topico_id'))
        data = request.forms.get('data')
        duracao_minutos = int(request.forms.get('duracao_minutos'))
        notas = request.forms.get('notas')

        sessao = SessaoEstudo(id=new_id,user_id=user_id,materia_id=materia_id,topico_id=topico_id,
                              data=data,duracao_minutos=duracao_minutos,notas=notas)

        self.model.add_sessao(sessao)

    def update(self, sessao: SessaoEstudo):
        sessao.data = request.forms.get('data')
        sessao.duracao_minutos = int(request.forms.get('duracao_minutos'))
        sessao.notas = request.forms.get('notas')

        self.model.update_sessao(sessao)

    def delete(self, sessao_id: int):
        self.model.delete_sessao(sessao_id)
