from pydantic import BaseModel

class CustomerInfoBase(BaseModel):
    name: str
    phone: str
    email: str
    address: str

class CustomerInfoCreate(CustomerInfoBase):
    pass

class CustomerInfoUpdate(CustomerInfoBase):
    pass

class CustomerInfo(CustomerInfoBase):
    id: int

    class Config:
        orm_mode = True
