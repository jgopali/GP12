from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import MenuItem as schemas
from ..controllers import menu_items as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['MenuItem'],
    prefix="/menu_items"
)

# Create method for the MenuItem router
@router.post("/", response_model=schemas.MenuItem)
def create_menu_item(menu_item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, menu_items=menu_item)

# Read all method for the MenuItem router
@router.get("/", response_model=List[schemas.MenuItem])
def read_all_menu_items(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Read one method for the MenuItem router
@router.get("/{menu_item_id}", response_model=schemas.MenuItem)
def read_one_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    menu_item = controller.read_one(db, menu_items_id=menu_item_id)
    if menu_item is None:
        raise HTTPException(status_code=404, detail="Menu Item not found")
    return menu_item

# Update method for the MenuItem router
@router.put("/{menu_item_id}", response_model=schemas.MenuItem)
def update_menu_item(menu_item_id: int, menu_item: schemas.MenuItemBase, db: Session = Depends(get_db)):
    db_menu_item = controller.read_one(db, menu_items_id=menu_item_id)
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="Menu Item not found")
    return controller.update(db=db, menu_items_id=menu_item_id, menu_items=menu_item)

# Delete method for the MenuItem router
@router.delete("/{menu_item_id}")
def delete_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    db_menu_item = controller.read_one(db, menu_items_id=menu_item_id)
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="Menu Item not found")
    return controller.delete(db=db, menu_items_id=menu_item_id)
