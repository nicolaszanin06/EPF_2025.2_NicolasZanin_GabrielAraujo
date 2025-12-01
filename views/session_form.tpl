% rebase('layout', title='Sessões de estudo')

<style>
  .main-header { display:none !important; }
  .form-page { font-family:'Segoe UI', Tahoma, sans-serif; }

  /* ===== BARRA SUPERIOR (igual stats/subjects) ===== */
  .stats-topbar {
    background: linear-gradient(90deg, #002F54, #005F3B);
    padding:12px 20px;
    border-radius:10px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:22px;
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
    padding:6px 14px;
    border-radius:999px;
    background:white;
    font-weight:600;
    font-size:0.9rem;
    color:#0b3b70;
    cursor:pointer;
    box-shadow:0 1px 3px rgba(0,0,0,0.15);
  }

  .stats-chip:hover {
    background:#eef9f2;
  }

  .btn-logout {
    background:white;
    color:#b91c1c;
    padding:6px 14px;
    border-radius:999px;
    border:none;
    font-weight:600;
    cursor:pointer;
    box-shadow:0 1px 3px rgba(0,0,0,0.15);
  }

  .btn-logout:hover {
    background:#fee2e2;
  }

  /* ===== FORM ===== */
  .page-title {
    font-size:1.6rem;
    color:#0b3b70;
    font-weight:700;
    margin-bottom:18px;
  }

  .form-card {
    background:#fff;
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

  input, select, textarea {
    width:100%;
    padding:10px;
    border:1px solid #cbd5e1;
    border-radius:8px;
    font-size:0.9rem;
  }

  input:focus, select:focus, textarea:focus {
    outline:none;
    border-color:#2563eb;
    box-shadow:0 0 0 1px rgba(37,99,235,0.25);
  }

  .form-actions {
    display:flex;
    gap:10px;
    margin-top:16px;
  }

  .btn-primary {
    background:#005F3B;
    padding:8px 16px;
    color:white;
    border:none;
    border-radius:8px;
    cursor:pointer;
    font-weight:600;
  }

  .btn-primary:hover { background:#007749; }

  .btn-secondary {
    background:#e5e7eb;
    padding:8px 16px;
    border-radius:8px;
    border:none;
    cursor:pointer;
    font-size:0.9rem;
  }

  .helper-text {
    font-size:0.8rem;
    color:#6b7280;
    margin-top:2px;
  }
</style>

<div class="form-page">

  <!-- BARRA SUPERIOR -->
  <div class="stats-topbar">
    <div class="stats-topbar-left">
      <img src="/static/img/logo_study_pequena.png"
           alt="Study Planner"
           class="stats-topbar-logo"
           onclick="window.location.href='/stats'">
      <div style="display:flex;gap:8px;">
        <button class="stats-chip" onclick="window.location.href='/subjects'">
          Matérias
        </button>
        <button class="stats-chip" onclick="window.location.href='/sessions'">
          Sessões de estudo
        </button>
      </div>
    </div>

    <button class="btn-logout" onclick="window.location.href='/logout'">
      Sair
    </button>
  </div>

  <!-- título muda automaticamente: nova x editar -->
  <h2 class="page-title">
    {{'Nova sessão de estudo' if not session else 'Editar sessão de estudo'}}
  </h2>

  <div class="form-card">
    <form method="post">

      <div class="form-group">
        <label for="date">Data da sessão</label>
        <input id="date"
               type="date"
               name="date"
               value="{{session.date if session else ''}}"
               required>
      </div>

      <div class="form-group">
        <label for="duration">Duração (minutos)</label>
        <input id="duration"
               type="number"
               min="1"
               name="duration_minutes"
               value="{{session.duration_minutes if session else ''}}"
               required>
        <div class="helper-text">Ex.: 25, 50, 90…</div>
      </div>

      <div class="form-group">
        <label for="subject_id">Matéria</label>
        <select id="subject_id" name="subject_id" required>
          % for s in subjects:
            <option value="{{s.id}}"
              % if session and session.subject_id == s.id:
                selected
              % end
            >{{s.name}}</option>
          % end
        </select>
      </div>

      <div class="form-group">
        <label for="topic_id">Tópico (opcional)</label>
        <select id="topic_id" name="topic_id">
          <option value="">-- Nenhum --</option>
          % for t in topics:
            <option value="{{t.id}}"
              % if session and session.topic_id == t.id:
                selected
              % end
            >{{t.title}}</option>
          % end
        </select>
      </div>

      <div class="form-group">
        <label for="notes">Notas</label>
        <textarea id="notes" name="notes">{{session.notes if session else ''}}</textarea>
      </div>

      <div class="form-actions">
        <button class="btn-primary" type="submit">Salvar</button>
        <button class="btn-secondary" type="button"
                onclick="window.location.href='/sessions'">
          Cancelar
        </button>
      </div>

    </form>
  </div>
</div>
