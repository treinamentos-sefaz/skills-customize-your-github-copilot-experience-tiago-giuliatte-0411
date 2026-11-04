# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com FastAPI, definir endpoints HTTP e validar dados com modelos Pydantic. Ao final, você terá uma API de catálogo de livros com operações CRUD e respostas HTTP apropriadas.

## 📝 Tasks

### 🛠️ Criar a aplicação e um endpoint de saúde

#### Descrição
Use o arquivo inicial fornecido para criar uma aplicação FastAPI e implementar um endpoint simples que confirme que a API está funcionando. Instale as dependências com `python -m pip install fastapi uvicorn` e inicie o servidor com `uvicorn main:app --reload`.

#### Requisitos
O programa concluído deve:

- Iniciar sem erros usando o comando fornecido
- Responder a `GET /health` com o status `200` e um JSON como `{"status": "ok"}`
- Exibir a documentação interativa da API em `http://127.0.0.1:8000/docs`


### 🛠️ Consultar livros pela API

#### Descrição
Implemente endpoints para listar os livros cadastrados e consultar um livro pelo seu identificador. Use o dicionário `books` do arquivo inicial como armazenamento em memória.

#### Requisitos
O programa concluído deve:

- Responder a `GET /books` com a lista de livros
- Responder a `GET /books/{book_id}` com o livro correspondente quando ele existir
- Retornar status `404` quando o identificador solicitado não existir
- Permitir verificar os endpoints e as respostas em `/docs`


### 🛠️ Implementar operações CRUD e validação

#### Descrição
Complete a API para permitir criar, atualizar e remover livros. Use os modelos Pydantic para validar os dados recebidos e retorne um código de status adequado para cada operação.

#### Requisitos
O programa concluído deve:

- Responder a `POST /books` criando um livro e retornando status `201`
- Responder a `PUT /books/{book_id}` atualizando um livro existente e retornar `404` se ele não existir
- Responder a `DELETE /books/{book_id}` removendo um livro existente e retornar `404` se ele não existir
- Rejeitar títulos ou autores vazios e anos negativos com uma resposta de validação `422`
- Manter as alterações disponíveis enquanto o servidor estiver em execução e demonstrar cada operação em `/docs`
