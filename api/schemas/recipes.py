from pydantic import BaseModel
from typing import List

class RecipeBase(BaseModel):
    menu_item_id: int
    resource_id: int
    amount_used: float

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    class Config:
        orm_mode = True
