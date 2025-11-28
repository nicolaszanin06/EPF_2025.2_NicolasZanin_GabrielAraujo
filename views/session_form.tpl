% rebase('layout', title='Study session form')

<h2>
  % if session:
    Edit study session
  % else:
    New study session
  % end
</h2>

<form action="{{action}}" method="post">
  <input type="hidden" name="user_id" value="{{user_id}}">

  <div>
    <label for="subject_id">Subject</label><br>
    <select id="subject_id" name="subject_id" required>
      <option value="">-- select a subject --</option>
      % for subj in subjects:
        % selected = ''
        % if session and session.subject_id == subj.id:
            % selected = 'selected'
        % elif current_subject and current_subject.id == subj.id and (not session):
            % selected = 'selected'
        % end
        <option value="{{subj.id}}" {{selected}}>{{subj.name}}</option>
      % end
    </select>
  </div>

  <div style="margin-top: 8px;">
    <label for="topic_id">Topic (optional)</label><br>
    <select id="topic_id" name="topic_id">
      <option value="">-- no topic --</option>
      % for t in topics:
        % selected = ''
        % if session and session.topic_id == t.id:
            % selected = 'selected'
        % elif current_topic and current_topic.id == t.id and (not session):
            % selected = 'selected'
        % end
        <option value="{{t.id}}" {{selected}}>{{t.title}}</option>
      % end
    </select>
  </div>

  <div style="margin-top: 8px;">
    <label for="date">Date</label><br>
    <input type="date"
           id="date"
           name="date"
           value="{{session.date if session else ''}}"
           required>
  </div>

  <div style="margin-top: 8px;">
    <label for="duration_minutes">Duration (minutes)</label><br>
    <input type="number"
           id="duration_minutes"
           name="duration_minutes"
           min="1"
           value="{{session.duration_minutes if session else 60}}"
           required>
  </div>

  <div style="margin-top: 8px;">
    <label for="notes">Notes</label><br>
    <textarea id="notes"
              name="notes"
              rows="4"
              cols="40">{{session.notes if session else ''}}</textarea>
  </div>

  <div style="margin-top: 12px;">
    <button type="submit">Save</button>
    <a href="/sessions">Cancel</a>
  </div>
</form>
