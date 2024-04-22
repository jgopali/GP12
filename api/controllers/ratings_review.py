from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, ratings_review):
    # Create a new instance of the Ratings model with the provided data
    db_ratings_review = models.Ratings(
        rating=ratings_review.rating,
        review=ratings_review.review
    )
    # Add the newly created object to the database session
    db.add(db_ratings_review)
    # Commit the changes to the database
    db.commit()
    # Refresh the object to ensure it reflects the current state in the database
    db.refresh(db_ratings_review)
    # Return the newly created object
    return db_ratings_review


def read_all(db: Session):
    return db.query(models.Ratings).all()


def read_one(db: Session, ratings_review_id):
    return db.query(models.Ratings).filter(models.Ratings.id == ratings_review_id).first()


def update(db: Session, ratings_review_id, ratings_review):
    # Query the database for the object to update
    db_ratings_review = db.query(models.Ratings).filter(models.Ratings.id == ratings_review_id)
    # Extract the update data from the provided object
    update_data = ratings_review.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_ratings_review.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated record
    return db_ratings_review.first()


def delete(db: Session, ratings_review_id):
    # Query the database for the object to delete
    db_ratings_review = db.query(models.Ratings).filter(models.Ratings.id == ratings_review_id)
    # Delete the database record without synchronizing the session
    db_ratings_review.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
