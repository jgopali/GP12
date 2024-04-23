from typing import Optional
from pydantic import BaseModel


class CustomerInfoBase(BaseModel):
    name: str
    phone: str
    email: str
    address: str

class CustomerInfoCreate(CustomerInfoBase):
    pass


class CustomerInfoUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None


class CustomerInfo(CustomerInfoBase):
    id: int

    class ConfigDict:
        from_attributes = True