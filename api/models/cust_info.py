# Drew Secker
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class CustomerInfo(Base):
    __tablename__ = "customer_info"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), index=True)
    phone = Column(String(50))
    email = Column(String(50))
    address = Column(String(100))