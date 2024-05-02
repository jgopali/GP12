from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..schemas import payment_info as schemas
from ..dependencies.database import get_db
from ..controllers import payment_info as controller

router = APIRouter(
    tags=['PaymentInfo'],
    prefix="/payment_info"
)

# Create method for the PaymentInfo router
@router.post("/", response_model=schemas.PaymentInfo)
def create_payment_info(payment_info: schemas.PaymentInfoCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, payment_info=payment_info)

# Read all method for the PaymentInfo router
@router.get("/", response_model=list[schemas.PaymentInfo])
def read_all_payment_info(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Read one method for the PaymentInfo router
@router.get("/{payment_info_id}", response_model=schemas.PaymentInfo)
def read_one_payment_info(payment_info_id: int, db: Session = Depends(get_db)):
    info = controller.read_one(db, payment_info_id=payment_info_id)
    if info is None:
        raise HTTPException(status_code=404, detail="Payment Info not found")
    return info

# Update method for the PaymentInfo router
@router.put("/{payment_info_id}", response_model=schemas.PaymentInfo)
def update_payment_info(payment_info_id: int, payment_info_update: schemas.PaymentInfoUpdate, db: Session = Depends(get_db)):
    payment_info_db = controller.read_one(db, payment_info_id=payment_info_id)
    if payment_info_db is None:
        raise HTTPException(status_code=404, detail="Payment Info not found")
    return controller.update(db=db, payment_info_id=payment_info_id, payment_info=payment_info_update)

# Delete method for the PaymentInfo router
@router.delete("/{payment_info_id}")
def delete_payment_info(payment_info_id: int, db: Session = Depends(get_db)):
    info = controller.read_one(db, payment_info_id=payment_info_id)
    if info is None:
        raise HTTPException(status_code=404, detail="Payment Info not found")
    return controller.delete(db=db, payment_info_id=payment_info_id)