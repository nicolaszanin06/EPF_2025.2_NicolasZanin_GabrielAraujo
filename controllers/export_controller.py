from bottle import Bottle, request, response
from .base_controller import BaseController
from services.study_session_service import StudySessionService
from services.subject_service import SubjectService
from services.topic_service import TopicService
from services.export_service import ExportService

SESSION_SECRET = "sua-chave-secreta-aqui"


class ExportController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.session_service = StudySessionService()
        self.subject_service = SubjectService()
        self.topic_service = TopicService()

        self.export_service = ExportService(
            self.session_service,
            self.subject_service,
            self.topic_service
        )

        self._setup_routes()

    def _setup_routes(self):
        self.app.route('/export/full.json', method='GET',
                       callback=self.export_full_json)
        self.app.route('/export/sessions.csv', method='GET',
                       callback=self.export_sessions_csv)
        self.app.route('/export/subjects.csv', method='GET',
                       callback=self.export_subjects_csv)
        self.app.route('/export/topics.csv', method='GET',
                       callback=self.export_topics_csv)

    def _require_login(self):
        user_id = request.get_cookie("session_user", secret=SESSION_SECRET)
        return int(user_id) if user_id else None

    def export_full_json(self):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        data = self.export_service.export_full_json(user_id)

        response.content_type = "application/json"
        response.set_header("Content-Disposition",
                            "attachment; filename=backup.json")
        return data

    def export_sessions_csv(self):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        csv_data = self.export_service.export_sessions_csv(user_id)
        response.content_type = "text/csv"
        response.set_header("Content-Disposition",
                            "attachment; filename=sessions.csv")
        return csv_data

    def export_subjects_csv(self):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        csv_data = self.export_service.export_subjects_csv(user_id)
        response.content_type = "text/csv"
        response.set_header("Content-Disposition",
                            "attachment; filename=subjects.csv")
        return csv_data

    def export_topics_csv(self):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        csv_data = self.export_service.export_topics_csv(user_id)
        response.content_type = "text/csv"
        response.set_header("Content-Disposition",
                            "attachment; filename=topics.csv")
        return csv_data


export_routes = Bottle()
export_controller = ExportController(export_routes)