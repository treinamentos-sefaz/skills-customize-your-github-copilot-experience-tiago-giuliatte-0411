from contextlib import asynccontextmanager, contextmanager
import sqlite3
from collections.abc import AsyncIterator, Iterator
from pathlib import Path

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

DATABASE_PATH = Path(__file__).with_name("books.db")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=0)


class Book(BookCreate):
    id: int


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def init_db() -> None:
    with get_connection() as connection:
        # TODO: Create the books table with the required columns and constraints.
        pass


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    init_db()
    yield


app = FastAPI(title="Book Catalog API", lifespan=lifespan)


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    # TODO: Return all books from SQLite, ordered by ID.
    raise HTTPException(status_code=501, detail="Endpoint not implemented yet")


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    # TODO: Return one book, or 404 when it does not exist.
    raise HTTPException(status_code=501, detail="Endpoint not implemented yet")


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate) -> Book:
    # TODO: Insert the book and return it with its generated ID.
    raise HTTPException(status_code=501, detail="Endpoint not implemented yet")


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate) -> Book:
    # TODO: Update the book, or return 404 when it does not exist.
    raise HTTPException(status_code=501, detail="Endpoint not implemented yet")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    # TODO: Delete the book, or return 404 when it does not exist.
    raise HTTPException(status_code=501, detail="Endpoint not implemented yet")
