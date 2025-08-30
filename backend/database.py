from sqlmodel import SQLModel, create_engine
from config import get_settings

settings = get_settings()

engine = create_engine(settings.database_url, echo=True)

def create_db_and_tables() -> None:
    from worldcup import models
    SQLModel.metadata.create_all(engine)