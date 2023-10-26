from router.models import Admin
from security.hashing import pwd_context
from core.database import Database






database = Database()
engine = database.get_db_connection()
db = database.get_db_session(engine)




# SEEDING STAFF DATA INTO DATABASE
def create_admin():
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