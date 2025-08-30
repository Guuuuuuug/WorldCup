from sqlmodel import Session, select
from typing import List
from sqlalchemy import func

from worldcup.models import WorldCup
from worldcup.schemas import WorldCupCreate, CountryWins, CountryRunnerUps, CountryThirdPlaces

def get_all_worldcups(session: Session) -> List[WorldCup]:
    return session.exec(select(WorldCup)).all()

def create_worldcup(world_data:WorldCupCreate, session:Session) -> WorldCup:
    worldcup = WorldCup.from_orm(world_data)
    session.add(worldcup)
    session.commit()
    session.refresh(worldcup)
    return worldcup

def get_wins_by_country(session: Session) -> List[CountryWins]:
    stmt = (
        select(WorldCup.winner, func.count().label("titles"), func.array_agg(WorldCup.year).label('year'))
        .where(WorldCup.winner.is_not(None))
        .group_by(WorldCup.winner)
        .order_by(func.count().desc(), WorldCup.winner)
    )

    rows = session.exec(stmt).all()
    return [CountryWins(country=winner, titles=titles, year=year) for winner, titles, year in rows]

def get_runnerups_by_country(session:Session) -> List[CountryRunnerUps]:
    stmt = (
        select(WorldCup.runner_up, func.count().label("silver"), func.array_agg(WorldCup.year).label('years'))
        .where(WorldCup.runner_up.is_not(None))
        .group_by(WorldCup.runner_up)
        .order_by(func.count().desc(), WorldCup.runner_up)
    )
    rows = session.exec(stmt).all()
    return [CountryRunnerUps(country=country, silver=silver, years=years) for country, silver, years in rows]

def get_thirdplaces_by_country(session:Session) -> List[CountryThirdPlaces]:
    stmt = (
        select(WorldCup.third_place, func.count().label('bronze'), func.array_agg(WorldCup.year).label('years'))
        .where(WorldCup.runner_up.is_not(None))
        .group_by(WorldCup.third_place)
        .order_by(func.count().desc(), WorldCup.third_place)
    )
    rows = session.exec(stmt).all()
    return [CountryThirdPlaces(country=country, bronze=bronze, years=years) for country, bronze, years in rows]