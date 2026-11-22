from pydantic import BaseModel, Field


class AgentRequest(BaseModel):

    question: str 


class AgentResponse(BaseModel):

    question: str

    answer: str