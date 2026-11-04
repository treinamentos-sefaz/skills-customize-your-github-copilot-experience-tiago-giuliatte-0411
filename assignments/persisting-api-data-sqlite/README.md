# 📘 Assignment: Persisting API Data with SQLite

## 🎯 Objective
Extend the FastAPI book catalog API to store books in a SQLite database instead of an in-memory dictionary. Practice creating a database table and using parameterized SQL queries to implement persistent CRUD operations.

## 📝 Tasks
### 🛠️ Prepare the SQLite Database
#### Descrição
Use the provided `main.py` as the starting point. Implement an idempotent database initialization function that creates a `books` table when the application starts.
#### Requisitos
O programa concluído deve:
- Use Python's built-in `sqlite3` module; no additional database package is needed.
- Create a `books` table with an auto-incrementing integer ID, a title, an author, and a year.
- Prevent empty titles or authors and negative years using database constraints.
- Create the table only when it does not already exist, preserving saved books when the server restarts.

### 🛠️ Connect the API Endpoints to SQLite
#### Descrição
Replace in-memory book storage with SQL queries that read and modify the database. Keep the existing FastAPI book catalog behavior while using bound parameters for values from requests.
#### Requisitos
O programa concluído deve:
- Return all books from `GET /books` and one matching book from `GET /books/{book_id}`.
- Create books with `POST /books` and return status `201`.
- Update books with `PUT /books/{book_id}` and remove books with `DELETE /books/{book_id}`.
- Return status `404` when an update, deletion, or lookup uses an ID that does not exist.
- Use parameterized SQL for every query that includes request data.

### 🛠️ Verify Persistence and API Behavior
#### Descrição
Run the API, make changes to the catalog, and restart the server to confirm that the database preserves those changes.
#### Requisitos
O programa concluído deve:
- Start from this assignment's directory with `uvicorn main:app --reload`.
- Create, list, retrieve, update, and delete books through the interactive API documentation at `http://127.0.0.1:8000/docs`.
- Keep created or updated books available after stopping and restarting the server.
- Confirm that invalid book data is rejected with status `422` and that missing IDs return status `404`.
