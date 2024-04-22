from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, menu_items):
    # Create a new instance of the MenuItem model with the provided data
    db_menu_items = models.MenuItem(
        name=menu_items.name,
        price=menu_items.price
    )
    # Add the newly created object to the database session
    db.add(db_menu_items)
    # Commit the changes to the database
    db.commit()
    # Refresh the object to ensure it reflects the current state in the database
    db.refresh(db_menu_items)
    # Return the newly created object
    return db_menu_items


def read_all(db: Session):
    return db.query(models.MenuItem).all()


def read_one(db: Session, menu_items_id):
    return db.query(models.MenuItem).filter(models.MenuItem.id == menu_items_id).first()


def update(db: Session, menu_items_id, menu_items):
    # Query the database for the object to update
    db_menu_items = db.query(models.MenuItem).filter(models.MenuItem.id == menu_items_id)
    # Extract the update data from the provided object
    update_data = menu_items.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_menu_items.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated record
    return db_menu_items.first()


def delete(db: Session, menu_items_id):
    # Query the database for the object to delete
    db_menu_items = db.query(models.MenuItem).filter(models.MenuItem.id == menu_items_id)
    # Delete the database record without synchronizing the session
    db_menu_items.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
