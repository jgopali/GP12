from pydantic import BaseModel
from typing import Optional

class OrderDetailBase(BaseModel):
    quantity: int
    price: float
    order_id: int
    item_id: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailUpdate(BaseModel):
    quantity: Optional[int] = None
    price: Optional[float] = None
    order_id: Optional[int] = None
    item_id: Optional[int] = None

class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    item_id: int

    class ConfigDict:
        from_attributes = True
