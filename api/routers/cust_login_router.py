from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from hashlib import md5
from ..schemas import customerLogin as schemas
from ..controllers import cust_login as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['CustomerLogin'],
    prefix="/cust_login"
)

def hash_password(password: str) -> str:
    """Hashes the password using MD5."""
    return md5(password.encode()).hexdigest()

# Create method for the CustomerLogin router
@router.post("/", response_model=schemas.CustomerLogin)
def create_customer_login(cust_login: schemas.CustomerLoginCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(cust_login.password_hash)
    cust_login.password_hash = hashed_password
    return controller.create(db=db, cust_login=cust_login)

# Read all method for the CustomerLogin router
@router.get("/", response_model=list[schemas.CustomerLogin])
def read_all_customer_logins(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Read one method for the CustomerLogin router
@router.get("/{cust_login_id}", response_model=schemas.CustomerLogin)
def read_one_customer_login(cust_login_id: int, db: Session = Depends(get_db)):
    login = controller.read_one(db, cust_login_id=cust_login_id)
    if login is None:
        raise HTTPException(status_code=404, detail="Login not found")
    return login

# Update method for the CustomerLogin router
@router.put("/{cust_login_id}", response_model=schemas.CustomerLogin)
def update_customer_login(cust_login_id: int, cust_login_update: schemas.CustomerLoginUpdate, db: Session = Depends(get_db)):
    hashed_password = hash_password(cust_login_update.password_hash)
    cust_login_update.password_hash = hashed_password
    login_db = controller.read_one(db, cust_login_id=cust_login_id)
    if login_db is None:
        raise HTTPException(status_code=404, detail="Login not found")
    return controller.update(db=db, cust_login_id=cust_login_id, cust_login=cust_login_update)

# Delete method for the CustomerLogin router
@router.delete("/{cust_login_id}")
def delete_customer_login(cust_login_id: int, db: Session = Depends(get_db)):
    login = controller.read_one(db, cust_login_id=cust_login_id)
    if login is None:
        raise HTTPException(status_code=404, detail="Login not found")
    return controller.delete(db=db, cust_login_id=cust_login_id)
