from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UsersService


class UserController(BaseController):
    def __init__(self, app: Bottle):
        super().__init__(app)
        self.user_service = UsersService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)

    def list_users(self):
        users = self.user_service.list_all()
        return self.render('users', users=users)

    def add_user(self):
        if request.method == 'GET':
            return self.render('user_form', user=None, action="/users/add")
        else:
            self.user_service.save()
            self.redirect('/users')

    def edit_user(self, user_id: int):
        user = self.user_service.get_by_id(user_id)
        if not user:
            return "User not found"

        if request.method == 'GET':
            return self.render('user_form', user=user, action=f"/users/edit/{user_id}")
        else:
            self.user_service.update(user)
            self.redirect('/users')

    def delete_user(self, user_id: int):
        self.user_service.delete(user_id)
        self.redirect('/users')


user_routes = Bottle()
user_controller = UserController(user_routes)
