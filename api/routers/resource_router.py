from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import resources as schemas
from ..controllers import resources as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Resource'],
    prefix="/resource"
)

# Create method for the Resource router
@router.post("/", response_model=schemas.Resource)
def create_resource(resources: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, resources=resources)

# Read all method for the Resource router
@router.get("/", response_model=List[schemas.Resource])
def read_all_resources(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Read one method for the Resource router
@router.get("/{resources_id}", response_model=schemas.Resource)
def read_one_resource(resources_id: int, db: Session = Depends(get_db)):
    resources = controller.read_one(db, resources_id=resources_id)
    if resources is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources

# Update method for the Resource router
@router.put("/{resources_id}", response_model=schemas.Resource)
def update_resource(resources_id: int, resources: schemas.ResourceBase, db: Session = Depends(get_db)):
    db_resource = controller.read_one(db, resources_id=resources_id)
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return controller.update(db=db, resources_id=resources_id, resources=resources)

# Delete method for the Resource router
@router.delete("/{resources_id}")
def delete_resource(resources_id: int, db: Session = Depends(get_db)):
    db_resource = controller.read_one(db, resources_id=resources_id)
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return controller.delete(db=db, resources_id=resources_id)
