from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = "postgresql+psycopg2://nutri:nutri@localhost:5432/nutri"
    JWT_SECRET: str = "troque-isto"
    JWT_EXPIRES_MIN: int = 60 * 24
    
    class Config:
        env_file = ".env"
    
settings = Settings()