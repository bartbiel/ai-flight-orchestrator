from langchain_community.vectorstores import FAISS


class FaissRepository:

    def __init__(self, embeddings):

        self.vectorstore = FAISS.load_local(
            "faiss_index",
            embeddings,
            allow_dangerous_deserialization=True
        )

    def search(
        self,
        query: str,
        k: int = 5
    ):
        return self.vectorstore.similarity_search(
            query=query,
            k=k
        )