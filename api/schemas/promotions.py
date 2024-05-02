from pydantic import BaseModel
from typing import Optional

class PromotionsBase(BaseModel):
    name: str
    discountAmount: float
    daysRemaining: int
    code: str

class PromotionsCreate(PromotionsBase):
    pass

class PromotionsUpdate(BaseModel):
    name: Optional[str] = None
    discountAmount: Optional[float] = None
    daysRemaining: Optional[int] = None
    code: Optional[str] = None

class Promotions(PromotionsBase):
    id: int
    code: str

    class ConfigDict:
        from_attributes = True
