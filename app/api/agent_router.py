import logging

from fastapi import APIRouter, HTTPException, Header

from app.schemas.agent_schema import (
    AgentRequest,
    AgentResponse
)

from app.agents.employee_agent import run_employee_agent


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/agent",
    tags=["Employee Agent"]
)


@router.post("/ask", response_model=AgentResponse)
async def ask_employee_agent(
    request: AgentRequest,
    authorization: str | None = Header(default=None)
):

    try:

        answer = await run_employee_agent(
            request.question,
            authorization
        )

        return AgentResponse(
            question=request.question,
            answer=answer
        )

    except Exception as exc:

        logger.exception("Employee Agent execution failed")

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )
