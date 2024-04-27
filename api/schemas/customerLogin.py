from pydantic import BaseModel

class CustomerLoginBase(BaseModel):
    username: str
    password_hash: str

class CustomerLoginCreate(CustomerLoginBase):
    pass

class CustomerLogin(CustomerLoginBase):
    id: int

class CustomerLoginUpdate(BaseModel):
    username: str
    password_hash: str

    class Config:
        orm_mode = True
