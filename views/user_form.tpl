% rebase('layout', title='User Form')

<section class="form-section">
    <h1>{{'Edit User' if user else 'Add User'}}</h1>
    
    <form action="{{action}}" method="post" class="form-container">

        <!-- USERNAME -->
        <div class="form-group">
            <label for="username">Username:</label>
            <input type="text"
                   id="username"
                   name="username"
                   required
                   value="{{user.username if user else ''}}">
        </div>
        
        <!-- EMAIL -->
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email"
                   id="email"
                   name="email"
                   required
                   value="{{user.email if user else ''}}">
        </div>
        
        <!-- PASSWORD -->
        <div class="form-group">
            <label for="password">Password:</label>
            <input type="password"
                   id="password"
                   name="password"
                   % if user:
                       placeholder="Leave blank to keep current password"
                   % else:
                       required
                   % end
            >
        </div>

        <!-- ROLE (opcional, aqui estou fixando como 'user' se não houver) -->
        <input type="hidden"
               name="role"
               value="{{user.role if user else 'user'}}">

        <div class="form-actions">
            <button type="submit" class="btn-submit">Save</button>
            <a href="/users" class="btn-cancel">Back</a>
        </div>
    </form>
</section>
