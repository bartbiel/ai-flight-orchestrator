from fastapi import APIRouter

from orchestration.airport_resolver import AirportResolver

router = APIRouter()

resolver = AirportResolver()


@router.get("/airportsCSVLookup")
def search_airports(query: str):

    return [
        airport.model_dump()
        for airport in resolver.resolve(query)
    ]