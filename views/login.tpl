% rebase('layout', title='Login')

<h2>Login</h2>

% if error:
  <p style="color: red;">{{error}}</p>
% end

<form action="/login" method="post">
  <div>
    <label for="username">Username</label><br>
    <input type="text" id="username" name="username" value="{{username or ''}}">
  </div>

  <div style="margin-top: 8px;">
    <label for="password">Password</label><br>
    <input type="password" id="password" name="password">
  </div>

  <div style="margin-top: 12px;">
    <button type="submit">Login</button>
  </div>

  <p style="margin-top: 12px;">
    Don't have an account?
    <a href="/register">Register here</a>.
  </p>
</form>
