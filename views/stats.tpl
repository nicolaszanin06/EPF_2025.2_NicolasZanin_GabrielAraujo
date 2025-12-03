% rebase('layout', title='Estatísticas')

<style>
  /* Esconde o header padrão (Home / Subjects / ...) só nesta página */
  .main-header {
    display: none !important;
  }

  .stats-page {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  /* ===== BARRA VERDE SUPERIOR (LOGO + BOTÕES) ===== */
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

  /* ===== TÍTULO PRINCIPAL ===== */
  .stats-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #0b3b70;
    margin-bottom: 12px;
  }

  /* ===== CARTÕES “BRANCOS” PRINCIPAIS ===== */
  .stats-card-shell {
    background: #ffffff;
    border-radius: 12px;
    padding: 14px 16px;
    box-shadow: 0 1px 4px rgba(15,23,42,0.08);
    margin-bottom: 18px;
  }

  /* ===== FILTRO POR DATA ===== */
  .stats-filter-form {
    display: flex;
    gap: 12px;
    align-items: flex-end;
    flex-wrap: wrap;
  }

  .stats-filter-form label {
    font-size: 0.85rem;
    color: #374151;
  }

  .stats-filter-form input[type="date"] {
    padding: 6px 8px;
    border-radius: 8px;
    border: 1px solid #cbd5e1;
    font-size: 0.9rem;
  }

  .btn-primary {
    border: none;
    border-radius: 999px;
    padding: 7px 16px;
    font-size: 0.9rem;
    font-weight: 600;
    background: #0b3b70;
    color: #ffffff;
    cursor: pointer;
    transition: background 0.12s ease, transform 0.08s ease, box-shadow 0.08s ease;
  }

  .btn-primary:hover {
    background: #0a325f;
    transform: translateY(-1px);
    box-shadow: 0 3px 6px rgba(0,0,0,0.18);
  }

  .btn-link {
    border: none;
    background: none;
    color: #0b3b70;
    font-size: 0.85rem;
    cursor: pointer;
    text-decoration: underline;
    padding: 0;
  }

  /* ===== CARDS DE MÉTRICAS (4 BLOQUINHOS) ===== */
  .stats-card-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    margin-bottom: 20px;
  }

  .stats-card {
    flex: 1 1 220px;
    background: #ffffff;
    border-radius: 12px;
    padding: 14px 16px;
    box-shadow: 0 1px 4px rgba(15,23,42,0.08);
  }

  .stats-card h3 {
    font-size: 0.95rem;
    color: #4b5563;
    margin-bottom: 4px;
  }

  .stats-card-value {
    font-size: 1.5rem;
    font-weight: 700;
    color: #0b3b70;
  }

  .stats-card small {
    font-size: 0.8rem;
    color: #6b7280;
  }

  .stats-progress-track {
    background: #e5e7eb;
    height: 8px;
    border-radius: 999px;
    overflow: hidden;
    margin: 4px 0;
  }

  .stats-progress-bar {
    height: 100%;
    background: #16a34a;
  }

  /* ===== TEMPO POR MATÉRIA ===== */
  .stats-subjects-section h3 {
    margin-bottom: 8px;
    color: #0b3b70;
  }

  .stats-subject-row {
    margin-bottom: 8px;
  }

  .stats-subject-header {
    display: flex;
    justify-content: space-between;
    font-size: 0.9rem;
  }

  .stats-subject-bar-track {
    background: #e5e7eb;
    height: 10px;
    border-radius: 999px;
    overflow: hidden;
    margin-top: 4px;
  }

  .stats-subject-bar {
    height: 100%;
    background: #2563eb;
  }

  /* ===== RESUMO ===== */
  .stats-summary-card h3 {
    margin-bottom: 8px;
    color: #0b3b70;
  }

  /* ===== EXPORTAÇÃO ===== */
  .stats-export-card h3 {
    margin-bottom: 6px;
    color: #0b3b70;
  }

  .stats-export-card ul {
    margin-top: 4px;
    padding-left: 18px;
  }

  .stats-export-card a {
    font-size: 0.9rem;
  }
</style>

<div class="stats-page">

  <!-- BARRA VERDE COM LOGO + BOTÕES -->
  <div class="stats-topbar">
    <div class="stats-topbar-left">
      <div class="stats-topbar-brand" onclick="window.location.href='/stats'">
        <img src="/static/img/logo_study_pequena.png" alt="Study Planner" class="stats-topbar-logo">
        <span class="stats-topbar-title"></span>
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

  <h2 class="stats-title">Estatísticas de estudo</h2>

  <!-- FILTRO POR PERÍODO -->
  <section class="stats-card-shell">
    <form method="get" action="/stats" class="stats-filter-form">
      <div>
        <label for="start_date">Data inicial:</label><br>
        <input type="date"
               id="start_date"
               name="start_date"
               value="{{stats['start_date']}}">
      </div>
      <div>
        <label for="end_date">Data final:</label><br>
        <input type="date"
               id="end_date"
               name="end_date"
               value="{{stats['end_date']}}">
      </div>
      <div>
        <button type="submit" class="btn-primary" style="margin-top: 2px;">
          Aplicar filtro
        </button>
      </div>
      % if stats['start_date'] or stats['end_date']:
        <div>
          <button type="button"
                  class="btn-link"
                  style="margin-top: 6px;"
                  onclick="window.location.href='/stats'">
            Limpar filtro
          </button>
        </div>
      % end
    </form>
  </section>

  <!-- CARDS PRINCIPAIS -->
  <section class="stats-card-grid">

    <div class="stats-card">
      <h3>Total de horas</h3>
      <p class="stats-card-value">
        {{stats['total_hours']}} h
      </p>
      <small>{{stats['total_minutes']}} minutos estudados</small>
    </div>

    <div class="stats-card">
      <h3>Sessões</h3>
      <p class="stats-card-value">
        {{stats['sessions_count']}}
      </p>
      <small>no período selecionado</small>
    </div>

    <div class="stats-card">
      <h3>Matérias</h3>
      <p class="stats-card-value">
        {{stats['subjects_count']}}
      </p>
      <small>registradas para este usuário</small>
    </div>

    <div class="stats-card">
      <h3>Tópicos concluídos</h3>
      <p class="stats-card-value">
        {{stats['topics_completed']}} / {{stats['topics_total']}}
      </p>
      % if stats['topics_total'] > 0:
        % completed_pct = int((stats['topics_completed'] / stats['topics_total']) * 100)
      % else:
        % completed_pct = 0
      % end
      <div class="stats-progress-track">
        <div class="stats-progress-bar" style="width: {{completed_pct}}%;"></div>
      </div>
      <small>{{completed_pct}}% concluído</small>
    </div>

  </section>

  <!-- BARRAS POR MATÉRIA -->
  <section class="stats-card-shell stats-subjects-section">
    <h3>Tempo de estudo por matéria</h3>

    % minutes_per_subject = stats['minutes_per_subject']
    % if not minutes_per_subject:
      <p>Nenhuma sessão de estudo encontrada para este período.</p>
    % else:
      % max_minutes = max(minutes_per_subject.values()) if minutes_per_subject else 0

      <div style="margin-top: 8px;">
        % for subj in subjects:
          % subj_minutes = minutes_per_subject.get(subj.id, 0)
          % if max_minutes > 0:
            % width_pct = int((subj_minutes / max_minutes) * 100)
          % else:
            % width_pct = 0
          % end

          <div class="stats-subject-row">
            <div class="stats-subject-header">
              <strong>{{subj.name}}</strong>
              <span>{{subj_minutes}} min</span>
            </div>
            <div class="stats-subject-bar-track">
              <div class="stats-subject-bar" style="width: {{width_pct}}%;"></div>
            </div>
          </div>
        % end
      </div>
    % end
  </section>

  <!-- RESUMO TEXTUAL -->
  <section class="stats-card-shell stats-summary-card">
    <h3>Resumo</h3>
    % if stats['sessions_count'] == 0:
      <p>Nenhuma sessão de estudo foi encontrada para o período selecionado.</p>
    % else:
      <p>
        Você estudou um total de <strong>{{stats['total_hours']}} horas</strong>
        ({{stats['total_minutes']}} minutos) em
        <strong>{{stats['sessions_count']}} sessões</strong>.
      </p>
      % if stats['topics_total'] > 0:
        <p>
          De {{stats['topics_total']}} tópicos,
          <strong>{{stats['topics_completed']}}</strong> estão marcados como concluídos.
        </p>
      % end
    % end
  </section>

  <!-- EXPORTAÇÃO -->
  <section class="stats-card-shell stats-export-card">
    <h3>Exportar dados</h3>
    <ul>
      <li><a href="/export/full.json">Baixar todos os dados (JSON)</a></li>
      <li><a href="/export/sessions.csv">Baixar sessões de estudo (CSV)</a></li>
      <li><a href="/export/subjects.csv">Baixar matérias (CSV)</a></li>
      <li><a href="/export/topics.csv">Baixar tópicos (CSV)</a></li>
    </ul>
  </section>

</div>