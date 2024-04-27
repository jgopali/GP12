from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import resources as schemas
from ..controllers import menu_item_resource as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['MenuItemResource'],
    prefix="/menu_item_resource"
)

# Create method for the MenuItemResource router
@router.post("/", response_model=schemas.Resource)
def create_menu_item_resource(menu_item_resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, menu_item_resource=menu_item_resource)

# Read all method for the MenuItemResource router
@router.get("/", response_model=List[schemas.Resource])
def read_all_menu_item_resources(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Read one method for the MenuItemResource router
@router.get("/{menu_item_resource_id}", response_model=schemas.Resource)
def read_one_menu_item_resource(menu_item_resource_id: int, db: Session = Depends(get_db)):
    menu_item_resource = controller.read_one(db, menu_item_resource_id=menu_item_resource_id)
    if menu_item_resource is None:
        raise HTTPException(status_code=404, detail="Menu Item Resource not found")
    return menu_item_resource

# Update method for the MenuItemResource router
@router.put("/{menu_item_resource_id}", response_model=schemas.Resource)
def update_menu_item_resource(menu_item_resource_id: int, menu_item_resource: schemas.ResourceBase, db: Session = Depends(get_db)):
    db_menu_item_resource = controller.read_one(db, menu_item_resource_id=menu_item_resource_id)
    if db_menu_item_resource is None:
        raise HTTPException(status_code=404, detail="Menu Item Resource not found")
    return controller.update(db=db, menu_item_resource_id=menu_item_resource_id, menu_item_resource=menu_item_resource)

# Delete method for the MenuItemResource router
@router.delete("/{menu_item_resource_id}")
def delete_menu_item_resource(menu_item_resource_id: int, db: Session = Depends(get_db)):
    db_menu_item_resource = controller.read_one(db, menu_item_resource_id=menu_item_resource_id)
    if db_menu_item_resource is None:
        raise HTTPException(status_code=404, detail="Menu Item Resource not found")
    return controller.delete(db=db, menu_item_resource_id=menu_item_resource_id)
