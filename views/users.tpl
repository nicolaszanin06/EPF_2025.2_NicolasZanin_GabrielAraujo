% rebase('layout', title='Usuários')

<section class="page-section">
  <div class="page-header">
    <div>
      <h1 class="page-title">Usuários do sistema</h1>
      <p class="page-subtitle">
        Apenas administradores podem visualizar e gerenciar usuários.
      </p>
    </div>

    <div class="page-header-actions">
      <a href="/users/add" class="btn-primary big">
        + Novo usuário
      </a>
    </div>
  </div>

  % if not users:
    <p>Nenhum usuário cadastrado ainda.</p>
  % else:
    <div class="card-table">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Usuário</th>
            <th>E-mail</th>
            <th>Papel</th>
            <th style="width: 150px;">Ações</th>
          </tr>
        </thead>
        <tbody>
          % for u in users:
            <tr>
              <td>{{u.id}}</td>
              <td>{{u.name or ''}}</td>
              <td>{{u.username}}</td>
              <td>{{u.email or ''}}</td>
              <td>
                % if u.role == 'admin':
                  Admin
                % else:
                  Usuário
                % end
              </td>
              <td>
                <a href="/users/edit/{{u.id}}" class="btn-secondary btn-table">
                  Editar
                </a>
                <form action="/users/delete/{{u.id}}" method="post" style="display:inline;">
                  <button type="submit"
                          class="btn-danger btn-table"
                          onclick="return confirm('Confirmar exclusão deste usuário?');">
                    Excluir
                  </button>
                </form>
              </td>
            </tr>
          % end
        </tbody>
      </table>
    </div>
  % end
</section>
