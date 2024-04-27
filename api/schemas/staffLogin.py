from pydantic import BaseModel
from typing import Optional

class StaffLoginBase(BaseModel):
    username: str
    password_hash: str

class StaffLoginCreate(StaffLoginBase):
    pass

class StaffLoginUpdate(BaseModel):
    username: Optional[str] = None
    password_hash: Optional[str] = None

class StaffLogin(StaffLoginBase):
    id: int

    class ConfigDict:
        from_attributes = True
