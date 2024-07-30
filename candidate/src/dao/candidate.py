from models.models import User
import config.db as db
from bson import json_util, ObjectId
import json
import logging
logging.basicConfig(level=logging.DEBUG)


def parse_json(data):
    return json.loads(json_util.dumps(data))

def login(email, password):
    candidate = internal_get_candidate_by_email(email)
    if candidate:
        user = User(userId=str(candidate["_id"]), role="candidate")
        return user

def get_all():
    data = list(db.candidate.find({}))
    if data:
        for i in data:
            i["_id"] = str(i["_id"])
    return data

def create_candidate(new_candidate):
    created_candidate = db.candidate.insert_one(dict(new_candidate))
    if created_candidate.inserted_id is not None:
        candidate = get_candidate_by_id(created_candidate.inserted_id)
        return candidate

def get_candidate_by_id(candidate_id):
    candidate = db.candidate.find_one({"_id": ObjectId(candidate_id)})
    if not candidate:
        return 
    candidate["candidate_id"] = str(candidate["_id"])
    candidate.pop("_id")
    return candidate

def internal_get_candidate_by_email(email):
    logging.debug(f"Querying candidate with email: {email}")
    candidate = db.candidate.find_one({"email": email})
    return candidate

def modify_candidate(candidate_id, updated_candidate):
    candidate = db.candidate.replace_one({"_id": ObjectId(candidate_id)}, updated_candidate)
    updated_candidate = get_candidate_by_id(candidate_id)
    return updated_candidate