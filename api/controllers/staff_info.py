from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, staff_info):
    # Create a new instance of the StaffInfo model with the provided data
    db_staff_info = models.StaffInfo(
        name=staff_info.name,
        phone=staff_info.phone,
        email=staff_info.email,
        address=staff_info.address
    )
    # Add the newly created object to the database session
    db.add(db_staff_info)
    # Commit the changes to the database
    db.commit()
    # Refresh the object to ensure it reflects the current state in the database
    db.refresh(db_staff_info)
    # Return the newly created object
    return db_staff_info


def read_all(db: Session):
    return db.query(models.StaffInfo).all()


def read_one(db: Session, staff_info_id):
    return db.query(models.StaffInfo).filter(models.StaffInfo.id == staff_info_id).first()


def update(db: Session, staff_info_id, staff_info):
    # Query the database for the object to update
    db_staff_info = db.query(models.StaffInfo).filter(models.StaffInfo.id == staff_info_id)
    # Extract the update data from the provided object
    update_data = staff_info.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_staff_info.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated record
    return db_staff_info.first()


def delete(db: Session, staff_info_id):
    # Query the database for the object to delete
    db_staff_info = db.query(models.StaffInfo).filter(models.StaffInfo.id == staff_info_id)
    # Delete the database record without synchronizing the session
    db_staff_info.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
