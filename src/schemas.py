from pydantic import BaseModel


class ItemCreateSchema(BaseModel):
    title: str
    description: str


class ItemSchema(ItemCreateSchema):
    id: int