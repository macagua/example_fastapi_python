from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    """Base model for Books

    Args:
        BaseModel (class): Base model class
    """
    title: str
    author: str
    pages: int
    editorial: Optional[str]

@app.get("/")
def index():
    return {"message": "Hola, Pythonianos 🐍"}

@app.get("/books/{id}")
def get_books(id: int):
    """Get books

    Args:
        id (int): Book id

    Returns:
        dict: Book id as dictionary
    """
    return {"data": id}

@app.post("/books")
def set_book(book: Book):
    """Set Book instance

    Args:
        book (Book): Base model for Books

    Returns:
        dict: the message of Book for save
    """
    return {"message": f"The '{book.title}' book was saved!"}
