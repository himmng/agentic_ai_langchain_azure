from langchain_openai import AzureChatOpenAI
from app.config.settings import settings

def get_llm(temperature: float = 0.0):
    return AzureChatOpenAI(
        azure_endpoint=settings.azure_openai_endpoint,
        azure_deployment=settings.azure_openai_deployment,
        api_version=settings.azure_openai_api_version,
        api_key=settings.azure_openai_api_key,
        temperature=temperature,
    )
