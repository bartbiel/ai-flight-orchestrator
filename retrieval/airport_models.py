from pydantic import BaseModel


class AirportResponse(BaseModel):
    code: str
    icao: str
    name: str
    latitude: float
    longitude: float
    country: str
    city: str