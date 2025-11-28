% rebase('layout', title='Study sessions')

<h2>Study sessions</h2>

% if current_subject:
  <p>Filtering by subject: <strong>{{current_subject.name}}</strong></p>
% end
% if current_topic:
  <p>Filtering by topic: <strong>{{current_topic.title}}</strong></p>
% end

<p>
  <a href="/sessions/new">+ New session</a>
</p>

% if not sessions:
  <p>No study sessions registered yet.</p>
% else:
  <table border="1" cellpadding="4" cellspacing="0">
    <tr>
      <th>ID</th>
      <th>Date</th>
      <th>Duration (min)</th>
      <th>Subject</th>
      <th>Topic</th>
      <th>Notes</th>
      <th>Actions</th>
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
        <td>
          <a href="/sessions/{{s.id}}/edit">Edit</a>
          |
          <form action="/sessions/{{s.id}}/delete"
                method="post"
                style="display:inline;">
            <button type="submit" onclick="return confirm('Delete this session?');">
              Delete
            </button>
          </form>
        </td>
      </tr>
    % end
  </table>
% end
