from bottle import Bottle, request
from .base_controller import BaseController
from services.subject_service import SubjectService
from controllers.auth_controller import AuthController


class SubjectController(BaseController):
    def __init__(self, app: Bottle):
        super().__init__(app)

        self.subject_service = SubjectService()
        self.auth = AuthController 

        self._setup_routes()

    def _setup_routes(self):
        self.app.route('/subjects', method='GET', callback=self.list_subjects)
        self.app.route('/subjects/new', method=['GET', 'POST'], callback=self.new_subject)
        self.app.route('/subjects/<id:int>/edit', method=['GET', 'POST'], callback=self.edit_subject)
        self.app.route('/subjects/<id:int>/delete', method='POST', callback=self.delete_subject)

    def list_subjects(self):
        user_id = AuthController.get_logged_user_id(self)
        if not user_id:
            return self.redirect('/login')

        subjects = [
            s for s in self.subject_service.list_all()
            if s.user_id == int(user_id)
        ]

        return self.render('subjects', subjects=subjects)

    def new_subject(self):
        user_id = AuthController.get_logged_user_id(self)
        if not user_id:
            return self.redirect('/login')

        if request.method == 'GET':
            return self.render('subject_form', subject=None, action="/subjects/new", user_id=user_id)

        request.forms['user_id'] = user_id
        self.subject_service.save()
        return self.redirect('/subjects')

    def edit_subject(self, id):
        user_id = AuthController.get_logged_user_id(self)
        if not user_id:
            return self.redirect('/login')

        subject = self.subject_service.get_by_id(id)
        if not subject:
            return "Subject not found"

        if request.method == 'GET':
            return self.render('subject_form', subject=subject, action=f"/subjects/{id}/edit", user_id=user_id)

        self.subject_service.update(subject)
        return self.redirect('/subjects')

    def delete_subject(self, id):
        self.subject_service.delete(id)
        return self.redirect('/subjects')


subject_routes = Bottle()
subject_controller = SubjectController(subject_routes)
