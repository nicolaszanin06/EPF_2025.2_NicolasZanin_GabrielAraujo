from bottle import Bottle, request
from datetime import date
from .base_controller import BaseController
from services.study_session_service import StudySessionService
from services.subject_service import SubjectService
from services.topic_service import TopicService
from services.stats_service import StatsService

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

        self._setup_routes()

    def _setup_routes(self):
        self.app.route('/stats', method='GET', callback=self.dashboard)

    def _require_login(self):
        user_id = request.get_cookie("session_user", secret=SESSION_SECRET)
        return int(user_id) if user_id else None

    def dashboard(self):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        # pega filtros opcionais
        start_date = request.query.get('start_date')
        end_date   = request.query.get('end_date')

        # chama o StatsService
        stats = self.stats_service.get_stats(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date
        )

        # renderiza stats.tpl
        return self.render(
            'stats',
            stats=stats,
            subjects=stats["subjects"],
        )


stats_routes = Bottle()
stats_controller = StatsController(stats_routes)