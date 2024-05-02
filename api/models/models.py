from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
from ..dependencies.database import Base

# Base declaration
Base = declarative_base()

# Database models
class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    price = Column(DECIMAL(5,2), nullable=False)
    discounted_price = Column(DECIMAL(5, 2))  # New attribute for discounted price
    type = Column(String(100)) # Such as vegetarian
    order_details = relationship("OrderDetail", back_populates="menu_item")
    recipes = relationship("Recipe", back_populates="menu_item")

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    resource_id = Column(Integer, ForeignKey('resources.id'))
    amount_used = Column(DECIMAL(5,2), nullable=False)
    menu_item = relationship("MenuItem", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    amount = Column(Integer, nullable=False)
    recipes = relationship("Recipe", back_populates="resource")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, default=datetime.now)
    description = Column(String(300))
    order_details = relationship("OrderDetail", back_populates="order")

class Promotions(Base):
    __tablename__ = "promotions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(150), unique=True)
    discountAmount = Column(DECIMAL(5, 2))
    daysRemaining = Column(Integer)

class Ratings(Base):
    __tablename__ = "ratings_review"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rating = Column(Integer)
    review = Column(String(50))

class CustomerInfo(Base):
    __tablename__ = "cust_info"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    phone = Column(String(50))
    email = Column(String(50))
    address = Column(String(100))
    payment_info = relationship("PaymentInfo", uselist=False, back_populates="cust_info")

class CustomerLogin(Base):
    __tablename__ = "cust_login"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(255))

class StaffInfo(Base):
    __tablename__ = "staff_info"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    phone = Column(String(50))
    email = Column(String(50))
    address = Column(String(100))

class StaffLogin(Base):
    __tablename__ = "staff_login"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(255))

class OrderDetail(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    item_id = Column(Integer, ForeignKey('menu_items.id'))
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(5, 2), nullable=False)
    takeout = Column(Boolean, nullable=False, default=False)
    promotion_id = Column(Integer, ForeignKey('promotions.id'), nullable=True)
    order = relationship("Order", back_populates="order_details")
    menu_item = relationship("MenuItem")
    promo = relationship("Promotions")

class PaymentInfo(Base):
    __tablename__ = "payment_info"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cust_info_id = Column(Integer, ForeignKey('cust_info.id'))
    card_number = Column(String(16), nullable=False)
    expiration_date = Column(DATETIME, nullable=False)
    cust_info = relationship("CustomerInfo", back_populates="payment_info")