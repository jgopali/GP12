from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models


def create(db: Session, recipes):
    # Create a new instance of the Recipe model with the provided data
    db_recipes = models.Recipe(
        menu_item_id=recipes.menu_item_id,
        resource_id=recipes.resource_id,
        amount_used=recipes.amount_used
    )
    # Add the newly created object to the database session
    db.add(db_recipes)
    # Commit the changes to the database
    db.commit()
    # Refresh the object to ensure it reflects the current state in the database
    db.refresh(db_recipes)
    # Return the newly created object
    return db_recipes


def read_all(db: Session):
    return db.query(models.Recipe).all()


def read_one(db: Session, recipes_id):
    return db.query(models.Recipe).filter(models.Recipe.id == recipes_id).first()


def update(db: Session, recipes_id, recipes):
    # Query the database for the object to update
    db_recipes = db.query(models.Recipe).filter(models.Recipe.id == recipes_id)
    # Extract the update data from the provided object
    update_data = recipes.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_recipes.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated record
    return db_recipes.first()




def delete(db: Session, recipes_id):
    # Query the database for the object to delete
    db_recipes = db.query(models.Recipe).filter(models.Recipe.id == recipes_id)
    # Delete the database record without synchronizing the session
    db_recipes.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
