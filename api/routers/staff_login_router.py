from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from hashlib import md5
from ..schemas import staffLogin as schemas
from ..controllers import staff_login as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['StaffLogin'],
    prefix="/staff_login"
)

def hash_password(password: str) -> str:
    """Hashes the password using MD5."""
    return md5(password.encode()).hexdigest()

# Create method for the StaffLogin router
@router.post("/", response_model=schemas.StaffLogin)
def create_staff_login(staff_login: schemas.StaffLoginCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(staff_login.password_hash)
    staff_login.password_hash = hashed_password
    return controller.create(db=db, staff_login=staff_login)

# Read all method for the StaffLogin router
@router.get("/", response_model=list[schemas.StaffLogin])
def read_all_staff_logins(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Read one method for the StaffLogin router
@router.get("/{staff_login_id}", response_model=schemas.StaffLogin)
def read_one_staff_login(staff_login_id: int, db: Session = Depends(get_db)):
    login = controller.read_one(db, staff_login_id=staff_login_id)
    if login is None:
        raise HTTPException(status_code=404, detail="Login not found")
    return login

# Update method for the StaffLogin router
@router.put("/{staff_login_id}", response_model=schemas.StaffLogin)
def update_staff_login(staff_login_id: int, staff_login_update: schemas.StaffLoginUpdate, db: Session = Depends(get_db)):
    hashed_password = hash_password(staff_login_update.password_hash)
    staff_login_update.password_hash = hashed_password
    login_db = controller.read_one(db, staff_login_id=staff_login_id)
    if login_db is None:
        raise HTTPException(status_code=404, detail="Login not found")
    return controller.update(db=db, staff_login_id=staff_login_id, staff_login=staff_login_update)

# Delete method for the StaffLogin router
@router.delete("/{staff_login_id}")
def delete_staff_login(staff_login_id: int, db: Session = Depends(get_db)):
    login = controller.read_one(db, staff_login_id=staff_login_id)
    if login is None:
        raise HTTPException(status_code=404, detail="Login not found")
    return controller.delete(db=db, staff_login_id=staff_login_id)
