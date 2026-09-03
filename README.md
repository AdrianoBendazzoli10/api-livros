API de Livros
API REST desenvolvida em Python com FastAPI, com o objetivo de realizar o gerenciamento de livros utilizando MySQL como banco de dados.

O projeto foi desenvolvido de forma incremental, abordando desde a configuração do ambiente e conexão com o banco de dados até a implementação das operações CRUD e, posteriormente, uma interface web para consumo da API.

🚀 Tecnologias
Python 3.11+
FastAPI — criação da API REST
Uvicorn — servidor da aplicação
SQLAlchemy — ORM e comunicação com o banco
PyMySQL — conexão com o MySQL
Pydantic Settings — gerenciamento das configurações
MySQL — banco de dados relacional
HTML, CSS e JavaScript — interface web
📖 Funcionalidades
A API permite o gerenciamento de livros, contendo informações como:

ID
Título
Autor
Ano de publicação
Disponibilidade
As principais operações da API são:

POST /livros — cadastrar um livro
GET /livros — listar livros
GET /livros/{id} — consultar um livro específico
PUT /livros/{id} — atualizar um livro
DELETE /livros/{id} — excluir um livro
GET /health — verificar o funcionamento da API e a conexão com o banco
🗂️ Estrutura do projeto
api-livros/
├── app/
│   ├── __init__.py
│   ├── database.py
│   └── main.py
├── database/
│   └── biblioteca_db.sql
├── .env
├── .gitignore
└── requirements.txt

🎯 Objetivo
O projeto tem como objetivo colocar em prática conceitos de desenvolvimento de APIs REST, integração com banco de dados relacionais, organização de projetos Python, gerenciamento de dependências e utilização do FastAPI.

A arquitetura separa a responsabilidade da API, da camada de acesso aos dados e do banco de dados, proporcionando uma base para evolução e implementação de novas funcionalidades.