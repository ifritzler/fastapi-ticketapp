"""
    Hola esta es una descripcion del modulo sin empezar :)
"""
from typing import List
import uvicorn
from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db.db import engine

from app.models.user import ResponseUser, User
from app.repositories.user import get_all_users

app = FastAPI()


@app.get("/users", response_model=List[ResponseUser])
def root():
    """Root Endpoint"""
    return get_all_users()


def create_db_and_tables():
    """Create all data tables in database"""
    SQLModel.metadata.create_all(engine)
    print("Database created")


def start():
    """Start app function for poetry script"""
    create_db_and_tables()
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        workers=2,
    )


if __name__ == "__main__":
    start()
