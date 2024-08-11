from sqlalchemy.orm import Session
from .models import Item
from .schemas import ItemCreateSchema


def get_all(db: Session):
    return db.query(Item).all()


def get_one(id: int, db: Session):
    return db.query(Item).filter(Item.id == id).first()


def add(item_to_add: ItemCreateSchema, db: Session):
    item = Item(**item_to_add.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update(id: int, update_data: ItemCreateSchema, db: Session):
    item = db.query(Item).filter(Item.id == id).first()
    if item is None:
        return None
    item.title = update_data.title
    item.description = update_data.description
    db.commit()
    db.refresh(item)
    return item


def delete(id: int, db: Session):
    item = db.query(Item).filter(Item.id == id).first()
    if item is None:
        return None
    db.delete(item)
    db.commit()
    return item
