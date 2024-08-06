from sqlalchemy import Column, Integer, String
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column("id", Integer, primary_key=True, index=True)
    title = Column("title", String)
    description = Column("description", String)
