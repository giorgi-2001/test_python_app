from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from os import getenv


load_dotenv()


SQLITE_URL = "sqlite:///./database.db"


DB_URI = getenv("PG_URL", SQLITE_URL)


engine = create_engine(DB_URI)


SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
