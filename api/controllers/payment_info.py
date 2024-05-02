from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models


def create(db: Session, payment_info):
    # Create a new instance of the PaymentInfo model with the provided data
    db_payment_info = models.PaymentInfo(
        cust_info_id=payment_info.cust_info_id,
        card_number=payment_info.card_number,
        expiration_date=payment_info.expiration_date
    )
    # Add the newly created object to the database session
    db.add(db_payment_info)
    # Commit the changes to the database
    db.commit()
    # Refresh the object to ensure it reflects the current state in the database
    db.refresh(db_payment_info)
    # Return the newly created object
    return db_payment_info


def read_all(db: Session):
    return db.query(models.PaymentInfo).all()


def read_one(db: Session, payment_info_id):
    return db.query(models.PaymentInfo).filter(models.PaymentInfo.id == payment_info_id).first()


def update(db: Session, payment_info_id, payment_info):
    # Query the database for the object to update
    db_payment_info = db.query(models.PaymentInfo).filter(models.PaymentInfo.id == payment_info_id)
    # Extract the update data from the provided object
    update_data = payment_info.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_payment_info.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated record
    return db_payment_info.first()


def delete(db: Session, payment_info_id):
    # Query the database for the object to delete
    db_payment_info = db.query(models.PaymentInfo).filter(models.PaymentInfo.id == payment_info_id)
    # Delete the database record without synchronizing the session
    db_payment_info.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
