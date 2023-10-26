# PROJECT DESCRIPTION

## Ready to set up the project:
    git clone https://github.com/Catalyst-OTU/reporting_app.git


## Installing Packages for Linux, Ubuntu
- Run the following command in your terminal
    - cd app
    - python3 -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt



## RUNNING OR STARTING APPLICATION
- Running FastAPI Service Locally
    - uvicorn main:app --reload





Setup environment variables; allowed environment variables `KEYWORDS`=`VALUES`:

| KEYWORDS | VALUES | DEFAULT VALUE | VALUE TYPE | 
| :------------ | :---------------------: | :------------------: | :------------------: |
| DB_TYPE | | postgresql | string 
| DB_NAME | | report_db | string
| DB_SERVER | | localhost | string 
| DB_USER | | postgres | string 
| DB_PASSWORD | | password  | string 
| DB_PORT | | 5432 | integer   
| BASE_URL | | http://localhost:8000/ | string  
| ADMIN_EMAIL | | admin@admin.com | string 
| ADMIN_PASSWORD | | openforme | string 

