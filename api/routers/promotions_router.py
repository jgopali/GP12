from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import promotions as schemas
from ..controllers import promotions as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Promotions'],
    prefix="/promotions"
)

# Create method for the Promotions router
@router.post("/", response_model=schemas.Promotions)
def create_promotion(promotions: schemas.PromotionsCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, promotions=promotions)

# Read all method for the Promotions router
@router.get("/", response_model=List[schemas.Promotions])
def read_all_promotions(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Read one method for the Promotions router
@router.get("/{promotions_id}", response_model=schemas.Promotions)
def read_one_promotion(promotions_id: int, db: Session = Depends(get_db)):
    promotion = controller.read_one(db, promotions_id=promotions_id)
    if promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion

# Update method for the Promotions router
@router.put("/{promotions_id}", response_model=schemas.Promotions)
def update_promotion(promotions_id: int, promotions: schemas.PromotionsBase, db: Session = Depends(get_db)):
    db_promotion = controller.read_one(db, promotions_id=promotions_id)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return controller.update(db=db, promotions_id=promotions_id, promotions=promotions)

# Delete method for the Promotions router
@router.delete("/{promotions_id}")
def delete_promotion(promotions_id: int, db: Session = Depends(get_db)):
    db_promotion = controller.read_one(db, promotions_id=promotions_id)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return controller.delete(db=db, promotions_id=promotions_id)
