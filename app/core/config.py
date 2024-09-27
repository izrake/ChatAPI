from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Qwen Coder API"
    MODEL_NAME: str = "Qwen/Qwen2.5-Coder-7B-Instruct"

    class Config:
        env_file = ".env"

settings = Settings()