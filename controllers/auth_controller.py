from bottle import Bottle, request, response
from .base_controller import BaseController
from services.user_service import UsersService


class AuthController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UsersService()
        self._setup_routes()

    def _setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/register', method=['GET', 'POST'], callback=self.register)
        self.app.route('/logout', method='GET', callback=self.logout)

    # LOGIN
    def login(self):
        if request.method == 'GET':
            return self.render('login')

        username = request.forms.get('username')
        password = request.forms.get('password')

        user = self.user_service.find_by_username(username)

        if not user or user.password_hash != password:
            return self.render('login', error="Usuário ou senha inválidos")

        response.set_cookie(
            "session_user",
            str(user.id),
            secret='sua-chave-secreta-aqui'
        )

        return self.redirect('/materias')

    # CADASTRO
    def register(self):
        if request.method == 'GET':
            return self.render('register')

        self.user_service.save()
        return self.redirect('/login')

    # LOGOUT
    def logout(self):
        response.delete_cookie("session_user")
        return self.redirect('/login')


    def get_logged_user_id(self):
        return request.get_cookie("session_user", secret='sua-chave-secreta-aqui')


auth_routes = Bottle()
auth_controller = AuthController(auth_routes)
