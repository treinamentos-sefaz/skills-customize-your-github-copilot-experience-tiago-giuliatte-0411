from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


class Book(BookCreate):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J. R. R. Tolkien", year=1937),
}
