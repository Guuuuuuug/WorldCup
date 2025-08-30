from __future__ import annotations
from functools import lru_cache
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_PATH = Path(__file__).with_name(".env")

class Settings(BaseSettings):

    database_url: str = Field(..., alias='DATABASE')
    secret_key: str = Field(..., alias="SECRET_KEY")
    algorithm: str = Field('HS256', alias="ALGORITHM")
    access_t_time: int = Field(50, alias="ACCESS_T_EXP")

    model_config = SettingsConfigDict(
        env_file=str(ENV_PATH),
        env_file_encoding='utf-8',
        populate_by_name=True,
        extra='ignore',
    )

@lru_cache()
def get_settings() -> Settings:
    s = Settings()
    return s
    