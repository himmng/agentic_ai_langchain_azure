from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    azure_openai_endpoint: str
    azure_openai_deployment: str
    azure_openai_api_version: str
    azure_openai_api_key: str

    class Config:
        env_file = ".env"

settings = Settings()
