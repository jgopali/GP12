from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DateTime, nullable=False, server_default=func.now())
    tracking_number = Column(String(100))
    order_status = Column(String(50))
    total_price = Column(DECIMAL(precision=10, scale=2))
    description = Column(String(300))

    # Relationship to OrderDetail
    order_details = relationship("OrderDetail", back_populates="order")

    class OrderDetail(Base):
        __tablename__ = "order_details"

        id = Column(Integer, primary_key=True, autoincrement=True)
        order_id = Column(Integer, ForeignKey('orders.id'))
        product_name = Column(String(100))
        quantity = Column(Integer)
        price = Column(DECIMAL(precision=10, scale=2))

        # Back-populates from Order
        order = relationship("Order", back_populates="order_details")