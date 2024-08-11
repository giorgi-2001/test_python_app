from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


SQL_ALCHEMY_DB_URL = "sqlite:///./database.db"


engine = create_engine(
    SQL_ALCHEMY_DB_URL, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
