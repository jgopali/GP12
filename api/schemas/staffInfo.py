from pydantic import BaseModel

class StaffInfoBase(BaseModel):
    name: str
    phone: str
    email: str
    address: str

class StaffInfoCreate(StaffInfoBase):
    pass

class StaffInfo(StaffInfoBase):
    id: int

    class Config:
        orm_mode = True
