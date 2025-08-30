from sqlmodel import SQLModel, Field
from typing import Optional

class WorldCup(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    year: int = Field(index=True, unique=True)
    host: Optional[str] = None
    winner: Optional[str] = None
    runner_up: Optional[str] = None
    third_place: Optional[str] = None
    final_score: Optional[str] = None
    stadium: Optional[str] = None
    referee: Optional[str] = None
    attendance: Optional[int] = None
    image_url: Optional[str] = None
    continent: Optional[str] = None