import config.db as db
from bson import json_util, ObjectId
import json

def parse_json(data):
    return json.loads(json_util.dumps(data))

def get_all():
    data = list(db.job.find({}))
    if data:
        for i in data:
            i["job_id"] = str(i["_id"])
            i.pop("_id")
    return data

def get_jobs_by_company_id(company_id):
    data = list(db.job.find({"company_id": company_id}))
    if data:
        for i in data:
            i["job_id"] = str(i["_id"])
            i.pop("_id")
    return data

def create_job(new_job):
    created_job = db.job.insert_one(dict(new_job))
    if created_job.inserted_id is not None:
        job = get_job_by_id(created_job.inserted_id)
        return job
    return 

def get_job_by_id(job_id):
    job = db.job.find_one({"_id": ObjectId(job_id)})
    if not job:
        return 
    job["job_id"] = str(job["_id"])
    job.pop("_id")
    return job

def modify_job(job_id, updated_job):
    job = db.job.replace_one({"_id": ObjectId(job_id)}, updated_job)
    updated_job = get_job_by_id(job_id)
    return updated_job

# application
def get_job_application_by_id(job_id):
    application = db.application.find_one({"_id": ObjectId(job_id)})
    if not application:
        return 
    application["application_id"] = str(application["_id"])
    application.pop("_id")
    return application

def view_job_applications(job_id):
    applications = list(db.application.find({"job_id": job_id}))
    if applications:
        for i in applications:
            i["job_application_id"] = str(i["_id"])
            i.pop("_id")
            i.pop("job_id")
            candidate = db.candidate.find_one({"_id": ObjectId(i["candidate_id"])})
            if candidate:
                candidate["candidate_id"] = str(candidate["_id"])
                candidate.pop("_id")
                i["candidate"] = candidate
    return applications

def create_job_application(new_job): 
    created_job_application = db.application.insert_one(dict(new_job))
    if created_job_application.inserted_id is not None:
        application = get_job_application_by_id(created_job_application.inserted_id)
        return application

def update_job_application_status(application_id, status):
    result = db.application.update_one({ "_id" : ObjectId(application_id) }, { "$set" : { "status" : status } })
    if result.modified_count == 1:
        application = get_job_application_by_id(application_id)
        return application

def view_candidate_job_applications(candidate_id):
    applications = list(db.application.find({"candidate_id": candidate_id}))
    if applications:
        for i, application in enumerate(applications):
            application["job_application_id"] = str(application["_id"])
            job = get_job_by_id(application["job_id"])
            job["status"] = application["status"]
            company = db.company.find_one({"_id": ObjectId(job["company_id"])})
            company["company_id"] = str(company["_id"])
            company.pop("_id")
            job["company"] = company
            applications[i] = job
    return applications

