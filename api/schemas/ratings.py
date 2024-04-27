from pydantic import BaseModel

class RatingsBase(BaseModel):
    rating: int
    review: str

class RatingsCreate(RatingsBase):
    pass

class Ratings(RatingsBase):
    id: int

    class Config:
        orm_mode = True
