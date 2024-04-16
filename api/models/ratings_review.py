# Drew Secker
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Ratings(Base):
    __tablename__ = "ratings_review"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rating = Column(Integer)
    review = Column(String(50))