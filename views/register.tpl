% rebase('layout', title='Register')

<h2>Create account</h2>

% if error:
  <p style="color: red;">{{error}}</p>
% end

<form action="/register" method="post">
  <div>
    <label for="username">Username</label><br>
    <input type="text" id="username" name="username" value="{{username or ''}}">
  </div>

  <div style="margin-top: 8px;">
    <label for="email">Email</label><br>
    <input type="email" id="email" name="email" value="{{email or ''}}">
  </div>

  <div style="margin-top: 8px;">
    <label for="password">Password</label><br>
    <input type="password" id="password" name="password">
  </div>

  <div style="margin-top: 12px;">
    <button type="submit">Create account</button>
  </div>

  <p style="margin-top: 12px;">
    Already have an account?
    <a href="/login">Login here</a>.
  </p>
</form>
