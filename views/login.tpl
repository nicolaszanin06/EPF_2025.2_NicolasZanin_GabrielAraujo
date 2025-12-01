% rebase('layout', title='Login', hide_header=True)

<!-- CSS específico só da tela de login -->
<style>
  /* Esconde header e footer só nesta página */
  .main-header,
  .main-footer {
    display: none !important;
  }

  /* Área inteira da página de login */
  .login-page {
    min-height: 100vh;
    background: #f9fafb;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 24px 16px;
  }

  /* Logo */
  .login-logo {
    display: flex;
    justify-content: center;
    margin-bottom: 18px;
  }

  .login-logo img {
    max-width: 500px;
    width: 100%;
    height: auto;
    display: block;
  }

  /* Card de login */
  .login-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 24px 28px;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.15);
    width: 100%;
    max-width: 420px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  .login-card-title {
    font-size: 1.6rem;
    font-weight: 600;
    margin-bottom: 20px;
    text-align: center;
  }

  .auth-error {
    background: #fee2e2;
    border: 1px solid #fecaca;
    color: #b91c1c;
    padding: 8px 10px;
    border-radius: 6px;
    font-size: 0.85rem;
    margin-bottom: 12px;
  }

  .auth-form {
    margin-top: 4px;
  }

  .auth-form .form-group {
    margin-bottom: 12px;
  }

  .auth-form label {
    display: block;
    font-size: 0.9rem;
    margin-bottom: 4px;
    color: #374151;
  }

  .auth-form input {
    width: 100%;
    padding: 8px 10px;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
    font-size: 0.9rem;
    outline: none;
  }

  .auth-form input:focus {
    border-color: #2563eb;
    box-shadow: 0 0 0 1px rgba(37, 99, 235, 0.2);
  }

  .auth-form button {
    width: 100%;
    margin-top: 8px;
    padding: 9px 10px;
    border-radius: 6px;
    border: none;
    background: #005F3A;
    color: #fff;
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.15s ease, transform 0.1s ease;
  }

  .auth-form button:hover {
    background: #1d4ed8;
    transform: translateY(-1px);
  }

  .auth-footer {
    margin-top: 12px;
    font-size: 0.85rem;
    text-align: center;
  }

  .auth-footer a {
    color: #002F54;
    text-decoration: none;
    font-weight: 500;
  }

  .auth-footer a:hover {
    text-decoration: underline;
  }
</style>

<div class="login-page">
  <!-- LOGO -->
  <div class="login-logo">
    <img src="/static/img/logo_study.png"
         alt="Study Planner">
  </div>

  <!-- CARD DE LOGIN -->
  <div class="login-card">
    <h1 class="login-card-title">Entrar</h1>

    % if error:
      <p class="auth-error">{{error}}</p>
    % end

    <form action="/login" method="post" class="auth-form">
      <div class="form-group">
        <label for="username">Usuário</label>
        <input id="username" name="username" type="text" required>
      </div>

      <div class="form-group">
        <label for="password">Senha</label>
        <input id="password" name="password" type="password" required>
      </div>

      <button type="submit">Login</button>
    </form>

    <p class="auth-footer">
      Não tem uma conta?
      <a href="/register">Registre-se aqui</a>.
    </p>
  </div>
</div>
