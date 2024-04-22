from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, staff_login):
    # Create a new instance of the StaffLogin model with the provided data
    db_staff_login = models.StaffLogin(
        username=staff_login.username,
        password_hash=staff_login.password_hash
    )
    # Add the newly created object to the database session
    db.add(db_staff_login)
    # Commit the changes to the database
    db.commit()
    # Refresh the object to ensure it reflects the current state in the database
    db.refresh(db_staff_login)
    # Return the newly created object
    return db_staff_login


def read_all(db: Session):
    return db.query(models.StaffLogin).all()


def read_one(db: Session, staff_login_id):
    return db.query(models.StaffLogin).filter(models.StaffLogin.id == staff_login_id).first()


def update(db: Session, staff_login_id, staff_login):
    # Query the database for the object to update
    db_staff_login = db.query(models.StaffLogin).filter(models.StaffLogin.id == staff_login_id)
    # Extract the update data from the provided object
    update_data = staff_login.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_staff_login.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated record
    return db_staff_login.first()


def delete(db: Session, staff_login_id):
    # Query the database for the object to delete
    db_staff_login = db.query(models.StaffLogin).filter(models.StaffLogin.id == staff_login_id)
    # Delete the database record without synchronizing the session
    db_staff_login.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
