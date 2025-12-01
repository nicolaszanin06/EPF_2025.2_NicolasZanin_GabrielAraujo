% rebase('layout', title='Matérias')

<style>
  .main-header { display:none !important; }

  .form-page {
    font-family: 'Segoe UI', Tahoma, sans-serif;
  }

  .stats-topbar {
    background: linear-gradient(90deg, #002F54 0%, #005F3B 100%);
    padding: 10px 18px;
    border-radius: 10px;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .stats-topbar-left {
    display: flex;
    align-items: center;
    gap: 16px;
    cursor: pointer;
  }

  .stats-topbar-logo {
    height: 70px;
  }

  .stats-chip {
    border: none;
    border-radius: 999px;
    padding: 6px 16px;
    background: #fff;
    color: #0b3b70;
    font-weight: 600;
    cursor: pointer;
  }

  .btn-logout {
    border: none;
    border-radius: 999px;
    padding: 6px 16px;
    background: white;
    color: #b91c1c;
    font-weight: 600;
    cursor:pointer;
  }

  .page-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #0b3b70;
    margin-bottom: 18px;
  }

  .form-card {
    background: white;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.12);
    max-width: 550px;
    margin: 0 auto;
  }

  .form-group {
    margin-bottom: 14px;
  }

  .form-group label {
    display:block;
    font-size:0.9rem;
    margin-bottom:4px;
    color:#374151;
  }

  input, textarea, select {
    width:100%;
    padding:9px 12px;
    border-radius:8px;
    border:1px solid #cbd5e1;
    font-size:0.9rem;
  }

  input:focus, textarea:focus, select:focus {
    outline:none;
    border-color:#2563eb;
    box-shadow:0 0 0 1px rgba(37,99,235,0.25);
  }

  .form-actions {
    margin-top:20px;
    display:flex;
    gap:12px;
  }

  .btn-primary {
    background:#005F3B;
    color:white;
    border:none;
    border-radius:8px;
    padding:8px 16px;
    font-weight:600;
    cursor:pointer;
  }

  .btn-primary:hover {
    background:#007749;
  }

  .btn-secondary {
    background:#e5e7eb;
    border:none;
    border-radius:8px;
    padding:8px 16px;
    cursor:pointer;
  }
</style>

<div class="form-page">

  <!-- TOP BAR -->
  <div class="stats-topbar">
  <div class="stats-topbar-left">
    <img src="/static/img/logo_study_pequena.png"
         class="stats-topbar-logo"
         alt="Study Planner"
         onclick="window.location.href='/stats'">

    <div style="display:flex;gap:8px;">
      <button type="button" class="stats-chip" onclick="window.location.href='/subjects'">
        Matérias
      </button>
      <button type="button" class="stats-chip" onclick="window.location.href='/sessions'">
        Sessões de estudo
      </button>
    </div>
  </div>

  <button type="button" class="btn-logout" onclick="window.location.href='/logout'">
    Sair
  </button>
</div>


  <!-- título muda automaticamente: nova x editar -->
  <h2 class="page-title">
    {{'Nova matéria' if not subject else 'Editar matéria'}}
  </h2>

  <div class="form-card">
    <form method="post">

      <div class="form-group">
        <label>Nome da matéria</label>
        <input type="text" name="name" value="{{subject.name if subject else ''}}" required>
      </div>

      <div class="form-group">
        <label>Cor (hexadecimal)</label>
        <input type="text" name="color" value="{{subject.color if subject else ''}}" placeholder="#00AA33">
      </div>

      <div class="form-group">
        <label>Descrição</label>
        <textarea name="description">{{subject.description if subject else ''}}</textarea>
      </div>

      <div class="form-actions">
        <button class="btn-primary" type="submit">Salvar</button>
        <button class="btn-secondary" type="button"
                onclick="window.location.href='/subjects'">Cancelar</button>
      </div>

    </form>
  </div>
</div>
