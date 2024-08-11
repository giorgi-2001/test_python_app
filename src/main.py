from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .schemas import ItemCreateSchema
from . import services
from typing import Annotated


Base.metadata.create_all(bind=engine)


app = FastAPI()


db_dependencie = Annotated[Session, Depends(get_db)]


@app.get("/", tags=["Server"])
def get_server():
    return "Server is running"


@app.get("/items", tags=["Items"])
def get_all_items(db: db_dependencie):
    return services.get_all(db)


@app.get("/items/{id}", tags=["Items"])
def get_item_by_id(id: int, db: db_dependencie):
    item = services.get_one(id, db)
    if item is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Item was not found"
        )
    return item


@app.post("/items", tags=["Items"], status_code=status.HTTP_201_CREATED)
def create_item(item_data: ItemCreateSchema, db: db_dependencie):
    return services.add(item_data, db)


@app.put("/items/{id}", tags=["Items"])
def update_item(id: int, item_data: ItemCreateSchema, db: db_dependencie):
    item = services.update(id, item_data, db)
    if item is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Item was not found"
        )
    return item


@app.delete("/items/{id}", tags=["Items"])
def delete_item(id: int, db: db_dependencie):
    item = services.delete(id, db)
    if item is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Item was not found"
        )
    return item
