from typing import Optional, List
from sqlmodel import SQLModel

class WorldCupBase(SQLModel):
    year: int
    host: str
    winner: str
    runner_up: str
    third_place: Optional[str] = None
    final_score: str
    stadium: str
    referee: Optional[str] = None
    attendance: Optional[int] = None
    image_url: Optional[str] = None
    continent: Optional[str] = None

class WorldCupCreate(WorldCupBase):
    pass

class WorldCupRead(WorldCupBase):
    host: Optional[str] = None
    winner: Optional[str] = None
    runner_up: Optional[str] = None
    final_score: Optional[str] = None
    stadium: Optional[str] = None
    # the already-optional fields can stay as-is
    id: int

    class Config:
        from_attributes = True  

class CountryWins(SQLModel):
    country: str
    titles: int
    year: List[int]

class CountryRunnerUps(SQLModel):
    country: str
    silver: int
    years: List[int]

class CountryThirdPlaces(SQLModel):
    country: str
    bronze: int
    years: List[int]
