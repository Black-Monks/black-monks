from pydantic import BaseModel


class Item(BaseModel):
    image: str
    weight: float
    uniqueness: str
    price: float
