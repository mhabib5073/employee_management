# import asyncio

# from openai import AsyncOpenAI
# from core.config import settings


# async def test_openai():

#     client = AsyncOpenAI(
#         api_key=settings.OPENAI_API_KEY
#     )

#     response = await client.responses.create(
#         model=settings.OPENAI_MODEL,
#         input="Reply with OK"
#     )

#     print(response.output_text)


# asyncio.run(test_openai())

import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_llm(question: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )
    return response.text