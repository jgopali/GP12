from pydantic import BaseModel
from datetime import datetime

class PaymentInfoBase(BaseModel):
    card_number: str
    expiration_date: datetime

class PaymentInfoCreate(PaymentInfoBase):
    pass

class PaymentInfoUpdate(PaymentInfoBase):
    pass

class PaymentInfo(PaymentInfoBase):
    id: int
    customer_id: int

    class ConfigDict:
        from_attributes = True
