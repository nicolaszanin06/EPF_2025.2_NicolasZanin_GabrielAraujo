from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.auth_controller import auth_routes
from controllers.subject_controller import subject_routes
from controllers.topic_controller import topic_routes
from controllers.study_session_controller import session_routes
from controllers.stats_controller import stats_routes
from controllers.dashboard_controller import dashboard_routes
from controllers.export_controller import export_routes

def init_controllers(app):
    app.merge(auth_routes)
    app.merge(subject_routes)
    app.merge(topic_routes)
    app.merge(session_routes)
    app.merge(stats_routes)
    app.merge(dashboard_routes)   
    app.merge(user_routes)
    app.merge(export_routes)

