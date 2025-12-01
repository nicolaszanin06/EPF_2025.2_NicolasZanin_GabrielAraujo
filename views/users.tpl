% rebase('layout', title='Users')

<h2>Usuários</h2>

<div style="margin-bottom: 12px;">
  <a href="/users/add">+ New user</a>
</div>

% if not users:
  <p>No users registered yet.</p>
% else:
  <table border="1" cellpadding="6" cellspacing="0">
    <tr>
      <th>ID</th>
      <th>Usuário</th>
      <th>Email</th>
      <th>Tipo</th>
      <th>Ações</th>
    </tr>
    % for user in users:
      <tr>
        <td>{{user.id}}</td>
        <td>{{user.username}}</td>
        <td>{{user.email}}</td>
        <td>{{user.role}}</td>
        <td>
          <a href="/users/edit/{{user.id}}">Edit</a>
          |
          <form action="/users/delete/{{user.id}}"
                method="post"
                style="display:inline;">
            <button type="submit"
                    onclick="return confirm('Delete this user?');">
              Delete
            </button>
          </form>
        </td>
      </tr>
    % end
  </table>
% end
