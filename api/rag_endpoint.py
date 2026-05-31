from fastapi import APIRouter

from orchestration.RAG_resolver import RagResolver
from retrieval.airport_FAISS import AirportFAISS
from providers.mistral_adapter import MistralAdapter

llm = MistralAdapter()

router = APIRouter()

resolver = RagResolver(
    faiss_repository=AirportFAISS(),
    llm=llm
)


@router.get("/RAGsearch")
def rag_search(
    query: str
):

    answer = resolver.answer(
        query=query
    )

    return {
        "query": query,
        "answer": answer
    }