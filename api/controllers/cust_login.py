from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models


def create(db: Session, cust_login):
    # Create a new instance of the CustomerLogin model with the provided data
    db_cust_login = models.CustomerLogin(
        username=cust_login.username,
        password_hash=cust_login.password_hash
    )
    # Add the newly created object to the database session
    db.add(db_cust_login)
    # Commit the changes to the database
    db.commit()
    # Refresh the object to ensure it reflects the current state in the database
    db.refresh(db_cust_login)
    # Return the newly created object
    return db_cust_login


def read_all(db: Session):
    return db.query(models.CustomerLogin).all()


def read_one(db: Session, cust_login_id):
    return db.query(models.CustomerLogin).filter(models.CustomerLogin.id == cust_login_id).first()


def update(db: Session, cust_login_id, cust_login):
    # Query the database for the object to update
    db_cust_login = db.query(models.CustomerLogin).filter(models.CustomerLogin.id == cust_login_id)
    # Extract the update data from the provided object
    update_data = cust_login.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_cust_login.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated record
    return db_cust_login.first()


def delete(db: Session, cust_login_id):
    # Query the database for the object to delete
    db_cust_login = db.query(models.CustomerLogin).filter(models.CustomerLogin.id == cust_login_id)
    # Delete the database record without synchronizing the session
    db_cust_login.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
