import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import dao.job as job_db
from fastapi.responses import JSONResponse
import models.models as models

app = FastAPI(docs_url="/job/swagger")

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/job")
async def root():
    return {"message": "hello job"}

# jobs
@app.get("/job/getall")
async def root():
    print("/getall: triggered")
    data = job_db.get_all()
    return JSONResponse(status_code=200, content=data)

@app.get("/job/{job_id}")
def get_job(job_id: str):
    job = job_db.get_job_by_id(job_id)
    if job:
        return JSONResponse(content=job, status_code=200)
    return JSONResponse(content="job not found.", status_code=400)

@app.get("/job/company/{company_id}")
def get_jobs(company_id: str):
    jobs = job_db.get_jobs_by_company_id(company_id)
    if jobs:
        return JSONResponse(content=jobs, status_code=200)
    return JSONResponse(content="job not found.", status_code=400)

@app.post("/job") 
def create_job(job: models.Job):
    new_job = job_db.create_job(job)
    if new_job:
        return JSONResponse(content=new_job, status_code=200)
    return JSONResponse(content="Unable to get or create new job.", status_code=400)

@app.put("/job/{job_id}")
def update_job(job_id: str , job: models.Job):
    updated_job = job_db.modify_job(job_id, job)
    if updated_job:
        return JSONResponse(content=updated_job, status_code=200)
    return JSONResponse(content="Unable to update job profile.", status_code=400)

# job application
@app.get("/job/{job_id}/application")
def view_job_applications(job_id: str):
    job_applications = job_db.view_job_applications(job_id)
    if job_applications:
        return JSONResponse(content=job_applications, status_code=200)
    return JSONResponse(content=f"Unable to get job applications for job_id {job_id}", status_code=400)


@app.post("/job/application")
def create_job_application(job_application: models.Application):
    new_job_application = job_db.create_job_application(job_application)
    if new_job_application:
        return JSONResponse(content=new_job_application, status_code=200)
    return JSONResponse(content="Unable to get or create new job_application.", status_code=400)

@app.put("/job/application/{application_id}")
def update_job_application_status(application_id: str, status: str):
    updated_application = job_db.update_job_application_status(application_id, status)
    if updated_application:
        return JSONResponse(content=updated_application, status_code=200)
    return JSONResponse(content=f"Unable to update job_application for application id {application_id}", status_code=400)

@app.get("/job/application/candidate/{candidate_id}")
def view_candidate_job_applications(candidate_id: str):
    job_applications = job_db.view_candidate_job_applications(candidate_id)
    if job_applications:
        return JSONResponse(content=job_applications, status_code=200)
    return JSONResponse(content=f"Unable to get job_application for candidate {candidate_id}", status_code=400)


if __name__ == "__main__":
    print("Service started!")
    uvicorn.run("main:app", host="0.0.0.0", port=8083, reload=True)

