from pathlib import Path
import time

import pandas as pd

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


class AirportFAISS:

    def __init__(self):

        start_time = time.time()

        csv_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "airports.csv"
        )

        self.df = pd.read_csv(csv_path)

        print(
            f"Loaded {len(self.df)} airports from CSV"
        )

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.index_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "faiss_airports"
        )

        if self.index_path.exists():

            print("Loading existing FAISS index...")

            self.vectorstore = FAISS.load_local(
                str(self.index_path),
                self.embeddings,
                allow_dangerous_deserialization=True
            )

        else:

            print("Building FAISS index...")

            self.vectorstore = self._build_vectorstore()

            self.vectorstore.save_local(
                str(self.index_path)
            )

            print(
                f"FAISS index saved to: {self.index_path}"
            )

        elapsed = time.time() - start_time

        print(
            f"FAISS ready in {elapsed:.2f} seconds"
        )

    def _build_vectorstore(self):

        documents = []

        for _, row in self.df.iterrows():

            text = f"""
            Airport: {row['name']}
            City: {row['city']}
            Country: {row['country']}
            ICAO: {row['icao']}
            IATA: {row['code']}
            """

            documents.append(
    Document(
        page_content=text,
        metadata={
            key: (
                None if pd.isna(value)
                else value
            )
            for key, value in row.to_dict().items()
        }
    )
)

        print(
            f"Created {len(documents)} documents"
        )

        return FAISS.from_documents(
            documents,
            self.embeddings
        )

    def search(
        self,
        query: str,
        k: int = 5
    ):

        print(
            f"Searching FAISS for: '{query}' (top {k})"
        )

        results = self.vectorstore.similarity_search(
            query,
            k=k
        )

        print(
            f"Found {len(results)} results"
        )

        return results