from bottle import static_file, template as render_template, request, HTTPResponse, response as bottle_response
from services.user_service import UsersService

SESSION_SECRET = "sua-chave-secreta-aqui"


class BaseController:
    def __init__(self, app):
        self.app = app
        self.user_service = UsersService()
        self._setup_base_routes()

    # ------------------ Rotas básicas ------------------ #
    def _setup_base_routes(self):
        """Configura rotas básicas comuns a todos os controllers"""
        self.app.route('/', method='GET', callback=self.home_redirect)
        self.app.route('/helper', method=['GET'], callback=self.helper)

        # Rota para arquivos estáticos (CSS, JS, imagens)
        self.app.route('/static/<filename:path>', callback=self.serve_static)

    def home_redirect(self):
        """Redireciona a rota raiz para a página principal (estatísticas)."""
        return self.redirect('/stats')

    def helper(self):
        return self.render('helper-final')

    def serve_static(self, filename):
        """Serve arquivos estáticos da pasta static/"""
        return static_file(filename, root='./static')

    # ------------------ Usuário logado / admin ------------------ #
    def _get_current_user(self):
        """Retorna o objeto User logado ou None."""
        user_id = request.get_cookie("session_user", secret=SESSION_SECRET)
        if not user_id:
            return None

        try:
            user_id = int(user_id)
        except ValueError:
            return None

        # procura o usuário pelo id
        for u in self.user_service.list_all():
            if u.id == user_id:
                return u
        return None

    # ------------------ Helpers de render e redirect ------------------ #
    def render(self, template_name, **context):
        user = self._get_current_user()

        # admin se role == 'admin'
        role = getattr(user, "role", "") if user else ""
        is_admin = (str(role).lower() == "admin")

        # injeta no contexto dos templates
        context.setdefault("current_user", user)
        context.setdefault("is_admin", is_admin)
        context.setdefault("current_role", role)

        return render_template(template_name, **context)


    def redirect(self, path, code=302):
        """Redirecionamento robusto com tratamento de erros"""
        try:
            bottle_response.status = code
            bottle_response.set_header('Location', path)
            return bottle_response
        except Exception as e:
            print(f"ERRO NO REDIRECT: {type(e).__name__} - {str(e)}")
            return HTTPResponse(
                body=f'<script>window.location.href="{path}";</script>',
                status=200,
                headers={'Content-Type': 'text/html'}
            )
