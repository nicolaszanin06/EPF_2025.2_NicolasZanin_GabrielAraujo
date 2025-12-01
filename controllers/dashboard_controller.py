from bottle import Bottle
from .base_controller import BaseController
from controllers.auth_controller import AuthController
from services.dashboard_service import DashboardService


class DashboardController(BaseController):
    def _init_(self, app):
        super()._init_(app)
        self.service = DashboardService()
        self._routes()

    def _routes(self):
        self.app.route('/dashboard', method='GET', callback=self.overview)
        self.app.route('/dashboard/subject/<subject_id:int>',
                       method='GET', callback=self.subject_detail)
        self.app.route('/dashboard/topic/<topic_id:int>',
                       method='GET', callback=self.topic_detail)

    def _user(self):
        uid = AuthController.get_logged_user_id(self)
        return int(uid) if uid else None

    # /dashboard
    def overview(self):
        user = self._user()
        if not user:
            return self.redirect('/login')

        data = {
            "overview": self.service.get_overview(user),
            "hours_subject": self.service.get_hours_per_subject(user),
            "hours_last_7": self.service.hours_last_days(user, 7),
            "progress_subject": self.service.subject_progress(user),
        }

        return self.render("dashboard", data=data)

    # /dashboard/subject/<id>
    def subject_detail(self, subject_id):
        user = self._user()
        if not user:
            return self.redirect('/login')

        data = {
            "hours_topic": self.service.get_hours_per_topic(user, subject_id),
            "hours_last_30": self.service.hours_last_days(user, 30),
        }

        return self.render("dashboard_subject", data=data)

    # /dashboard/topic/<id>
    def topic_detail(self, topic_id):
        user = self._user()
        if not user:
            return self.redirect('/login')

        data = {
            "hours_topic": self.service.get_hours_per_topic(user),
            "hours_last_30": self.service.hours_last_days(user, 30),
        }

        return self.render("dashboard_topic", data=data)


dashboard_routes = Bottle()
dashboard_controller = DashboardController(dashboard_routes)
