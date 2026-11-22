
from app.clients.employee_api_client import (
    get_all_employees,
    get_employee_by_id,
    get_employee_by_email,
    get_employees_by_department
)


async def execute_employee_tool(
    tool_name: str,
    arguments: dict,
    authorization: str | None = None
):
    if tool_name == "get_all_employees":
        return await get_all_employees(
            authorization=authorization
        )

    elif tool_name == "get_by_emp_id":
        return await get_employee_by_id(
            emp_id=arguments["emp_id"],
            authorization=authorization
        )

    elif tool_name == "get_by_email":
        return await get_employee_by_email(
            email=arguments["email"],
            authorization=authorization
        )

    elif tool_name == "get_by_department":
        return await get_employees_by_department(
            authorization=authorization
        )

    else:
        raise ValueError(f"Unknown employee tool: {tool_name}")
