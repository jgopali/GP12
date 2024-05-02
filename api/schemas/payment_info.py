from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .cust_info import CustomerInfo

class PaymentInfoBase(BaseModel):
    card_number: str
    expiration_date: datetime
    cust_info_id: int

class PaymentInfoCreate(PaymentInfoBase):
    pass

class PaymentInfoUpdate(PaymentInfoBase):
    card_number: Optional[str] = None
    expiration_date: Optional[datetime] = None
    cust_info_id: Optional[int] = None

class PaymentInfo(PaymentInfoBase):
    id: int
    cust_info_id: int

    cust_info: CustomerInfo = None

    class ConfigDict:
        from_attributes = True
