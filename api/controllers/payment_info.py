from sqlalchemy.orm import Session
from typing import List
from ..models import models

def create_payment_info(db: Session, payment_info: dict):
    db_payment_info = models.PaymentInfo(**payment_info)
    db.add(db_payment_info)
    db.commit()
    db.refresh(db_payment_info)
    return db_payment_info

def get_payment_info_by_id(db: Session, payment_info_id: int):
    return db.query(models.PaymentInfo).filter(models.PaymentInfo.id == payment_info_id).first()

def get_all_payment_info(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.PaymentInfo).offset(skip).limit(limit).all()

def update_payment_info(db: Session, payment_info_id: int, payment_info: dict):
    db_payment_info = db.query(models.PaymentInfo).filter(models.PaymentInfo.id == payment_info_id).first()
    if db_payment_info is None:
        return None
    for key, value in payment_info.items():
        setattr(db_payment_info, key, value)
    db.commit()
    db.refresh(db_payment_info)
    return db_payment_info

def delete_payment_info(db: Session, payment_info_id: int):
    db_payment_info = db.query(models.PaymentInfo).filter(models.PaymentInfo.id == payment_info_id).first()
    if db_payment_info is None:
        return None
    db.delete(db_payment_info)
    db.commit()
    return db_payment_info
