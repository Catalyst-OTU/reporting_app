from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter,Depends,status
from fastapi.exceptions import HTTPException
from security.hashing import Hasher
from sqlalchemy.orm import Session
from core.database import get_db
from core.config import settings
from .models import Logs
from datetime import timedelta
from router.models import Admin
from security.hashing import pwd_context










# Authentication module for admins and users
auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

















## function to authenticate all admin and users
@auth_router.post('/token')
async def admin_and_user_authentication(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    data = Hasher.authenticate_user(form_data.username, form_data.password, db=db)
    if not data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                        detail="Invalid login credentials")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = Hasher.create_access_token(data={"email": data.email}, expires_delta=access_token_expires)

    #Save admin and user login time and date
    db_token = Logs(user_id=data.id)
    db.add(db_token)
    db.commit()
    db.close()

    return {
        "access_token":access_token,
        "token_type": "bearer",
        "user": data
        }
