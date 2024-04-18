#EliELk
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Recipe(Base):
    __tablename__ = 'menu_item_resource'

    menu_item_id = Column(Integer, ForeignKey('menu_items.id'), primary_key=True)
    resource_id = Column(Integer, ForeignKey('resources.id'), primary_key=True)
    amount_used = Column(DECIMAL(5,2), nullable=False)

    # Relationship to MenuItem and Resource
    menu_item = relationship("MenuItem", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")
