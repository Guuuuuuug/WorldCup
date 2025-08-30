from sqlmodel import SQLModel
from database import engine
from worldcup.models import WorldCup

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("Database tables created.")

if __name__ == "__main__":
    create_db_and_tables()