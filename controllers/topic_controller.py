from bottle import Bottle, request
from .base_controller import BaseController
from services.topic_service import TopicService
from services.subject_service import SubjectService

SESSION_SECRET = "sua-chave-secreta-aqui"


class TopicController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.topic_service = TopicService()
        self.subject_service = SubjectService()
        self._setup_routes()

    def _setup_routes(self):
        # Listar tópicos de uma matéria
        self.app.route(
            '/subjects/<subject_id:int>/topics',
            method='GET',
            callback=self.list_by_subject
        )

        # Criar novo tópico
        self.app.route(
            '/subjects/<subject_id:int>/topics/new',
            method=['GET', 'POST'],
            callback=self.add
        )

        # Editar tópico existente
        self.app.route(
            '/subjects/<subject_id:int>/topics/<topic_id:int>/edit',
            method=['GET', 'POST'],
            callback=self.edit
        )

        # Excluir tópico
        self.app.route(
            '/subjects/<subject_id:int>/topics/<topic_id:int>/delete',
            method='POST',
            callback=self.delete
        )

        # Alternar status (pendente/concluído)
        self.app.route(
            '/subjects/<subject_id:int>/topics/<topic_id:int>/toggle',
            method='POST',
            callback=self.toggle_status
        )

    # Helpers ---------------------------------------------------------

    def _get_logged_user_id(self):
        """Obtém o ID do usuário logado lendo o cookie de sessão."""
        user_id = request.get_cookie("session_user", secret=SESSION_SECRET)
        return int(user_id) if user_id is not None else None

    def _ensure_subject_owner(self, subject_id: int):
        """
        Garante que a matéria pertence ao usuário logado.

        Retorna (subject, response):
          - (subject, None) se estiver tudo OK
          - (None, redirect(...)) se precisar redirecionar
        """
        user_id = self._get_logged_user_id()
        if not user_id:
            return None, self.redirect('/login')

        subject = self.subject_service.get_by_id(subject_id)
        if not subject or subject.user_id != user_id:
            # não deixa acessar matéria de outro usuário
            return None, self.redirect('/subjects')

        return subject, None

    # Actions ---------------------------------------------------------

    def list_by_subject(self, subject_id):
        subject, resp = self._ensure_subject_owner(subject_id)
        if resp:
            return resp  # já redirecionou

        all_topics = self.topic_service.list_all()
        topics = [t for t in all_topics if t.subject_id == subject_id]

        return self.render(
            'topics',
            subject=subject,
            topics=topics
        )

    def add(self, subject_id):
        subject, resp = self._ensure_subject_owner(subject_id)
        if resp:
            return resp

        if request.method == 'GET':
            return self.render(
                'topic_form',
                subject=subject,
                topic=None,
                action=f'/subjects/{subject_id}/topics/new'
            )

        # POST — garante que o form tenha subject_id pro service usar
        request.forms['subject_id'] = str(subject_id)
        self.topic_service.save()
        return self.redirect(f'/subjects/{subject_id}/topics')

    def edit(self, subject_id, topic_id):
        subject, resp = self._ensure_subject_owner(subject_id)
        if resp:
            return resp

        topic = self.topic_service.get_by_id(topic_id)
        if not topic or topic.subject_id != subject_id:
            return self.redirect(f'/subjects/{subject_id}/topics')

        if request.method == 'GET':
            return self.render(
                'topic_form',
                subject=subject,
                topic=topic,
                action=f'/subjects/{subject_id}/topics/{topic_id}/edit'
            )

        # POST
        self.topic_service.update(topic)
        return self.redirect(f'/subjects/{subject_id}/topics')

    def delete(self, subject_id, topic_id):
        subject, resp = self._ensure_subject_owner(subject_id)
        if resp:
            return resp

        topic = self.topic_service.get_by_id(topic_id)
        if topic and topic.subject_id == subject_id:
            self.topic_service.delete(topic_id)

        return self.redirect(f'/subjects/{subject_id}/topics')

    def toggle_status(self, subject_id, topic_id):
        subject, resp = self._ensure_subject_owner(subject_id)
        if resp:
            return resp

        topic = self.topic_service.get_by_id(topic_id)
        if not topic or topic.subject_id != subject_id:
            return self.redirect(f'/subjects/{subject_id}/topics')

        # alterna entre 'pending' e 'completed'
        topic.status = 'completed' if topic.status != 'completed' else 'pending'
        self.topic_service.update(topic)

        return self.redirect(f'/subjects/{subject_id}/topics')


topic_routes = Bottle()
topic_controller = TopicController(topic_routes)
