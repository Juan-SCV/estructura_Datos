from typing import List
from pydantic import BaseModel


class Item(BaseModel):
    nombre: str
    productos: List[str]