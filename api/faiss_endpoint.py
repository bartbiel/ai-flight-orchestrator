from fastapi import APIRouter
import pandas as pd

from orchestration.FAISS_resolver import FaissResolver
from retrieval.airport_FAISS import AirportFAISS

router = APIRouter()

resolver = FaissResolver(
    AirportFAISS()
)


@router.get("/FAISSsearch")
def search(
    query: str,
    k: int = 4
):

    docs = resolver.resolve(
        query=query,
        k=k
    )

    return [
        {
            key: (
                None if pd.isna(value)
                else str(value)
            )
            for key, value in doc.metadata.items()
        }
        for doc in docs
    ]