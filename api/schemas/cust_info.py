from pydantic import BaseModel
from typing import Optional

class CustomerInfoBase(BaseModel):
    name: str
    phone: str
    email: str
    address: str

class CustomerInfoCreate(CustomerInfoBase):
    pass

class CustomerInfoUpdate(CustomerInfoBase):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

class CustomerInfo(CustomerInfoBase):
    id: int

    class ConfigDict:
        from_attributes = True