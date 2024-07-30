from models.models import User
import config.db as db
from bson import json_util, ObjectId
import json

def parse_json(data):
    return json.loads(json_util.dumps(data))

def login(email, password):
    company = internal_get_company_by_email(email)
    if company:
        user = User(userId=str(company["_id"]), role="company")
        return user

def get_all():
    data = list(db.company.find({}))
    if data:
        for i in data:
            i["_id"] = str(i["_id"])
    return data

def create_company(new_company):
    created_company = db.company.insert_one(dict(new_company))
    if created_company.inserted_id is not None:
        company = get_company_by_id(created_company.inserted_id)
        return company
    return 

def get_company_by_id(company_id):
    company = db.company.find_one({"_id": ObjectId(company_id)})
    if not company:
        return 
    company["company_id"] = str(company["_id"])
    company.pop("_id")
    return company

def internal_get_company_by_email(email):
    company = db.company.find_one({"email": email})
    return company

def modify_company(company_id, updated_company):
    company = db.company.replace_one({"_id": ObjectId(company_id)}, updated_company)
    updated_company = get_company_by_id(company_id)
    return updated_company