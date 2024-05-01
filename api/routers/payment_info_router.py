from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas.payment_info import PaymentInfoCreate as PaymentInfoCreate, PaymentInfoUpdate as PaymentInfoUpdate, PaymentInfo as PaymentInfoSchema
from ..controllers import payment_info as PaymentInfoController
from ..dependencies.database import get_db

router = APIRouter(
    tags=['PaymentInfo'],
    prefix="/payment_info"
)

# Create method for the PaymentInfo router
@router.post("/", response_model=PaymentInfoSchema)
def create_payment_info(payment_info: PaymentInfoCreate, db: Session = Depends(get_db)):
    return PaymentInfoController.create_payment_info(db=db, payment_info=payment_info.dict())

# Read all method for the PaymentInfo router
@router.get("/", response_model=List[PaymentInfoSchema])
def read_all_payment_info(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return PaymentInfoController.get_all_payment_info(db=db, skip=skip, limit=limit)

# Read one method for the PaymentInfo router
@router.get("/{payment_info_id}", response_model=PaymentInfoSchema)
def read_one_payment_info(payment_info_id: int, db: Session = Depends(get_db)):
    payment_info = PaymentInfoController.get_payment_info_by_id(db=db, payment_info_id=payment_info_id)
    if payment_info is None:
        raise HTTPException(status_code=404, detail="Payment info not found")
    return payment_info

# Update method for the PaymentInfo router
@router.put("/{payment_info_id}", response_model=PaymentInfoSchema)
def update_payment_info(payment_info_id: int, payment_info: PaymentInfoUpdate, db: Session = Depends(get_db)):
    updated_payment_info = PaymentInfoController.update_payment_info(db=db, payment_info_id=payment_info_id, payment_info=payment_info.dict())
    if updated_payment_info is None:
        raise HTTPException(status_code=404, detail="Payment info not found")
    return updated_payment_info

# Delete method for the PaymentInfo router
@router.delete("/{payment_info_id}")
def delete_payment_info(payment_info_id: int, db: Session = Depends(get_db)):
    deleted_payment_info = PaymentInfoController.delete_payment_info(db=db, payment_info_id=payment_info_id)
    if deleted_payment_info is None:
        raise HTTPException(status_code=404, detail="Payment info not found")
    return deleted_payment_info
