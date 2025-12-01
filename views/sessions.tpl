% rebase('layout', title='Sessões de estudo')

<style>
  /* Esconde o header padrão nesta página */
  .main-header {
    display: none !important;
  }

  .sessions-page {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  /* ===== BARRA SUPERIOR IGUAL À DE ESTATÍSTICAS ===== */
  .stats-topbar {
    background: linear-gradient(90deg, #002F54 0%, #005F3B 100%);
    padding: 10px 18px;
    border-radius: 10px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .stats-topbar-left {
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .stats-topbar-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
  }

  .stats-topbar-logo {
    height: 70px;
    width: auto;
    display: block;
  }

  .stats-topbar-title {
    color: #e5f3ff;
    font-weight: 600;
    letter-spacing: 0.03em;
    font-size: 1rem;
  }

  .stats-topbar-actions {
    display: flex;
    gap: 8px;
  }

  .stats-chip {
    border: none;
    border-radius: 999px;
    padding: 6px 16px;
    font-size: 0.9rem;
    font-weight: 600;
    background: #ffffff;
    color: #0b3b70;
    cursor: pointer;
    box-shadow: 0 1px 3px rgba(0,0,0,0.15);
    text-decoration: none;
    display: inline-block;
    transition: transform 0.08s ease, box-shadow 0.08s ease, background 0.12s ease;
  }

  .stats-chip:hover {
    background: #eef9f2;
    transform: translateY(-1px);
    box-shadow: 0 3px 6px rgba(0,0,0,0.16);
  }

  .stats-topbar-right {
    display: flex;
    align-items: center;
  }

  .btn-logout {
    border: none;
    border-radius: 999px;
    padding: 6px 16px;
    font-size: 0.9rem;
    font-weight: 600;
    background: #ffffff;
    color: #b91c1c;
    cursor: pointer;
    box-shadow: 0 1px 3px rgba(0,0,0,0.15);
    transition: transform 0.08s ease, box-shadow 0.08s ease, background 0.12s ease;
  }

  .btn-logout:hover {
    background: #fee2e2;
    transform: translateY(-1px);
    box-shadow: 0 3px 6px rgba(0,0,0,0.16);
  }

  /* ===== TÍTULO E BOTÃO VERDE CENTRAL ===== */
  .page-title-main {
    font-size: 1.5rem;
    font-weight: 700;
    color: #0b3b70;
    margin-bottom: 12px;
  }

  .create-card-wrapper {
    display: flex;
    justify-content: center;
    margin: 24px 0 16px;
  }

  .create-card {
    width: 260px;
    height: 220px;
    background: #005F3B;
    border-radius: 18px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
    text-decoration: none;
    color: #ffffff;
    box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    transition: transform 0.12s ease, box-shadow 0.12s ease, background 0.12s ease;
  }

  .create-card:hover {
    background: #007749;
    transform: translateY(-3px);
    box-shadow: 0 16px 40px rgba(0,0,0,0.28);
  }

  .create-card-icon {
    font-size: 3rem;
    line-height: 1;
  }

  .create-card-text {
    font-size: 1.2rem;
    font-weight: 600;
  }

  /* ===== LISTA DE SESSÕES ===== */
  .sessions-list {
    margin-top: 10px;
  }

  .sessions-list-title {
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 6px;
    color: #0b3b70;
  }

  .sessions-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 4px;
    font-size: 0.9rem;
  }

  .sessions-table th,
  .sessions-table td {
    border: 1px solid #e5e7eb;
    padding: 8px 10px;
    text-align: left;
  }

  .sessions-table th {
    background: #e5f3ff;
    color: #0b3b70;
    font-weight: 600;
  }

  .sessions-table tr:nth-child(even) {
    background: #f9fafb;
  }

  .sessions-actions a {
    font-size: 0.8rem;
    color: #0b3b70;
    text-decoration: none;
  }

  .sessions-actions a:hover {
    text-decoration: underline;
  }

  .btn-inline-danger {
    border: none;
    background: transparent;
    color: #b91c1c;
    cursor: pointer;
    padding: 0;
    font-size: 0.8rem;
  }

  .btn-inline-danger:hover {
    text-decoration: underline;
  }
</style>

<div class="sessions-page">

  <!-- BARRA SUPERIOR -->
  <div class="stats-topbar">
    <div class="stats-topbar-left">
      <div class="stats-topbar-brand" onclick="window.location.href='/stats'">
        <img src="/static/img/logo_study_pequena.png" alt="Study Planner" class="stats-topbar-logo">
        <span class="stats-topbar-title">Study Planner</span>
      </div>

      <div class="stats-topbar-actions">
        <button type="button" class="stats-chip" onclick="window.location.href='/subjects'">
          Matérias
        </button>
        <button type="button" class="stats-chip" onclick="window.location.href='/sessions'">
          Sessões de estudo
        </button>
      </div>
    </div>

    <div class="stats-topbar-right">
      <button type="button" class="btn-logout" onclick="window.location.href='/logout'">
        Sair
      </button>
    </div>
  </div>

  <h2 class="page-title-main">Sessões de estudo</h2>

  <!-- BOTÃO VERDE CENTRAL -->
  <div class="create-card-wrapper">
    <a href="/sessions/new" class="create-card">
      <div class="create-card-icon">📘</div>
      <div class="create-card-text">Criar sessão</div>
    </a>
  </div>

  <!-- FILTROS (SE HOUVER) -->
  % if current_subject:
    <p>Filtrando por matéria: <strong>{{current_subject.name}}</strong></p>
  % end
  % if current_topic:
    <p>Filtrando por tópico: <strong>{{current_topic.title}}</strong></p>
  % end

  <!-- LISTA DE SESSÕES -->
  <section class="sessions-list">
    <h3 class="sessions-list-title">Lista de sessões</h3>

    % if not sessions:
      <p>Nenhuma sessão de estudo cadastrada ainda.</p>
    % else:
      <table class="sessions-table">
        <tr>
          <th>ID</th>
          <th>Data</th>
          <th>Duração (min)</th>
          <th>Matéria</th>
          <th>Tópico</th>
          <th>Notas</th>
          <th>Ações</th>
        </tr>
        % for s in sessions:
          <tr>
            <td>{{s.id}}</td>
            <td>{{s.date}}</td>
            <td>{{s.duration_minutes}}</td>
            <td>
              % if s.subject_id in subjects:
                {{subjects[s.subject_id].name}}
              % else:
                {{s.subject_id}}
              % end
            </td>
            <td>
              % if s.topic_id and s.topic_id in topics:
                {{topics[s.topic_id].title}}
              % elif s.topic_id:
                {{s.topic_id}}
              % else:
                -
              % end
            </td>
            <td>{{s.notes or ''}}</td>
            <td class="sessions-actions">
              <a href="/sessions/{{s.id}}/edit">Editar</a>
              |
              <form action="/sessions/{{s.id}}/delete"
                    method="post"
                    style="display:inline;">
                <button type="submit"
                        class="btn-inline-danger"
                        onclick="return confirm('Excluir esta sessão?');">
                  Excluir
                </button>
              </form>
            </td>
          </tr>
        % end
      </table>
    % end
  </section>

</div>
