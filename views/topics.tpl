% rebase('layout', title='Topics')

<h2>Topics for {{subject.name}}</h2>

<p>
  <a href="/subjects">← Back to subjects</a>
</p>

<p>
  <a href="/subjects/{{subject.id}}/topics/new">+ New topic</a>
</p>

% if not topics:
  <p>No topics registered yet.</p>
% else:
  <table border="1" cellpadding="4" cellspacing="0">
    <tr>
      <th>ID</th>
      <th>Title</th>
      <th>Status</th>
      <th>Estimated minutes</th>
      <th>Order</th>
      <th>Actions</th>
    </tr>
    % for t in topics:
      <tr>
        <td>{{t.id}}</td>
        <td>{{t.title}}</td>
        <td>{{t.status}}</td>
        <td>{{t.estimated_minutes}}</td>
        <td>{{t.order}}</td>
        <td>
          <a href="/subjects/{{subject.id}}/topics/{{t.id}}/edit">Edit</a>
          |
          <form action="/subjects/{{subject.id}}/topics/{{t.id}}/delete"
                method="post"
                style="display:inline;">
            <button type="submit"
                    onclick="return confirm('Delete this topic?');">
              Delete
            </button>
          </form>
        </td>
      </tr>
    % end
  </table>
% end
