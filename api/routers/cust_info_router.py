from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..schemas import cust_info as schemas
from ..dependencies.database import get_db
from ..controllers import cust_info as controller

router = APIRouter(
    tags=['CustomerInfo'],
    prefix="/cust_info"
)

# Create method for the CustomerInfo router
@router.post("/", response_model=schemas.CustomerInfo)
def create_customer_info(cust_info: schemas.CustomerInfoCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, cust_info=cust_info)

# Read all method for the CustomerInfo router
@router.get("/", response_model=list[schemas.CustomerInfo])
def read_all_customer_info(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Read one method for the CustomerInfo router
@router.get("/{cust_info_id}", response_model=schemas.CustomerInfo)
def read_one_customer_info(cust_info_id: int, db: Session = Depends(get_db)):
    info = controller.read_one(db, cust_info_id=cust_info_id)
    if info is None:
        raise HTTPException(status_code=404, detail="User not found")
    return info

# Update method for the CustomerInfo router
@router.put("/{cust_info_id}", response_model=schemas.CustomerInfo)
def update_customer_info(cust_info_id: int, cust_info_update: schemas.CustomerInfoUpdate, db: Session = Depends(get_db)):
    cust_info_db = controller.read_one(db, cust_info_id=cust_info_id)
    if cust_info_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return controller.update(db=db, cust_info_id=cust_info_id, cust_info=cust_info_update)

# Delete method for the CustomerInfo router
@router.delete("/{cust_info_id}")
def delete_customer_info(cust_info_id: int, db: Session = Depends(get_db)):
    info = controller.read_one(db, cust_info_id=cust_info_id)
    if info is None:
        raise HTTPException(status_code=404, detail="User not found")
    return controller.delete(db=db, cust_info_id=cust_info_id)