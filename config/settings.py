from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Backend API"
    version: str = "1.0.0"
    openai_api_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
