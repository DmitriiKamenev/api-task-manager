from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Секретный ключ — в реальном проекте брать из .env!
    SECRET_KEY: str = "your-super-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()