from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.auth_controller import auth_routes
from controllers.materia_controller import subject_routes

def init_controllers(app: Bottle):
    app.merge(auth_routes)
    app.merge(subject_routes)
    app.merge(user_routes)
