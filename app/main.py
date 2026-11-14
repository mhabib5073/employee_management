from fastapi import FastAPI, Depends
from app.database import Base, engine
from app.api.employee_api import router as emp_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def get_health():
    return {"message": "FastAPI server is running"}

app.include_router(emp_router)