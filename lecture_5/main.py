from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book Collection API",
    description="API for managing book collections",
    version="1.0.0"
)


def get_book_or_404(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
    return book

@app.post("/books/", response_model=schemas.BookResponse, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        year=book.year
    )
    
    db.add(db_book)
    db.commit()
    db.refresh(db_book) 
    
    return db_book

@app.get("/books/", response_model=List[schemas.BookResponse])
def read_books(
    skip: int = Query(0, ge=0, description="Skip first N records"),
    limit: int = Query(100, ge=1, le=1000, description="Record number limit"),
    db: Session = Depends(get_db)
):

    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books

@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):

    return get_book_or_404(db, book_id)

@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(
    book_id: int, 
    book_update: schemas.BookUpdate,
    db: Session = Depends(get_db)
):
    
    db_book = get_book_or_404(db, book_id)
    
    update_data = book_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(db_book, field, value)

    db.commit()
    db.refresh(db_book)
    
    return db_book

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):

    db_book = get_book_or_404(db, book_id)
    
    db.delete(db_book)
    db.commit()
    
    return 

@app.get("/books/search/", response_model=List[schemas.BookResponse])
def search_books(
    title: Optional[str] = Query(None, description="Search by name (partial match)"),
    author: Optional[str] = Query(None, description="Search by author (partial match)"),
    year: Optional[int] = Query(None, description="Search by year of publication"),
    db: Session = Depends(get_db)
):

    query = db.query(models.Book)
    
    if title:
        query = query.filter(models.Book.title.contains(title))
    
    if author:
        query = query.filter(models.Book.author.contains(author))
    
    if year:
        query = query.filter(models.Book.year == year)
    
    books = query.all()
    return books

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Book Collection API!",
        "docs": "Documentation is available at /docs",
        "endpoints": {
            "POST /books/": "Add a new book",
            "GET /books/": "Get all books (with pagination)",
            "GET /books/{id}": "Get a book by ID",
            "PUT /books/{id}": "Update book",
            "DELETE /books/{id}": "Delete book",
            "GET /books/search/": "Book Search"
        }
    }

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {
        "error": exc.detail,
        "status_code": exc.status_code
    }