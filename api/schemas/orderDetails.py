from pydantic import BaseModel
from typing import Optional

class OrderDetailBase(BaseModel):
    quantity: int
    price: float

class OrderDetailCreate(OrderDetailBase):
    order_id: int
    item_id: int

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    item_id: Optional[int] = None
    quantity: Optional[int] = None
    price: Optional[float] = None

class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    item_id: int

    class Config:
        orm_mode = True
