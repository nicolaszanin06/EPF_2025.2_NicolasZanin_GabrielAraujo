from bottle import Bottle, request
from datetime import date
from .base_controller import BaseController
from services.study_session_service import StudySessionService
from services.subject_service import SubjectService
from services.topic_service import TopicService
from services.stats_service import StatsService
from services.user_service import UsersService

SESSION_SECRET = "sua-chave-secreta-aqui"


class StatsController(BaseController):
    def __init__(self, app: Bottle):
        super().__init__(app)
        self.session_service = StudySessionService()
        self.subject_service = SubjectService()
        self.topic_service = TopicService()
        self.stats_service = StatsService(
            self.session_service,
            self.subject_service,
            self.topic_service
        )
        self.user_service = UsersService()
        self._setup_routes()

    def _setup_routes(self):
        self.app.route('/stats', method='GET', callback=self.dashboard)

    def _require_login(self):
        from bottle import request
        user_id = request.get_cookie("session_user", secret=SESSION_SECRET)
        if not user_id:
            return None
        return int(user_id)

    def dashboard(self):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        start_date = request.query.get('start_date') or None
        end_date = request.query.get('end_date') or None

        stats = self.stats_service.get_stats(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date
        )

        user = self.user_service.get_by_id(user_id)
        is_admin = bool(user and getattr(user, "role", "") == "admin")

        return self.render(
            'stats',
            stats=stats,
            subjects=stats["subjects"],
            is_admin=is_admin,
            start_date=stats["start_date"],
            end_date=stats["end_date"],
        )

stats_routes = Bottle()
stats_controller = StatsController(stats_routes)
