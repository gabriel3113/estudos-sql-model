from __future__ import annotations
from typing import Optional
from sqlmodel import SQLModel, Field




class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None




class Livros(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    book_name: str
    autor: str
    genero: str