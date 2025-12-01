% rebase('layout', title='Tópicos')

<style>
  .main-header { display:none !important; }

  .topics-page {
    font-family:'Segoe UI', Tahoma, sans-serif;
  }

  /* ===== BARRA SUPERIOR ===== */
  .stats-topbar {
    background: linear-gradient(90deg, #002F54 0%, #005F3B 100%);
    padding: 10px 18px;
    border-radius: 10px;
    margin-bottom: 20px;
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
    font-size:0.9rem;
    font-weight:600;
    background:#ffffff;
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
    font-size:0.9rem;
    font-weight:600;
    background:#ffffff;
    color:#b91c1c;
    cursor:pointer;
    box-shadow:0 1px 3px rgba(0,0,0,0.15);
  }

  .btn-logout:hover {
    background:#fee2e2;
  }

  /* ===== TÍTULO + CARD VERDE ===== */
  .page-title {
    font-size:1.5rem;
    font-weight:700;
    color:#0b3b70;
    margin-bottom:8px;
  }

  .page-subtitle {
    font-size:0.95rem;
    color:#4b5563;
    margin-bottom:18px;
  }

  .create-card-wrapper {
    display:flex;
    justify-content:center;
    margin:18px 0 16px;
  }

  .create-card {
    width:260px;
    height:200px;
    background:#005F3B;
    border-radius:18px;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    gap:8px;
    text-decoration:none;
    color:#ffffff;
    box-shadow:0 10px 28px rgba(0,0,0,0.26);
    transition:transform 0.12s ease, box-shadow 0.12s ease, background 0.12s ease;
  }

  .create-card:hover {
    background:#007749;
    transform:translateY(-3px);
    box-shadow:0 16px 40px rgba(0,0,0,0.3);
  }

  .create-card-icon {
    font-size:2.4rem;
  }

  .create-card-text {
    font-size:1.1rem;
    font-weight:600;
  }

  /* ===== TABELA ===== */
  .topics-list {
    margin-top:10px;
  }

  .topics-list-title {
    font-size:1.05rem;
    font-weight:600;
    color:#0b3b70;
    margin-bottom:6px;
  }

  .topics-table {
    width:100%;
    border-collapse:collapse;
    font-size:0.9rem;
  }

  .topics-table th,
  .topics-table td {
    border:1px solid #e5e7eb;
    padding:8px 10px;
    text-align:left;
  }

  .topics-table th {
    background:#e5f3ff;
    color:#0b3b70;
    font-weight:600;
  }

  .topics-table tr:nth-child(even) {
    background:#f9fafb;
  }

  .topics-actions a {
    font-size:0.8rem;
    color:#0b3b70;
    text-decoration:none;
  }

  .topics-actions a:hover {
    text-decoration:underline;
  }

  .btn-inline-danger {
    border:none;
    background:transparent;
    color:#b91c1c;
    cursor:pointer;
    padding:0;
    font-size:0.8rem;
  }

  .btn-inline-danger:hover {
    text-decoration:underline;
  }
</style>

<div class="topics-page">

  <!-- BARRA SUPERIOR -->
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

  <h2 class="page-title">Tópicos</h2>
  <p class="page-subtitle">
    Matéria: <strong>{{subject.name}}</strong>
  </p>

  <!-- BOTÃOZÃO VERDE -->
  <div class="create-card-wrapper">
    <!-- Se sua rota for diferente, só trocar o href -->
    <a href="/subjects/{{subject.id}}/topics/new" class="create-card">
      <div class="create-card-icon">📚</div>
      <div class="create-card-text">Criar tópico</div>
    </a>
  </div>

  <!-- LISTA -->
  <section class="topics-list">
    <h3 class="topics-list-title">Lista de tópicos</h3>

    % if not topics:
      <p>Nenhum tópico cadastrado ainda.</p>
    % else:
 <table class="topics-table">
  <tr>
    <th>ID</th>
    <th>Título</th>
    <th>Status</th>
    <th>Ações</th>
  </tr>
  % for t in topics:
    <tr>
      <td>{{t.id}}</td>
      <td>{{t.title}}</td>

      <!-- status visual -->
      <td>
        % if t.status == 'completed':
          <span class="status-pill status-done">Concluído</span>
        % else:
          <span class="status-pill status-pending">Pendente</span>
        % end
      </td>

      <td class="topics-actions">
        <!-- botão de marcar/desfazer -->
        <form action="/subjects/{{subject.id}}/topics/{{t.id}}/toggle"
              method="post"
              style="display:inline;">
          % if t.status == 'completed':
            <button type="submit" class="btn-chip done">
              ✔ Desfazer
            </button>
          % else:
            <button type="submit" class="btn-chip">
              Marcar como concluído
            </button>
          % end
        </form>

        |
        <a href="/subjects/{{subject.id}}/topics/{{t.id}}/edit">Editar</a>
        |
        <form action="/subjects/{{subject.id}}/topics/{{t.id}}/delete"
              method="post"
              style="display:inline;">
          <button type="submit"
                  class="btn-inline-danger"
                  onclick="return confirm('Excluir este tópico?');">
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
