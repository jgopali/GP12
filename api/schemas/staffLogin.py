from pydantic import BaseModel

class StaffLoginBase(BaseModel):
    username: str
    password_hash: str

class StaffLoginCreate(StaffLoginBase):
    pass

class StaffLogin(StaffLoginBase):
    id: int

    class Config:
        orm_mode = True
