from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import ratings as schemas
from ..controllers import ratings_review as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Ratings & Reviews'],
    prefix="/ratings_review"
)

# Create method for the Ratings & Reviews router
@router.post("/", response_model=schemas.Ratings)
def create_rating_review(ratings_review: schemas.RatingsCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, ratings_review=ratings_review)

# Read all method for the Ratings & Reviews router
@router.get("/", response_model=List[schemas.Ratings])
def read_all_ratings_review(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Read one method for the Ratings & Reviews router
@router.get("/{ratings_review_id}", response_model=schemas.Ratings)
def read_one_rating_review(ratings_review_id: int, db: Session = Depends(get_db)):
    rating_review = controller.read_one(db, ratings_review_id=ratings_review_id)
    if rating_review is None:
        raise HTTPException(status_code=404, detail="Rating & Review not found")
    return rating_review

# Update method for the Ratings & Reviews router
@router.put("/{ratings_review_id}", response_model=schemas.Ratings)
def update_rating_review(ratings_review_id: int, ratings_review: schemas.RatingsBase, db: Session = Depends(get_db)):
    db_rating_review = controller.read_one(db, ratings_review_id=ratings_review_id)
    if db_rating_review is None:
        raise HTTPException(status_code=404, detail="Rating & Review not found")
    return controller.update(db=db, ratings_review_id=ratings_review_id, ratings_review=ratings_review)

# Delete method for the Ratings & Reviews router
@router.delete("/{ratings_review_id}")
def delete_rating_review(ratings_review_id: int, db: Session = Depends(get_db)):
    db_rating_review = controller.read_one(db, ratings_review_id=ratings_review_id)
    if db_rating_review is None:
        raise HTTPException(status_code=404, detail="Rating & Review not found")
    return controller.delete(db=db, ratings_review_id=ratings_review_id)
