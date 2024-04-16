from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from passlib.context import CryptContext
from ..dependencies.database import Base

# Define a global instance of the password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CustomerLogin(Base):
    __tablename__ = "customer_login"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True)
    password_hash = Column(String)

    @validates("password_hash")
    def validate_password_hash(self, key, password):
        """Encrypt the password using a secure hashing algorithm before storing it."""
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str):
        """Verify if the provided password matches the stored hashed password."""
        return pwd_context.verify(plain_password, self.password_hash)
