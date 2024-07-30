
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import dao.company as company_db
from fastapi.responses import JSONResponse
import models.models as models

app = FastAPI(docs_url="/company/swagger")

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/company")
async def root():
    return {"message": "hello company"}

@app.get("/company/getall")
async def root():
    print("/getall: triggered")
    data = company_db.get_all()
    return JSONResponse(status_code=200, content=data)

@app.get("/company/{company_id}")
def get_company(company_id: str ,):
    company = company_db.get_company_by_id(company_id)
    if company:
        return JSONResponse(content=company, status_code=200)
    return JSONResponse(content="company not found.", status_code=400)

@app.post("/company/login", response_model=models.User)
def login(credentials: models.CompanyLogin):
    user = company_db.login(credentials.email, credentials.password)
    if user:
        return user
    return JSONResponse(content="Unable to login", status_code=400)

@app.post("/company")
def create_company(company: models.Company):
    new_company = company_db.create_company(company)
    if new_company:
        return JSONResponse(content=new_company, status_code=200)
    return JSONResponse(content="Unable to get or create new company.", status_code=400)

@app.put("/company")
def update_company(company: models.Company):
    updated_company = company_db.modify_company(company)
    if updated_company:
        return JSONResponse(content=updated_company, status_code=200)
    return JSONResponse(content="Unable to update company profile.", status_code=400)


if __name__ == "__main__":
    print("Service started!")
    uvicorn.run("main:app", host="0.0.0.0", port=8084, reload=True)

