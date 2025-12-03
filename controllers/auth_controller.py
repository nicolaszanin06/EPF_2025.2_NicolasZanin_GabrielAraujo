from bottle import Bottle, request, response
from .base_controller import BaseController
from services.user_service import UsersService


SESSION_SECRET = "sua-chave-secreta-aqui"


class AuthController(BaseController):
    def __init__(self, app: Bottle):
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
            # username/error opcionais para reaproveitar o template
            return self.render('login', error=None, username="")

        username = request.forms.get('username') or ""
        password = request.forms.get('password') or ""

        user = self.user_service.find_by_username(username)

        # compara com user.password (não password_hash)
        if not user or user.password != password:
            return self.render(
                'login',
                error="Invalid username or password",
                username=username
            )

        # cria cookie de sessão
        response.set_cookie(
            "session_user",
            str(user.id),
            secret=SESSION_SECRET,
            path="/"
        )

        # depois do login, manda para a página de estatísticas
        return self.redirect('/stats')

  # REGISTER
    def register(self):
        if request.method == 'GET':
            return self.render('register', error=None, username="", email="")

        # aqui dá pra colocar validação, se quiser, antes de salvar
        self.user_service.save()
        return self.redirect('/login')

    # LOGOUT
    def logout(self):
        response.delete_cookie("session_user", path="/")
        return self.redirect('/login')

    def get_logged_user_id(self):
        user_id = request.get_cookie("session_user", secret=SESSION_SECRET)
        return int(user_id) if user_id is not None else None


auth_routes = Bottle()
auth_controller = AuthController(auth_routes)