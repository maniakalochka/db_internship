from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv

#  Load environment variables from .env file
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)



class Settings(BaseSettings):
    DB_URL: str

    class Config:
        env_file = Path(__file__).resolve().parents[1] / ".env"

settings = Settings()  #type: ignore
