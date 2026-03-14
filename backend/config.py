from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    SECRET_KEY: str = Field(..., env='SECRET_KEY')
    DATABASE_URL: str = Field(..., env='DATABASE_URL')

    class Config:
        env_file = '.env'