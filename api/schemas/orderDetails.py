from pydantic import BaseModel
from typing import Optional
from .MenuItem import MenuItem
from .promotions import Promotions
from .orders import Order

class OrderDetailBase(BaseModel):
    quantity: int
    price: float
    takeout: bool
    order_id: int
    item_id: int
    promotion_id: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailUpdate(BaseModel):
    quantity: Optional[int] = None
    price: Optional[float] = None
    takeout: Optional[bool] = None
    order_id: Optional[int] = None
    item_id: Optional[int] = None
    promotion_id: Optional[int] = None

class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    item_id: int
    promotion_id: int

    order: Order = None
    menu_item: MenuItem = None
    promo: Optional[Promotions] = None

    class ConfigDict:
        from_attributes = True
