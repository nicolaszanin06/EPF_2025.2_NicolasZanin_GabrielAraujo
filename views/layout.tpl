<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title or 'Study Planner'}}</title>

    <link rel="stylesheet" href="/static/css/style.css" />
</head>

<body>

    <!-- HEADER / NAVBAR -->
    <header style="background:#222; padding:12px;">
        <nav style="display:flex; gap:16px; align-items:center;">
            <a href="/" style="color:white; text-decoration:none;">Home</a>
            <a href="/subjects" style="color:white; text-decoration:none;">Subjects</a>
            <a href="/sessions" style="color:white; text-decoration:none;">Study Sessions</a>
            <a href="/stats" style="color:white; text-decoration:none;">Statistics</a>

            <!-- Login / Logout: será melhorado depois quando tiver session -->
            <span style="flex:1;"></span>

            <a href="/login" style="color:white; text-decoration:none;">Login</a>
            <a href="/register" style="color:white; text-decoration:none; margin-left:8px;">Register</a>
            <a href="/logout" style="color:white; text-decoration:none; margin-left:8px;">Logout</a>
        </nav>
    </header>

    <!-- MAIN CONTENT -->
    <main class="container" style="padding: 20px;">
        {{!base}}
    </main>

    <!-- FOOTER -->
    <footer style="text-align:center; padding:15px; margin-top:40px; color:#555;">
        <p>&copy; 2025 Study Planner. All rights reserved.</p>
    </footer>

    <script src="/static/js/main.js"></script>

</body>
</html>
