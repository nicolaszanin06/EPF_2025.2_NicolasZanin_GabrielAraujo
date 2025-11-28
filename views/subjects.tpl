% rebase('layout', title='Subjects')

<h2>Subjects</h2>

<div style="margin-bottom: 12px;">
  <a href="/subjects/new">+ New subject</a>
</div>

% if not subjects:
  <p>No subjects registered yet.</p>
% else:
  <table border="1" cellpadding="6" cellspacing="0">
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>Color</th>
      <th>Description</th>
      <th>Actions</th>
    </tr>
    % for subject in subjects:
      <tr>
        <td>{{subject.id}}</td>
        <td>{{subject.name}}</td>
        <td>
          % if subject.color:
            <span style="display:inline-block;width:16px;height:16px;
                         background-color: {{subject.color}};border:1px solid #000;
                         vertical-align: middle;"></span>
            <span>{{subject.color}}</span>
          % else:
            -
          % end
        </td>
        <td>{{subject.description or ''}}</td>
        <td>
          <!-- editar / apagar -->
          <a href="/subjects/{{subject.id}}/edit">Edit</a>
          |
          <form action="/subjects/{{subject.id}}/delete"
                method="post"
                style="display:inline;">
            <button type="submit"
                    onclick="return confirm('Delete this subject?');">
              Delete
            </button>
          </form>
          |
          <!-- NOVO: ver tópicos da matéria -->
          <a href="/subjects/{{subject.id}}/topics">Topics</a>
          |
          <!-- OPCIONAL: ver sessões da matéria -->
          <a href="/subjects/{{subject.id}}/sessions">Sessions</a>
        </td>
      </tr>
    % end
  </table>
% end
