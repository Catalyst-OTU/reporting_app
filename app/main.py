from fastapi.middleware.cors import CORSMiddleware
from api.urls import router as api_router
from security.hashing import pwd_context
from core.database import Database
from core.database import engine
from core.config import settings
from router.models import Base
from router.models import Admin
from fastapi import FastAPI
import uvicorn







database = Database()
engine = database.get_db_connection()
db = database.get_db_session(engine)
Base.metadata.create_all(bind=engine)




## adding our api routes 
def include_router(app):
    app.include_router(api_router)
#


# SEEDING STAFF DATA INTO DATABASE
def create_admin(app):
    db_addStaff = Admin()
    db_addStaff.name = "Super Admin"
    db_addStaff.email = "admin@admin.com"
    db_addStaff.password = pwd_context.hash("openforme")
    db_addStaff.contact = "0123456789",
    db_addStaff.role = "admin"
    db_email = db.query(Admin).filter(Admin.email == db_addStaff.email).first()
    db_contact = db.query(Admin).filter(Admin.contact == db_addStaff.contact).first()
    if db_email or db_contact:
        return "Admin already exist!!!"
    db.add(db_addStaff)
    db.flush()
    db.commit()
    print("Admin created successful")





def start_application():
    app = FastAPI(docs_url="/", title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,    
    allow_methods=["*"],
    allow_headers=["*"]
    )
    create_admin(app)
    include_router(app)
    return app
app = start_application()



if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=2020, log_level="info", reload = True)
    print("running")
