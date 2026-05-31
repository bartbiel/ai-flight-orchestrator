from retrieval.airport_FAISS import AirportFAISS


class FaissResolver:

    def __init__(self, repository: AirportFAISS):

        self.repository = repository

    def resolve(
        self,
        query: str,
        k: int = 5
    ):
        return self.repository.search(
            query=query,
            k=k
        )