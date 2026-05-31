from pathlib import Path

import pandas as pd

from retrieval.airport_models import AirportResponse




class AirportRepository:

    def __init__(self):

        csv_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "airports.csv"
        )

        self.df = pd.read_csv(csv_path)

    def find_by_prompt(
        self,
        prompt: str
    ) -> list[AirportResponse]:

        query = prompt.strip().lower()

        name_matches = self.df[
            self.df["name"]
            .fillna("")
            .str.lower()
            .str.contains(query, na=False)
        ]

        city_matches = self.df[
            self.df["city"]
            .fillna("")
            .str.lower()
            .str.contains(query, na=False)
        ]

        icao_matches = self.df[
            self.df["icao"]
            .fillna("")
            .str.lower()
            == query
        ]

        iata_matches = self.df[
            self.df["code"]
            .fillna("")
            .str.lower()
            == query
        ]

        city_code_matches = pd.DataFrame()

     

        matches = pd.concat(
            [
                name_matches,
                city_matches,
                icao_matches,
                iata_matches,
                city_code_matches,
            ]
        ).drop_duplicates()

        airports = []

        for _, row in matches.iterrows():

            airports.append(
                AirportResponse(
                    code=str(row["code"]),
                    icao=str(row["icao"]),
                    name=str(row["name"]),
                    latitude=float(row["latitude"]),
                    longitude=float(row["longitude"]),
                    country=str(row["country"]),
                    city=str(row["city"]),
                )
            )

        return airports