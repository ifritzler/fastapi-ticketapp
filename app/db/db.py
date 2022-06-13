""" Database initialization """
from sqlmodel import create_engine

ENG = r"Z:\desarrollo\python\fastapi\mati-2\app\database.db"
sqlite_url = f"sqlite:///{ENG}"
engine = create_engine(sqlite_url, echo=True)
