`markdown
# Study Planner UnB – Planejador de Estudos em Python + Bottle

Este projeto foi desenvolvido por dois colegas, **Gabriel** e **Nicolas**, alunos da Universidade de Brasília (UnB), que buscaram construir uma aplicação web de planejamento de estudos que pudesse ser utilizada futuramente por outros estudantes da UnB em seus estudos pessoais, de forma mais **personalizada**, **organizada** e com a **“carinha UnB”** (layout inspirado nas cores e identidade visual da universidade).

A aplicação foi construída em **Python**, utilizando o microframework **Bottle** e arquivos **JSON** para persistência dos dados, seguindo uma arquitetura simples e didática, adequada para disciplinas de **Programação Orientada a Objetos (POO)** e projetos educacionais.

---

## 💡 Objetivo

O objetivo do **Study Planner UnB** é oferecer a estudantes uma ferramenta web para:

- Organizar **matérias/disciplinas** e **tópicos de estudo**  
- Registrar e acompanhar **sessões de estudo**  
- Visualizar **estatísticas** (por exemplo, tempo total estudado por matéria)  
- Manter tudo em um ambiente simples, acessível via navegador e com visual alinhado às cores da UnB

Além disso, o projeto serve como exemplo prático de:

- Uso de **POO em Python**  
- Organização em **camadas** (models, services, controllers, views)  
- Persistência de dados em **JSON**  
- Desenvolvimento de aplicações **web educacionais** com Bottle  

---

## 🗂 Estrutura de Pastas

bash
study-planner-unb/
├── app.py                 # Ponto de entrada / inicialização Bottle (opcional, dependendo da seu projeto)
├── config.py              # Configurações e caminhos do projeto
├── main.py                # Arquivo principal para subir a aplicação
├── requirements.txt       # Dependências do projeto
├── README.md              # Este arquivo
├── controllers/           # Controladores e rotas da aplicação
├── models/                # Definição das entidades de domínio (User, Subject, StudySession, etc.)
├── services/              # Camada de serviços e persistência (JSON)
├── views/                 # Templates .tpl (HTML usando Bottle)
├── static/                # CSS, JS, imagens e assets visuais
└── data/                  # Arquivos .json com os dados da aplicação
`

> **Obs.:** Ajuste os nomes dos arquivos/pastas acima conforme a estrutura real do seu projeto.

---

## 📁 Descrição das Pastas

### `controllers/`

Contém as classes responsáveis por lidar com as **rotas** e orquestrar a lógica entre models, services e views. Exemplos (ajuste conforme o seu projeto):

* `user_controller.py` – rotas de usuários (login, cadastro, listagem)
* `subject_controller.py` – CRUD de matérias/disciplinas
* `session_controller.py` – criação e gerenciamento de sessões de estudo
* `stats_controller.py` – rotas para visualização de estatísticas
* `base_controller.py` – lógica compartilhada (render, redirect, rotas básicas)

---

### `models/`

Define as classes que representam as **entidades de domínio** da aplicação. Exemplos:

* `user.py` – classe `User`, representando o estudante que utiliza o sistema
* `subject.py` – classe `Subject`, com atributos como `id`, `nome`, `cor`, `descrição`
* `topic.py` ou `topico.py` – representa tópicos dentro de uma matéria
* `study_session.py` – classe `StudySession`, registrando data, duração, matéria, tipo de estudo etc.

---

### `services/`

Responsável pela **persistência** e manipulação dos dados em arquivos JSON. Exemplos:

* `json_repository.py` ou serviços específicos (`user_service.py`, `subject_service.py` etc.)
* Métodos típicos: `get_all`, `get_by_id`, `add`, `update`, `delete`, `save`

Essa camada abstrai o acesso aos arquivos da pasta `data/`, facilitando testes e manutenção.

---

### `views/`

Contém os arquivos `.tpl` usados pelo Bottle para renderizar as páginas HTML. Exemplos:

* `layout.tpl` – layout base com cabeçalho, menu e bloco de conteúdo
* `login.tpl` – página de login do usuário
* `subjects.tpl` – listagem de matérias com botão **“Criar matéria”**
* `subject_form.tpl` – formulário para criar/editar matéria
* `sessions.tpl` – listagem e criação de sessões de estudo
* `stats.tpl` – dashboard com estatísticas de estudo (tempo total, por matéria, etc.)

As views utilizam o visual com **cores verde e azul escuro**, remetendo à identidade da UnB.

---

### `static/`

Arquivos estáticos, como:

* `css/style.css` – estilos da aplicação (cores, fontes, botões arredondados etc.)
* `js/main.js` – scripts JS opcionais (interações de UI)
* `img/` – logo do Study Planner, ícones, imagens usadas no layout

---

### `data/`

Armazena os arquivos **JSON** que funcionam como o “banco de dados” do projeto:

* `users.json` – dados de usuários cadastrados
* `subjects.json` – matérias/disciplinas
* `sessions.json` – sessões de estudo registradas
* Outros arquivos que o grupo julgar necessários

---

## ▶ Como Executar

1. **Criar ambiente virtual** (recomendado fazer fora da pasta do projeto):

bash
python -m venv venv

# Ativar o ambiente virtual
# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate


2. **Instalar as dependências** dentro da pasta do projeto:

bash
pip install -r requirements.txt


3. **Rodar a aplicação**:

bash
python main.py


4. **Acessar no navegador**:

Abra: [http://localhost:8080](http://localhost:8080)

(A porta pode ser diferente se você tiver configurado outro valor no `main.py`.)

---

## 🎯 Funcionalidades Principais

* Cadastro e gerenciamento de **usuários**
* Gestão de **matérias/disciplinas** com cores personalizadas
* Registro de **tópicos** associados às matérias
* Criação de **sessões de estudo** com data, duração, tipo de estudo etc.
* Página de **estatísticas** para acompanhar o progresso
* Interface simples em **Bottle**, com visual inspirado na **UnB**

---

## ✍ Personalização

Para adaptar o projeto a novas necessidades (por exemplo, outros cursos, tipos de atividades ou métricas):

1. Criar ou alterar as classes no diretório **`models/`**.
2. Atualizar/estender os **services** responsáveis pelos arquivos JSON em **`services/`**.
3. Adicionar novas rotas e lógicas nos **controllers**.
4. Criar ou modificar templates `.tpl` em **`views/`** para refletir novas telas.
5. Ajustar o visual no **`static/css/style.css`**, mantendo ou evoluindo a “carinha UnB”.

---

## 🧠 Autores e Licença

Projeto desenvolvido por:

* **Gabriel Araujo**
* **Nicolas Zanin**

como trabalho acadêmico na **Universidade de Brasília (UnB)**, com fins didáticos e de apoio aos estudos de outros alunos.

Você pode **reutilizar**, **modificar** e **compartilhar** este projeto livremente para fins educacionais.
Caso use como base para outro trabalho ou projeto, recomenda-se creditar os autores e a Universidade de Brasília.


```