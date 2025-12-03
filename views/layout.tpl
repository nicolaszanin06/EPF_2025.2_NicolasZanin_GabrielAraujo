<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title or 'Study Planner'}}</title>
    <link rel="stylesheet" href="/static/css/style.css" />
</head>

% hide_header = locals().get('hide_header', False)

<body class="{{'auth-page' if hide_header else ''}}">

    % if not hide_header:
    <header class="main-header">
        <div class="logo">Study Planner</div>

        <nav class="main-nav">
            <a href="/stats">Estatísticas</a>
            <a href="/subjects">Matérias</a>
            <a href="/sessions">Sessões de estudo</a>

            % if is_admin:
                <a href="/users">Usuários</a>
            % end

            <a href="/logout">Sair</a>
        </nav>
    </header>
    % end

    <main class="main-container">
        <div class="content">
            {{!base}}
        </div>
    </main>

    <footer class="main-footer">
        <p>&copy; 2025, Study Planner. Todos os direitos reservados.</p>
    </footer>

</body>
</html>
