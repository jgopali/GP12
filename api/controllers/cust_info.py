from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models


def create(db: Session, cust_info):
    # Create a new instance of the CustomerInfo model with the provided data
    db_cust_info = models.CustomerInfo(
        name=cust_info.name,
        phone=cust_info.phone,
        email=cust_info.email,
        address=cust_info.address
    )
    # Add the newly created object to the database session
    db.add(db_cust_info)
    # Commit the changes to the database
    db.commit()
    # Refresh the object to ensure it reflects the current state in the database
    db.refresh(db_cust_info)
    # Return the newly created object
    return db_cust_info


def read_all(db: Session):
    return db.query(models.CustomerInfo).all()


def read_one(db: Session, cust_info_id):
    return db.query(models.CustomerInfo).filter(models.CustomerInfo.id == cust_info_id).first()


def update(db: Session, cust_info_id, cust_info):
    # Query the database for the object to update
    db_cust_info = db.query(models.CustomerInfo).filter(models.CustomerInfo.id == cust_info_id)
    # Extract the update data from the provided object
    update_data = cust_info.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_cust_info.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated record
    return db_cust_info.first()


def delete(db: Session, cust_info_id):
    # Query the database for the object to delete
    db_cust_info = db.query(models.CustomerInfo).filter(models.CustomerInfo.id == cust_info_id)
    # Delete the database record without synchronizing the session
    db_cust_info.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
