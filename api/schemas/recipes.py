from pydantic import BaseModel
from typing import Optional

class RecipeBase(BaseModel):
    menu_item_id: int
    resource_id: int
    amount_used: float

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(BaseModel):
    menu_item_id: Optional[int] = None
    resource_id: Optional[int] = None
    amount_used: Optional[float] = None

class Recipe(RecipeBase):
    id: int
    
    class ConfigDict:
        from_attributes = True
