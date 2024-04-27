from pydantic import BaseModel

class PromotionsBase(BaseModel):
    name: str
    discountAmount: float

class PromotionsCreate(PromotionsBase):
    pass

class Promotions(PromotionsBase):
    id: int

    class Config:
        orm_mode = True
