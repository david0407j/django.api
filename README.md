# django.api
"API para gerenciamento de usuários, desenvolvida com Django REST Framework. Permite criar, atualizar, listar e excluir usuários, com autenticação JWT para segurança. Inclui endpoints para recuperação de senha e verificação de e-mail."

Projeto: API com Django e Poetry
Este projeto é uma aplicação desenvolvida com Django, utilizando o Poetry para gerenciamento de dependências e ambiente virtual. Ele demonstra a criação e consumo de APIs para manipular dados de forma eficiente e escalável.

🚀 Funcionalidades
📡 Exposição de APIs RESTful.
🔍 Suporte a operações CRUD (Create, Read, Update, Delete).
📂 Estrutura modular para adicionar novos endpoints facilmente.
🛠️ Documentação automática de API com Swagger ou Redoc.
🛡️ Autenticação e autorização básica para proteger endpoints.
🔗 Integração com APIs externas (se necessário).
🛠️ Tecnologias Utilizadas
Python 3.9+
Django 4.2+
Django REST Framework (DRF)
Poetry para gerenciamento de dependências.
PostgreSQL (ou outro banco de dados à sua escolha).
🏗️ Configuração do Ambiente
1. Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas:

Python 3.9+
Poetry
Banco de Dados PostgreSQL (ou outro configurado no settings.py)
2. Clone o repositório
bash
Copiar código
git clone https://github.com/david0407j/django.api.git
cd seuprojeto
3. Configuração do ambiente virtual com Poetry
Crie e ative o ambiente virtual:

bash
Copiar código
poetry install
poetry shell
4. Configuração do banco de dados
Atualize o arquivo .env com as variáveis de ambiente do banco de dados:

env
Copiar código
POSTGRES_DB=seubanco
POSTGRES_USER=seuusuario
POSTGRES_PASSWORD=suasenha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
5. Execute as migrações
bash
Copiar código
python manage.py migrate
6. Crie um superusuário
bash
Copiar código
python manage.py createsuperuser
7. Inicie o servidor de desenvolvimento
bash
Copiar código
python manage.py runserver
📖 Documentação da API
A documentação da API pode ser acessada em:

🌟 Testes
Executar os testes automatizados:
bash
Copiar código
python manage.py test
Análise de código com Flake8:
bash
Copiar código
poetry run flake8 .
🏗️ Estrutura do Projeto
markdown
Copiar código
├── manage.py
├── pyproject.toml
├── README.md
├── .env
├── .flake8
├── api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
🤝 Contribuição
Contribuições são sempre bem-vindas! Para contribuir:

Faça um fork do projeto.
Crie sua branch de funcionalidade: git checkout -b minha-feature.
Envie suas mudanças: git push origin minha-feature.
Abra um pull request.
📄 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

📞 Contato
Davidson Junio
📍 Belo Horizonte, MG - Brasil
✉️ Email: djunio239@gmail.com


