from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UsersService
from controllers.auth_controller import AuthController


class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UsersService()
        self._setup_routes()

    def _setup_routes(self):
        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)

    def _get_logged_user(self):
        user_id = AuthController.get_logged_user_id()
        if not user_id:
            return None
        return self.user_service.get_by_id(user_id)

    def _ensure_admin(self):
        user = self._get_logged_user()
        if not user:
            return self.redirect('/login')
        if user.role != 'admin':
            return self.redirect('/subjects')
        return user

    def list_users(self):
        admin = self._ensure_admin()
        if not isinstance(admin, object): 
            return admin

        users = self.user_service.list_all()
        return self.render('users', users=users)

    def add_user(self):
        admin = self._ensure_admin()
        if not isinstance(admin, object):
            return admin

        if request.method == 'GET':
            return self.render('user_form', user=None, action='/users/add')

        self.user_service.save()
        return self.redirect('/users')

    def edit_user(self, user_id):
        admin = self._ensure_admin()
        if not isinstance(admin, object):
            return admin

        user = self.user_service.get_by_id(user_id)
        if not user:
            return self.redirect('/users')

        if request.method == 'GET':
            return self.render('user_form', user=user, action=f'/users/edit/{user_id}')

        self.user_service.update(user)
        return self.redirect('/users')

    def delete_user(self, user_id):
        admin = self._ensure_admin()
        if not isinstance(admin, object):
            return admin

        self.user_service.delete(user_id)
        return self.redirect('/users')


user_routes = Bottle()
user_controller = UserController(user_routes)
