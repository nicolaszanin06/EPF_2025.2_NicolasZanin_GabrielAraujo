from bottle import Bottle, request
from .base_controller import BaseController
from services.stats_service import StatsService
from controllers.auth_controller import AuthController


class StatsController(BaseController):
    def __init__(self, app: Bottle):
        super().__init__(app)
        self.stats_service = StatsService()
        self._setup_routes()

    def _setup_routes(self):
        self.app.route('/stats', method=['GET', 'POST'], callback=self.stats_page)

    def _require_login(self):
        user_id = AuthController.get_logged_user_id(self)
        if not user_id:
            return None
        return int(user_id)

    def stats_page(self):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        if request.method == 'POST':
            start_date = request.forms.get('start_date') or None
            end_date = request.forms.get('end_date') or None
        else:
            start_date = request.query.get('start_date') or None
            end_date = request.query.get('end_date') or None

        stats = self.stats_service.get_stats(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date,
        )

        return self.render(
            'stats',
            stats=stats,
            start_date=start_date,
            end_date=end_date,
        )


stats_routes = Bottle()
stats_controller = StatsController(stats_routes)
