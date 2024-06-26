from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status, Response, Depends
from ..models import models


def create(db: Session, promotions):
    # Create a new instance of the Promotions model with the provided data
    db_promotions = models.Promotions(
        name=promotions.name,
        discountAmount=promotions.discountAmount,
        daysRemaining=promotions.daysRemaining,
        code=promotions.code  # New attribute for promotion code
    )
    # Add the newly created object to the database session
    db.add(db_promotions)
    # Commit the changes to the database
    db.commit()
    # Refresh the object to ensure it reflects the current state in the database
    db.refresh(db_promotions)
    # Return the newly created object
    return db_promotions

def update(db: Session, promotions_id, promotions):
    # Query the database for the object to update
    db_promotions = db.query(models.Promotions).filter(models.Promotions.id == promotions_id)
    # Extract the update data from the provided object
    update_data = promotions.dict(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_promotions.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated record
    return db_promotions.first()

def read_all(db: Session):
    return db.query(models.Promotions).all()

def read_one(db: Session, promotions_id):
    return db.query(models.Promotions).filter(models.Promotions.id == promotions_id).first()

def delete(db: Session, promotions_id):
    # Query the database for the object to delete
    db_promotions = db.query(models.Promotions).filter(models.Promotions.id == promotions_id)
    # Delete the database record without synchronizing the session
    db_promotions.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
