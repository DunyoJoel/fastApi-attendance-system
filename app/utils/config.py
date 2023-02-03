import os
from typing import Optional
from pydantic import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv, find_dotenv
import secrets

load_dotenv(find_dotenv())


class settings (BaseSettings):
    PROJECT_NAME: str = "ATTENDANCE SYSTEM"
    SQLALCHEMY_DATABASE_URL: str = os.environ.get("DATABASE_URL")

    if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)




    class Config:
       case_sensitive = True
       env_file = '.env'

@lru_cache()
def get_settings():
    return settings()
settings  = get_settings()
