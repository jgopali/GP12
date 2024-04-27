from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import staffInfo as schemas
from ..controllers import staff_info as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Staff Information'],
    prefix="/staff_info"
)

# Create method for the Staff Information router
@router.post("/", response_model=schemas.StaffInfo)
def create_staff_info(staff_info: schemas.StaffInfoCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, staff_info=staff_info)

# Read all method for the Staff Information router
@router.get("/", response_model=List[schemas.StaffInfo])
def read_all_staff_info(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Read one method for the Staff Information router
@router.get("/{staff_info_id}", response_model=schemas.StaffInfo)
def read_one_staff_info(staff_info_id: int, db: Session = Depends(get_db)):
    staff_info = controller.read_one(db, staff_info_id=staff_info_id)
    if staff_info is None:
        raise HTTPException(status_code=404, detail="Staff Information not found")
    return staff_info

# Update method for the Staff Information router
@router.put("/{staff_info_id}", response_model=schemas.StaffInfo)
def update_staff_info(staff_info_id: int, staff_info: schemas.StaffInfoBase, db: Session = Depends(get_db)):
    db_staff_info = controller.read_one(db, staff_info_id=staff_info_id)
    if db_staff_info is None:
        raise HTTPException(status_code=404, detail="Staff Information not found")
    return controller.update(db=db, staff_info_id=staff_info_id, staff_info=staff_info)

# Delete method for the Staff Information router
@router.delete("/{staff_info_id}")
def delete_staff_info(staff_info_id: int, db: Session = Depends(get_db)):
    db_staff_info = controller.read_one(db, staff_info_id=staff_info_id)
    if db_staff_info is None:
        raise HTTPException(status_code=404, detail="Staff Information not found")
    return controller.delete(db=db, staff_info_id=staff_info_id)
