from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.auth_controller import auth_routes
from controllers.subject_controller import subject_routes
from controllers.study_session_controller import session_routes


def init_controllers(app: Bottle):
    app.merge(auth_routes)
    app.merge(subject_routes)
    app.merge(session_routes)
    app.merge(user_routes)
