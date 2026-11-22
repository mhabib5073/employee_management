
from google.genai import types


EMPLOYEE_TOOLS = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="get_all_employees",
                description="Retrieve all employees from the Employee Management API.",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={}
                )
            ),

            types.FunctionDeclaration(
                name="get_by_emp_id",
                description="Retrieve an employee using employee ID.",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "emp_id": types.Schema(
                            type=types.Type.INTEGER,
                            description="Employee ID"
                        )
                    },
                    required=["emp_id"]
                )
            ),

            types.FunctionDeclaration(
                name="get_by_email",
                description="Retrieve an employee using email address.",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "email": types.Schema(
                            type=types.Type.STRING,
                            description="Employee email address"
                        )
                    },
                    required=["email"]
                )
            ),

            types.FunctionDeclaration(
                name="get_by_department",
                description="Retrieve employees belonging to a department.",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "department": types.Schema(
                            type=types.Type.STRING,
                            description="Department name"
                        )
                    },
                    required=["department"]
                )
            )
        ]
    )
]
