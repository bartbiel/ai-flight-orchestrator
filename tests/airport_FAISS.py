import json

from retrieval.airport_FAISS import AirportFAISS


def main():

    faiss = AirportFAISS()

    while True:

        query = input(
            "\nEnter airport query (or 'exit'): "
        )

        if query.lower() == "exit":
            break

        results = faiss.search(
            query=query,
            k=5
        )

        output = []

        for doc in results:

            metadata = doc.metadata

            output.append(
                {
                    "code": metadata.get("code"),
                    "icao": metadata.get("icao"),
                    "name": metadata.get("name"),
                    "latitude": metadata.get("latitude"),
                    "longitude": metadata.get("longitude"),
                    "country": metadata.get("country"),
                    "city": metadata.get("city"),
                }
            )

        print(
            json.dumps(
                output,
                indent=4,
                ensure_ascii=False
            )
        )


if __name__ == "__main__":
    main()