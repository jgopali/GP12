from pydantic import BaseModel
from typing import Optional

class StaffInfoBase(BaseModel):
    name: str
    phone: str
    email: str
    address: str

class StaffInfoCreate(StaffInfoBase):
    pass

class StaffInfoUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

class StaffInfo(StaffInfoBase):
    id: int

    class ConfigDict:
        from_attributes = True
