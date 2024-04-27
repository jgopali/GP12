from pydantic import BaseModel
from typing import Optional

class RatingsBase(BaseModel):
    rating: int
    review: str

class RatingsCreate(RatingsBase):
    pass

class RatingsUpdate(BaseModel):
    rating: Optional[int] = None
    review: Optional[str] = None

class Ratings(RatingsBase):
    id: int

    class ConfigDict:
        from_attributes = True
