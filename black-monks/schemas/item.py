from pydantic import BaseClass


class Item(BaseClass):
    image: str
    weight: float
    uniqueness: str
    price: float
