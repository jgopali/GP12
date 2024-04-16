from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

# Using declarative base for ORM
Base = declarative_base()

class PaymentInfo(Base):
    __tablename__ = 'payment_info'
    id = Column(Integer, primary_key=True)
    cardholder_name = Column(String(100), nullable=False)
    card_number = Column(String(16))  # Example placeholder, encryption needed
    expiration_date = Column(String(5), nullable=False)  # Format: MM/YY
    cvv = Column(String(3))  # Example placeholder, do not store per PCI DSS
    created_at = Column(DateTime, default=datetime.utcnow)
