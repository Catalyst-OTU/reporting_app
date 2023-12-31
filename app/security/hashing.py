from passlib.context import CryptContext
from datetime import datetime,timedelta
from sqlalchemy.orm import Session
from core.config import settings
from router.models import Admin
from typing import Optional
from jose import jwt








pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")









class Hasher():

    #get user by email function
    @staticmethod
    def get_user_by_email(username: str, db: Session):
        user = db.query(Admin).filter(Admin.email == username).first()
        if not user:
            return False
        return user



    #function to verify password
    @staticmethod 
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
    



    #function to authenticate user
    @staticmethod
    def authenticate_user(username: str, password: str, db: Session):
        db_user = Hasher.get_user_by_email(username=username, db=db)
        if not db_user:
            return False
        if not Hasher.verify_password(password, db_user.password):
            return False 
        return db_user


    

    # Generate access token function
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt
    




    # Generate reset password token function
    @staticmethod
    def generate_reset_password_token(expires: int = None):
        if expires is not None:
            expires = datetime.utcnow() + expires
        else:
            expires = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {"exp": expires}
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)
        return encoded_jwt


        
    


