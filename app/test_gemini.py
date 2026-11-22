
import asyncio

from google import genai
from google.genai.errors import ServerError
from app.core.config import settings


async def test_gemini():

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    print("Model:", settings.GEMINI_MODEL)

    try:
        for attempt in range(3):
            try:
                response = await client.aio.models.generate_content(
                    model=settings.GEMINI_MODEL,
                    contents="Explain FastAPI in 3 lines."
                )

                print("\nGemini Response:")
                print(response.text)
                return

            except ServerError as error:
                if error.code != 503 or attempt == 2:
                    raise

                wait_time = 2 ** (attempt + 1)
                print(f"Gemini unavailable. Retrying in {wait_time}s...")
                await asyncio.sleep(wait_time)

    finally:
        await client.aio.aclose()


if __name__ == "__main__":
    asyncio.run(test_gemini())
