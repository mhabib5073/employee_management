
from google import genai

from app.core.config import settings


class GeminiClient:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = settings.GEMINI_MODEL

    async def generate_response(self, prompt: str):

        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text or ""

    async def close(self):
        await self.client.aio.aclose()
