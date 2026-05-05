from fastapi import FastAPI
import json
from pydantic import BaseModel

#
app = FastAPI()


#
#
# @app.get("/greeting")
# def greeting():
#     return {"respond": "Привіт з сервера2"}
# --- модель ---
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    pages: int


def write_books(books):
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4)


def read_books():
    with open("books.json", "r", encoding="utf-8") as f:
        return json.load(f)


@app.get("/books")
def get_books():
    return read_books()


@app.get("/books/{book_id}")
def get_book(book_id: int):
    books = read_books()
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}


@app.post("/books")
def add_book(book: Book):
    books = read_books()
    books.append(book.dict())
    write_books(books)
    return {"message": "Book added successfully"}


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    books = read_books()
    new_books = [b for b in books if b["id"] != book_id]

    if len(new_books) == len(books):
        return {"error": "Book not found"}

    write_books(new_books)
    return {"message": "Book deleted"}
