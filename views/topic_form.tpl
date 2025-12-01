% rebase('layout', title='Tópicos')

<style>
  .main-header { display:none !important; }
  .form-page { font-family:'Segoe UI', Tahoma, sans-serif; }

  /* ===== BARRA SUPERIOR (igual stats/subjects/sessions) ===== */
  .stats-topbar {
    background: linear-gradient(90deg, #002F54 0%, #005F3B 100%);
    padding: 10px 18px;
    border-radius: 10px;
    margin-bottom: 22px;
    display:flex;
    justify-content:space-between;
    align-items:center;
  }

  .stats-topbar-left {
    display:flex;
    align-items:center;
    gap:16px;
  }

  .stats-topbar-logo {
    height:70px;
    cursor:pointer;
  }

  .stats-chip {
    border:none;
    border-radius:999px;
    padding:6px 16px;
    background:#ffffff;
    font-size:0.9rem;
    font-weight:600;
    color:#0b3b70;
    cursor:pointer;
    box-shadow:0 1px 3px rgba(0,0,0,0.15);
  }

  .stats-chip:hover {
    background:#eef9f2;
  }

  .btn-logout {
    border:none;
    border-radius:999px;
    padding:6px 16px;
    background:#ffffff;
    font-size:0.9rem;
    font-weight:600;
    color:#b91c1c;
    cursor:pointer;
    box-shadow:0 1px 3px rgba(0,0,0,0.15);
  }

  .btn-logout:hover {
    background:#fee2e2;
  }

  /* ===== FORM ===== */
  .page-title {
    font-size:1.5rem;
    font-weight:700;
    color:#0b3b70;
    margin-bottom:6px;
  }

  .page-subtitle {
    font-size:0.95rem;
    color:#4b5563;
    margin-bottom:16px;
  }

  .form-card {
    background:#ffffff;
    padding:24px;
    border-radius:12px;
    max-width:550px;
    margin:0 auto;
    box-shadow:0 2px 8px rgba(0,0,0,0.15);
  }

  .form-group { margin-bottom:14px; }

  .form-group label {
    display:block;
    margin-bottom:4px;
    font-size:0.9rem;
    color:#374151;
  }

  .form-group input,
  .form-group select {
    width:100%;
    padding:9px 12px;
    border-radius:8px;
    border:1px solid #cbd5e1;
    font-size:0.9rem;
  }

  .form-group input:focus,
  .form-group select:focus {
    outline:none;
    border-color:#2563eb;
    box-shadow:0 0 0 1px rgba(37,99,235,0.25);
  }

  .form-actions {
    margin-top:18px;
    display:flex;
    gap:10px;
  }

  .btn-primary {
    background:#005F3B;
    color:#ffffff;
    border:none;
    border-radius:8px;
    padding:8px 16px;
    font-weight:600;
    cursor:pointer;
  }

  .btn-primary:hover { background:#007749; }

  .btn-secondary {
    background:#e5e7eb;
    color:#111827;
    border:none;
    border-radius:8px;
    padding:8px 16px;
    font-size:0.9rem;
    cursor:pointer;
  }

  .btn-secondary:hover {
    background:#d1d5db;
  }
</style>

<div class="form-page">

  <!-- BARRA SUPERIOR -->
  <div class="stats-topbar">
    <div class="stats-topbar-left">
      <img src="/static/img/logo_study_pequena.png"
           class="stats-topbar-logo"
           alt="Study Planner"
           onclick="window.location.href='/stats'">

      <div style="display:flex;gap:8px;">
        <button type="button" class="stats-chip"
                onclick="window.location.href='/subjects'">
          Matérias
        </button>
        <button type="button" class="stats-chip"
                onclick="window.location.href='/sessions'">
          Sessões de estudo
        </button>
      </div>
    </div>

    <button type="button" class="btn-logout"
            onclick="window.location.href='/logout'">
      Sair
    </button>
  </div>

  <!-- TÍTULO + SUBTÍTULO -->
  <h2 class="page-title">
    {{'Novo tópico' if not topic else 'Editar tópico'}}
  </h2>
  <p class="page-subtitle">
    Matéria: <strong>{{subject.name}}</strong>
  </p>

  <!-- FORMULÁRIO -->
  <div class="form-card">
    <form method="post" action="{{action}}">

      <div class="form-group">
        <label for="title">Título</label>
        <input id="title"
               name="title"
               type="text"
               required
               value="{{topic.title if topic else ''}}">
      </div>

      <div class="form-group">
        <label for="status">Status</label>
        <select id="status" name="status">
          <option value="pending"
            % if not topic or topic.status == 'pending':
              selected
            % end
          >Pendente</option>

          <option value="completed"
            % if topic and topic.status == 'completed':
              selected
            % end
          >Concluído</option>
        </select>
      </div>

      <div class="form-group">
        <label for="estimated_minutes">Tempo estimado (minutos)</label>
        <input id="estimated_minutes"
               name="estimated_minutes"
               type="number"
               min="0"
               value="{{topic.estimated_minutes if topic else ''}}">
      </div>

      <div class="form-group">
        <label for="order">Ordem</label>
        <input id="order"
               name="order"
               type="number"
               min="0"
               value="{{topic.order if topic else ''}}">
      </div>

      <div class="form-actions">
        <button type="submit" class="btn-primary">Salvar</button>
        <button type="button"
                class="btn-secondary"
                onclick="window.location.href='/subjects/{{subject.id}}/topics'">
          Cancelar
        </button>
      </div>
    </form>
  </div>

</div>
