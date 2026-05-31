import json

from orchestration.airport_resolver import AirportResolver


def main():

    resolver = AirportResolver()

    while True:

        city = input(
            "\nEnter city name (or 'exit'): "
        ).strip()

        if city.lower() == "exit":
            break

        result = resolver.resolve(city)

        json_result = [
            airport.__dict__
            for airport in result
        ]

        print(
            json.dumps(
                json_result,
                indent=4,
                ensure_ascii=False
            )
        )


if __name__ == "__main__":
    main()