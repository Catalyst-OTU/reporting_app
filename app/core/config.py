## import libraries
from datetime import time, date
from functools import lru_cache
import os, logging, config
from dotenv import load_dotenv 
import secrets

from pathlib import Path
from babel import Locale

## lets load our .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)



class Settings:
    PROJECT_NAME:str = "REPORTING APP"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "report_db")

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


    POOL_SIZE: int = 20
    POOL_RECYCLE: int = 3600
    POOL_TIMEOUT: int = 15
    MAX_OVERFLOW: int = 2
    CONNECT_TIMEOUT: int = 60
    connect_args = {"connect_timeout":CONNECT_TIMEOUT}

    ## lets define var for creating the access token
    SECRET_KEY : str = "7b6c506ee07337cc3d02536d5119c4b2"
    ALGORITHM = "HS256"
    JWT_SECRET_KEY : str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    EMAIL_CODE_DURATION_IN_MINUTES= 15
    EMAIL_CODE_DURATION_IN_MINUTES: int = 15
    ACCESS_TOKEN_DURATION_IN_MINUTES: int = 60
    REFRESH_TOKEN_DURATION_IN_MINUTES: int = 600
    PASSWORD_RESET_TOKEN_DURATION_IN_MINUTES: int = 15
    ACCOUNT_VERIFICATION_TOKEN_DURATION_IN_MINUTES: int = 15


    MAIL_USERNAME: str = 'dev.aiti.com.gh@gmail.com'
    MAIL_PASSWORD: str = 'uefuovgtfwyfgskv'
    MAIL_FROM: str = 'dev.aiti.com.gh@gmail.com'
    MAIL_PORT: int = 587
    MAIL_SERVER: str = 'smtp.gmail.com'
    MAIL_STARTTLS = True
    MAIL_SSL_TLS = False
    USE_CREDENTIALS = True
    VALIDATE_CERTS = True

    APS_COALESCE: bool = False
    APS_MAX_INSTANCES: int = 20
    APS_MISFIRE_GRACE_TIME: int = 4
    APS_THREAD_POOL_MAX_WORKERS: int = 20
    APS_PROCESS_POOL_MAX_WORKERS: int = 5






    # DATABASE_URL = "mysql+pymysql://root:@localhost:3307/appraisal_db"
    # SECRET_KEY = "supersecretkeyhere"

settings = Settings()