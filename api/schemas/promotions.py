from pydantic import BaseModel
from typing import Optional

class PromotionsBase(BaseModel):
    name: str
    discountAmount: float
    daysRemaining: int

class PromotionsCreate(PromotionsBase):
    pass

class PromotionsUpdate(BaseModel):
    name: Optional[str] = None
    discountAmount: Optional[float] = None
    daysRemaining: Optional[int] = None

class Promotions(PromotionsBase):
    id: int

    class ConfigDict:
        from_attributes = True
