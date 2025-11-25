% rebase('layout', title='Subject form')

<h2>{{ 'Edit subject' if subject else 'New subject' }}</h2>

<form action="{{action}}" method="post">
  <!-- Ideal: user_id vem da sessão; por enquanto vem do controller -->
  <input type="hidden" name="user_id" value="{{user_id}}">

  <div>
    <label for="name">Name</label><br>
    <input type="text"
           id="name"
           name="name"
           value="{{subject.name if subject else ''}}">
  </div>

  <div style="margin-top: 8px;">
    <label for="color">Color (hex)</label><br>
    <input type="text"
           id="color"
           name="color"
           placeholder="#FF0000"
           value="{{subject.color if subject else ''}}">
  </div>

  <div style="margin-top: 8px;">
    <label for="description">Description</label><br>
    <textarea id="description"
              name="description"
              rows="4"
              cols="40">{{subject.description if subject else ''}}</textarea>
  </div>

  <div style="margin-top: 12px;">
    <button type="submit">Save</button>
    <a href="/subjects">Cancel</a>
  </div>
</form>
