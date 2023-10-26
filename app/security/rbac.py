from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException,Depends,status
from sqlalchemy.orm import Session
from core.database import get_db
from core.config import settings
from router.models import Admin
from jose import JWTError, jwt
from typing import Annotated










oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")









    # function to get user or admin by email
def get_user_by_email(username: str, db: Session):
    data = db.query(Admin).filter(Admin.email == username).first()
    return data







#function to get current user by token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("email")
        #print("username/email extracted is ", username)
    
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(username=username, db=db)
    if user is None:
        raise credentials_exception
    return user 








#function to get active current user by token
async def get_current_active_user(current_user: Annotated[Admin, Depends(get_current_user)]):
    if current_user.is_active != True:
        raise HTTPException(status_code=400, detail="you account is not active")
    return current_user








#function to check if current user is admin
async def check_if_is_admin(current_active_user: Annotated[Admin, Depends(get_current_active_user)]):
    if current_active_user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="only admin can access this api route")
    return current_active_user








#function to get access role to all users
async def for_all_users(current_active_user: Annotated[Admin, Depends(get_current_active_user)]):
    if current_active_user.role != 'user' and current_active_user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="admin and user can access this api route")
    return current_active_user








