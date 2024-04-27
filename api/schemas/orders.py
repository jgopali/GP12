from pydantic import BaseModel
from typing import List
from datetime import datetime

class OrderBase(BaseModel):
    customer_name: str
    order_date: datetime
    description: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    order_details: List["OrderDetail"] = []

    class Config:
        orm_mode = True
