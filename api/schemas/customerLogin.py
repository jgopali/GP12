from pydantic import BaseModel
from typing import Optional

class CustomerLoginBase(BaseModel):
    username: str
    password_hash: str

class CustomerLoginCreate(CustomerLoginBase):
    pass

class CustomerLoginUpdate(BaseModel):
    username: Optional[str] = None
    password_hash: Optional[str] = None

class CustomerLogin(CustomerLoginBase):
    id: int

    class ConfigDict:
        from_attributes = True
