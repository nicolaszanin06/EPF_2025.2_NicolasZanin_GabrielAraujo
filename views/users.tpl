% rebase('layout', title='Usuários')

<style>
    .main-header { display: none !important; }

    .users-page {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* ===== BARRA VERDE SUPERIOR ===== */
    .users-topbar {
        background: linear-gradient(90deg, #002F54 0%, #005F3B 100%);
        padding: 12px 20px;
        border-radius: 10px;
        margin-bottom: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .users-topbar-left {
        display: flex;
        align-items: center;
        gap: 16px;
    }

    .users-logo {
        height: 60px;
        cursor: pointer;
    }

    .users-nav-buttons {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .chip-btn {
        background: #fff;
        color: #002F54;
        border-radius: 999px;
        padding: 6px 16px;
        font-weight: 600;
        cursor: pointer;
        border: none;
        box-shadow: 0 1px 3px rgba(0,0,0,0.15);
        transition: 0.15s ease;
    }

    .chip-btn:hover {
        background: #eef9f2;
        transform: translateY(-2px);
    }

    .users-topbar-right {
        display: flex;
        align-items: center;
    }

    .logout-btn {
        background: #fff;
        color: #b91c1c;
        border-radius: 999px;
        padding: 6px 18px;
        font-weight: 600;
        border: none;
        cursor: pointer;
        box-shadow: 0 1px 3px rgba(0,0,0,0.15);
    }

    .logout-btn:hover {
        background: #ffe5e5;
    }

    /* ===== CONTEÚDO ===== */
    .users-title {
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 16px;
        color: #0b3b70;
    }

    .users-card {
        background: #fff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 1px 4px rgba(15,23,42,0.08);
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 16px;
        font-size: 0.95rem;
    }

    th {
        background: #f0f4f8;
        padding: 10px;
        text-align: left;
        font-weight: 600;
    }

    td {
        padding: 10px;
        border-top: 1px solid #e2e8f0;
    }

    .delete-btn {
        background: #002F54;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 4px 12px;
        cursor: pointer;
        font-size: 0.85rem;
        font-weight: 600;
    }

    .delete-btn:hover {
        opacity: 0.85;
    }

    .edit-link {
        color: #005F3B;
        font-weight: 600;
        text-decoration: none;
        margin-right: 8px;
    }

    .edit-link:hover {
        text-decoration: underline;
    }

</style>

<div class="users-page">

    <!-- BARRA SUPERIOR -->
    <div class="users-topbar">
        <div class="users-topbar-left">
            <img src="/static/img/logo_study_pequena.png"
                 class="users-logo"
                 onclick="window.location.href='/stats'">

            <div class="users-nav-buttons">
                <button class="chip-btn" onclick="window.location.href='/subjects'">Matérias</button>
                <button class="chip-btn" onclick="window.location.href='/sessions'">Sessões de estudo</button>
                <button class="chip-btn" onclick="window.location.href='/users'">Usuários</button>
            </div>
        </div>

        <div class="users-topbar-right">
            <button class="logout-btn" onclick="window.location.href='/logout'">Sair</button>
        </div>
    </div>

    <!-- CONTEÚDO -->
    <div class="users-card">

        <h2 class="users-title">Usuários</h2>

        <div style="margin-bottom: 12px;">
            <a href="/users/add" style="font-weight:600;">+ New user</a>
        </div>

        % if not users:
            <p>Nenhum usuário encontrado.</p>
        % else:
            <table>
                <tr>
                    <th>ID</th>
                    <th>Usuário</th>
                    <th>Email</th>
                    <th>Tipo</th>
                    <th>Ações</th>
                </tr>

                % for u in users:
                    <tr>
                        <td>{{u.id}}</td>
                        <td>{{u.username}}</td>
                        <td>{{u.email}}</td>
                        <td>{{u.role}}</td>
                        <td>
                            <a class="edit-link" href="/users/edit/{{u.id}}">Editar</a>

                            <form method="post"
                                  action="/users/delete/{{u.id}}"
                                  style="display:inline;">
                                <button type="submit"
                                        class="delete-btn"
                                        onclick="return confirm('Apagar esse usuário?');">
                                    Apagar
                                </button>
                            </form>
                        </td>
                    </tr>
                % end
            </table>
        % end

    </div>

</div>
