# orchestration/rag_resolver.py

class RagResolver:

    def __init__(
        self,
        faiss_repository,
        llm
    ):
        self.faiss_repository = faiss_repository
        self.llm = llm

    def answer(
        self,
        query: str
    ):

        docs = self.faiss_repository.search(
            query=query,
            k=5
        )

        context = "\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = f"""
Question:
{query}

Context:
{context}

Answer using only the context.
"""

        return {
    "answer": self.llm.invoke(prompt),
    "sources": [
        doc.metadata
        for doc in docs
    ]
}