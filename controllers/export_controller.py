# controllers/export_controller.py
from bottle import Bottle, request, response, HTTPResponse
from .base_controller import BaseController
from services.study_session_service import StudySessionService
from services.subject_service import SubjectService
from services.topic_service import TopicService
from services.export_service import ExportService
from services.user_service import UsersService

SESSION_SECRET = "sua-chave-secreta-aqui"


class ExportController(BaseController):
    def __init__(self, app: Bottle):
        super().__init__(app)
        self.session_service = StudySessionService()
        self.subject_service = SubjectService()
        self.topic_service = TopicService()
        self.export_service = ExportService(
            self.session_service,
            self.subject_service,
            self.topic_service
        )
        self.user_service = UsersService()
        self._setup_routes()

    def _setup_routes(self):
        self.app.route('/export/full.json', method='GET', callback=self.export_full_json)
        self.app.route('/export/sessions.csv', method='GET', callback=self.export_sessions_csv)
        self.app.route('/export/subjects.csv', method='GET', callback=self.export_subjects_csv)
        self.app.route('/export/topics.csv', method='GET', callback=self.export_topics_csv)

    def _get_logged_user(self):
        user_id = request.get_cookie("session_user", secret=SESSION_SECRET)
        if not user_id:
            return None
        return self.user_service.get_by_id(int(user_id))

    def _ensure_admin(self):
        """Garante que o usuário esteja logado e seja admin.

        Retorna:
          - HTTPResponse de redirect (login/subjects) em caso de erro
          - objeto user (admin) em caso de sucesso
        """
        user = self._get_logged_user()
        if not user:
            return self.redirect('/login')
        if getattr(user, "role", "") != "admin":
            return self.redirect('/subjects')
        return user

    def export_full_json(self):
        admin = self._ensure_admin()
        if isinstance(admin, HTTPResponse):
            return admin

        user_id = admin.id
        data = self.export_service.export_full_json(user_id)
        response.content_type = 'application/json; charset=utf-8'
        return data

    def export_sessions_csv(self):
        admin = self._ensure_admin()
        if isinstance(admin, HTTPResponse):
            return admin

        user_id = admin.id
        csv_data = self.export_service.export_sessions_csv(user_id)
        response.content_type = 'text/csv; charset=utf-8'
        return csv_data

    def export_subjects_csv(self):
        admin = self._ensure_admin()
        if isinstance(admin, HTTPResponse):
            return admin

        user_id = admin.id
        csv_data = self.export_service.export_subjects_csv(user_id)
        response.content_type = 'text/csv; charset=utf-8'
        return csv_data

    def export_topics_csv(self):
        admin = self._ensure_admin()
        if isinstance(admin, HTTPResponse):
            return admin

        user_id = admin.id
        csv_data = self.export_service.export_topics_csv(user_id)
        response.content_type = 'text/csv; charset=utf-8'
        return csv_data


export_routes = Bottle()
export_controller = ExportController(export_routes)
