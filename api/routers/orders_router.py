'''from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import orders as schemas
from ..controllers import orders as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Order'],
    prefix="/orders"
)

# Create method for the Order router
@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, order=order)

# Read all method for the Order router
@router.get("/", response_model=List[schemas.Order])
def read_all_orders(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Read one method for the Order router
@router.get("/{order_id}", response_model=schemas.Order)
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = controller.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# Update method for the Order router
@router.put("/{order_id}", response_model=schemas.Order)
def update_order(order_id: int, order: schemas.OrderBase, db: Session = Depends(get_db)):
    db_order = controller.read_one(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return controller.update(db=db, order_id=order_id, order=order)

# Delete method for the Order router
@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = controller.read_one(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return controller.delete(db=db, order_id=order_id)'''
