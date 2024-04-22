from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, resources):
    # Create a new instance of the Resource model with the provided data
    db_resources = models.Resource(
        name=resources.name,
        amount=resources.amount
    )
    # Add the newly created object to the database session
    db.add(db_resources)
    # Commit the changes to the database
    db.commit()
    # Refresh the object to ensure it reflects the current state in the database
    db.refresh(db_resources)
    # Return the newly created object
    return db_resources


def read_all(db: Session):
    return db.query(models.Resource).all()


def read_one(db: Session, resources_id):
    return db.query(models.Resource).filter(models.Resource.id == resources_id).first()


def update(db: Session, resources_id, resources):
    # Query the database for the object to update
    db_resources = db.query(models.Resource).filter(models.Resource.id == resources_id)
    # Extract the update data from the provided object
    update_data = resources.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_resources.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated record
    return db_resources.first()


def delete(db: Session, resources_id):
    # Query the database for the object to delete
    db_resources = db.query(models.Resource).filter(models.Resource.id == resources_id)
    # Delete the database record without synchronizing the session
    db_resources.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
