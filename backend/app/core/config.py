from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

class Settings(BaseSettings):
    # Database for users, auth, and query history
    APP_DATABASE_URL: str
    
    # Default target database for querying (sample data)
    DEFAULT_TARGET_DB_URL: str
    
    # JWT Settings
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    # LLM Settings (Ollama)
    LLM_PROVIDER: str  # or "openai"
    LLAMA_BASE_URL: str
    LLAMA_MODEL: str
    LLAMA_VERIFY_SSL: bool
    
    # Gemini / OpenAI Settings (optional)
    GOOGLE_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "gpt-3.5-turbo"
    
    # Query Settings
    MAX_QUERY_ROWS: int
    QUERY_TIMEOUT_SECONDS: int

    class Config:
        env_file = ".env"


settings = Settings()
