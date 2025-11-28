% rebase('layout', title='Topic form')

<h2>
  % if topic:
    Edit topic
  % else:
    New topic
  % end
  for subject: {{subject.name}}
</h2>

<form action="{{action}}" method="post">
  <div>
    <label for="title">Title</label><br>
    <input type="text"
           id="title"
           name="title"
           value="{{topic.title if topic else ''}}"
           required>
  </div>

  <div style="margin-top: 8px;">
    <label for="status">Status</label><br>
    <select id="status" name="status">
      % current = topic.status if topic else 'not_started'
      <option value="not_started" {{'selected' if current == 'not_started' else ''}}>Not started</option>
      <option value="in_progress" {{'selected' if current == 'in_progress' else ''}}>In progress</option>
      <option value="done" {{'selected' if current == 'done' else ''}}>Done</option>
    </select>
  </div>

  <div style="margin-top: 8px;">
    <label for="estimated_minutes">Estimated minutes</label><br>
    <input type="number"
           id="estimated_minutes"
           name="estimated_minutes"
           min="1"
           value="{{topic.estimated_minutes if topic else 60}}">
  </div>

  <div style="margin-top: 8px;">
    <label for="order">Order</label><br>
    <input type="number"
           id="order"
           name="order"
           min="1"
           value="{{topic.order if topic else 1}}">
  </div>

  <div style="margin-top: 12px;">
    <button type="submit">Save</button>
    <a href="/subjects/{{subject.id}}/topics">Cancel</a>
  </div>
</form>
