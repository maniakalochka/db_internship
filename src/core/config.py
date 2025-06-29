from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

#  Load environment variables from .env file
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    DB_URL: str

    class Config:
        env_file = env_path


settings = Settings()  # type: ignore
