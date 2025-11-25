from bottle import Bottle, request
from .base_controller import BaseController
from services.subject_service import SubjectsService
from controllers.auth_controller import AuthController


class MateriaController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.subject_service = SubjectsService()
        self.auth = AuthController(app)  
        self._setup_routes()

    def _setup_routes(self):
        self.app.route('/materias', method='GET', callback=self.listar)
        self.app.route('/materias/add', method=['GET', 'POST'], callback=self.adicionar)
        self.app.route('/materias/edit/<id:int>', method=['GET', 'POST'], callback=self.editar)
        self.app.route('/materias/delete/<id:int>', method='POST', callback=self.excluir)

    def listar(self):
        user_id = self.auth.get_logged_user_id()
        if not user_id:
            return self.redirect('/login')

        materias = [m for m in self.subject_service.list_all() if m.user_id == int(user_id)]
        return self.render('materias', materias=materias)

    def adicionar(self):
        user_id = self.auth.get_logged_user_id()
        if not user_id:
            return self.redirect('/login')

        if request.method == 'GET':
            return self.render('materia_form', materia=None, action="/materias/add")

        request.forms['user_id'] = user_id  
        self.subject_service.save()
        return self.redirect('/materias')

    def editar(self, id):
        user_id = self.auth.get_logged_user_id()
        if not user_id:
            return self.redirect('/login')

        materia = self.subject_service.get_by_id(id)

        if request.method == 'GET':
            return self.render('materia_form', materia=materia, action=f"/materias/edit/{id}")

        self.subject_service.update(materia)
        return self.redirect('/materias')

    def excluir(self, id):
        self.subject_service.delete(id)
        return self.redirect('/materias')


subject_routes = Bottle()
subject_controller = MateriaController(subject_routes)
