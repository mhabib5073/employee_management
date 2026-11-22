
import httpx
from urllib.parse import quote

from app.core.config import settings


async def make_employee_request(
    endpoint: str,
    authorization: str | None = None
):
    headers = {}

    if authorization:
        headers["Authorization"] = authorization

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{settings.EMPLOYEE_API_BASE_URL}{endpoint}",
            headers=headers
        )

        response.raise_for_status()
        return response.json()


async def get_all_employees(authorization=None):
    return await make_employee_request(
        "/employee/all",
        authorization
    )


async def get_employee_by_id(emp_id: int, authorization=None):
    return await make_employee_request(
        f"/employee/{emp_id}",
        authorization
    )


async def get_employee_by_email(email: str, authorization=None):
    encoded_email = quote(email, safe="")

    return await make_employee_request(
        f"/employee/email/{encoded_email}",
        authorization
    )


async def get_employees_by_department(authorization=None):
    return await make_employee_request(
        "/employee/departments",
        authorization
    )
