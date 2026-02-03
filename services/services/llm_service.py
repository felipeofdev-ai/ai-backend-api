from config.settings import settings
from config.logger import logger
from openai import OpenAI

class LLMService:
    def __init__(self):
        api_key = settings.openai_api_key
        if not api_key:
            logger.error("OPENAI_API_KEY not found in environment variables")
            raise ValueError("OPENAI_API_KEY not found in environment variables")

        self.client = OpenAI(api_key=api_key)
        logger.info("LLMService initialized successfully")

    def generate_response(self, prompt: str) -> str:
        logger.info(f"Generating response for prompt: {prompt[:50]}...")
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        result = response.choices[0].message.content
        logger.info("Response generated successfully")
        return result
