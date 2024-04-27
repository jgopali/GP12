'''from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models


def create(db: Session, menu_item_resource):
    # Create a new instance of the Recipe model with the provided data
    db_menu_item_resource = models.Recipe(
        menu_item_id=menu_item_resource.menu_item_id,
        resource_id=menu_item_resource.resource_id,
        amount_used=menu_item_resource.amount_used
    )
    # Add the newly created object to the database session
    db.add(db_menu_item_resource)
    # Commit the changes to the database
    db.commit()
    # Refresh the object to ensure it reflects the current state in the database
    db.refresh(db_menu_item_resource)
    # Return the newly created object
    return db_menu_item_resource


def read_all(db: Session):
    return db.query(models.Recipe).all()


def read_one(db: Session, menu_item_resource_id):
    return db.query(models.Recipe).filter(models.Recipe.id == menu_item_resource_id).first()


def update(db: Session, menu_item_resource_id, menu_item_resource):
    # Query the database for the object to update
    db_menu_item_resource = db.query(models.Recipe).filter(models.Recipe.id == menu_item_resource_id)
    # Extract the update data from the provided object
    update_data = menu_item_resource.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_menu_item_resource.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated record
    return db_menu_item_resource.first()


def delete(db: Session, menu_item_resource_id):
    # Query the database for the object to delete
    db_menu_item_resource = db.query(models.Recipe).filter(models.Recipe.id == menu_item_resource_id)
    # Delete the database record without synchronizing the session
    db_menu_item_resource.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)'''
