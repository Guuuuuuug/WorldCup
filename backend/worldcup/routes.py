from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from database import engine
from worldcup.schemas import WorldCupRead, WorldCupCreate, CountryWins, CountryRunnerUps, CountryThirdPlaces
from worldcup.services import get_all_worldcups, create_worldcup, get_wins_by_country, get_runnerups_by_country, get_thirdplaces_by_country

router = APIRouter(prefix='/worldcups', tags=['World Cups'])

def get_session():
    with Session(engine) as session:
        yield session


@router.get('/', response_model=List[WorldCupRead])
def read_worldcups(session: Session = Depends(get_session)):
    return get_all_worldcups(session)


@router.post('/', response_model=WorldCupRead, status_code=status.HTTP_201_CREATED)
def add_worldcup(worldcup: WorldCupCreate, session: Session = Depends(get_session)):
    return create_worldcup(worldcup, session)

@router.get('/wins', response_model=List[CountryWins])
def worldcup_wins(session:Session = Depends(get_session)):
    return get_wins_by_country(session)

@router.get('/runnerups', response_model=List[CountryRunnerUps])
def world_runnerups(session: Session = Depends(get_session)):
    return get_runnerups_by_country(session)

@router.get('/thirdplaces', response_model=List[CountryThirdPlaces])
def worldcup_thirdplaces(session:Session = Depends(get_session)):
    return get_thirdplaces_by_country(session)