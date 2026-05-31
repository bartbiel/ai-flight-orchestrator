from retrieval.airport_repository import AirportRepository


class AirportResolver:

    def __init__(self):
        self.repository = AirportRepository()

    def resolve(self, prompt: str):

        return self.repository.find_by_prompt(prompt)