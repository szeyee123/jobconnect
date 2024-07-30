
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import dao.candidate as candidate_db
from fastapi.responses import JSONResponse
import models.models as models

app = FastAPI(docs_url="/candidate/swagger")

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/candidate")
async def root():
    return {"message": "hello candidate"}

@app.get("/candidate/getall")
async def root():
    print("/getall: triggered")
    data = candidate_db.get_all()
    return JSONResponse(status_code=200, content=data)

@app.get("/candidate/{candidate_id}")
def get_candidate(candidate_id: str ,):
    candidate = candidate_db.get_candidate_by_id(candidate_id)
    if candidate:
        return JSONResponse(content=candidate, status_code=200)
    return JSONResponse(content="candidate not found.", status_code=400)

@app.post("/candidate/login", response_model=models.User)
def login(credentials: models.CandidateLogin):
    user = candidate_db.login(credentials.email, credentials.password)
    if user:
        return user
    return JSONResponse(content="Unable to login", status_code=400)

@app.post("/candidate")
def create_candidate(candidate: models.Candidate):
    new_candidate = candidate_db.create_candidate(candidate)
    if new_candidate:
        return JSONResponse(content=new_candidate, status_code=200)
    return JSONResponse(content="Unable to get or create new candidate.", status_code=400)

@app.put("/candidate")
def update_candidate(candidate: models.Candidate):
    updated_candidate = candidate_db.modify_candidate(candidate)
    if updated_candidate:
        return JSONResponse(content=updated_candidate, status_code=200)
    return JSONResponse(content="Unable to update candidate profile.", status_code=400)


if __name__ == "__main__":
    print("Service started!")
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)

