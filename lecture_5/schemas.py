from pydantic import BaseModel, Field
from typing import Optional

# Scheme for creating a new book
class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Название книги")
    author: str = Field(..., min_length=1, max_length=100, description="Автор книги")
    year: Optional[int] = Field(None, ge=1000, le=2100, description="Год издания")


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    year: Optional[int] = Field(None, ge=1000, le=2100)


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int]
    

    class Config:
        from_attributes = True 