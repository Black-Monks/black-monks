from pydantic import BaseModel


class Character(BaseModel):
    body: str
    head: str
    weapon: str
    max_healt: int
    healt: int
    speed: float
