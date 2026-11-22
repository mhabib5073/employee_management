from fastapi import FastAPI

from app.api.agent_router import router


app = FastAPI(
    title="Employee AI Agent",
    description="AI Agent for Employee Management",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
async def root():

    return {
        "message": "Employee AI Agent is running"
    }