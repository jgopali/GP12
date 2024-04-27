from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderBase(BaseModel):
    customer_name: str
    order_date: datetime
    description: str

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    order_date: Optional[datetime] = None
    description: Optional[str] = None

class Order(OrderBase):
    id: int

    class ConfigDict:
        from_attributes = True
