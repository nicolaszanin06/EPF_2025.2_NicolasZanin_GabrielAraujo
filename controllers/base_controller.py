from bottle import static_file, request, template as render_template, HTTPResponse

# ATENÇÃO: precisa ser o mesmo valor usado no AuthController
SESSION_SECRET = "sua-chave-secreta-aqui"


class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()

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

    def get_logged_user_id(self):
        """
        Lê o ID do usuário logado a partir do cookie 'session_user'.
        Retorna int ou None se não estiver logado.
        """
        user_id = request.get_cookie("session_user", secret=SESSION_SECRET)
        return int(user_id) if user_id else None

    def is_admin(self):
        """
        Verifica o papel do usuário a partir do cookie 'session_role'.
        Espera 'admin' para administrador.
        """
        role = request.get_cookie("session_role", secret=SESSION_SECRET)
        if not role:
            return False
        return str(role).strip().lower() == "admin"

    def render(self, template_name, **context):
        """
        Renderiza templates sempre injetando 'is_admin' no contexto,
        caso ainda não tenha sido passado explicitamente.
        """
        context.setdefault("is_admin", self.is_admin())
        return render_template(template_name, **context)

    def redirect(self, path, code=302):
        """
        Redireciona usando sempre HTTPResponse.

        Isso garante que isinstance(x, HTTPResponse) funcione nos controllers
        que verificam esse tipo (como outros controllers do sistema).
        """
        return HTTPResponse(
            body='',
            status=code,
            headers={'Location': path}
        )
