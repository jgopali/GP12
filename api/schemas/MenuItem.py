from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    name: str
    price: float
    type: str

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(MenuItemBase):
    name: Optional[str] = None
    price: Optional[float] = None
    type: Optional[str] = None

class MenuItem(MenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True
