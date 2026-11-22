import json
import logging

from google import genai
from google.genai import types

from app.core.config import settings
from app.tools.employee_tools import EMPLOYEE_TOOLS
from app.tools.employee_executor import execute_employee_tool
# from app.tools.employee_tools import execute_employee_tool

logger = logging.getLogger(__name__)

SYSTEM_INSTRUCTIONS = """
You are an Employee Management Assistant.

You can only answer employee data questions
using the available employee tools.

Available operations:
1. Get all employees.
2. Get employee by ID.
3. Get employee by email.
4. Get employees by department.

Rules:
- Select the correct tool based on user intent.
- Never invent employee information.
- Never answer employee data questions without using tools.
- If employee data is not found, clearly explain that.
- Never reveal passwords or sensitive information.
- Summarize API results clearly.
"""


async def run_employee_agent(
    user_message: str,
    authorization: str | None = None
):

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    try:
        contents = [
            types.Content(
                role="user",
                parts=[types.Part(text=user_message)]
            )
        ]

        config = types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTIONS,
            tools=EMPLOYEE_TOOLS,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            )
        )

        for _ in range(4):

            response = await client.aio.models.generate_content(
                model=settings.GEMINI_MODEL,
                contents=contents,
                config=config
            )

            if not response.candidates:
                return "Gemini did not return a response."

            model_content = response.candidates[0].content

            if not model_content:
                return "Gemini returned an empty response."

            function_calls = [
                part.function_call
                for part in model_content.parts
                if part.function_call is not None
            ]

            # No tool call: return the final answer.
            if not function_calls:
                return response.text or "No response generated."

            # Preserve Gemini's function-call response.
            contents.append(model_content)

            function_responses = []

            for function_call in function_calls:

                arguments = dict(function_call.args or {})

                try:
                    result = await execute_employee_tool(
                        function_call.name,
                        arguments,
                        authorization
                    )

                    output = {
                        "success": True,
                        "data": result
                    }

                except Exception:
                    logger.exception(
                        "Employee tool failed: %s",
                        function_call.name
                    )

                    output = {
                        "success": False,
                        "error": "Employee operation failed."
                    }

                function_responses.append(
                    types.Part.from_function_response(
                        name=function_call.name,
                        response=output
                    )
                )

            # Send tool results back to Gemini.
            contents.append(
                types.Content(
                    role="user",
                    parts=function_responses
                )
            )

        raise RuntimeError(
            "Maximum agent tool rounds exceeded."
        )

    finally:
        await client.aio.aclose()