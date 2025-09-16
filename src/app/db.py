from __future__ import annotations
from contextlib import contextmanager
from pathlib import Path
from sqlmodel import SQLModel, create_engine, Session


DB_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "database.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)




def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)




@contextmanager
def get_session() -> Session:
    with Session(engine) as session:
        yield session