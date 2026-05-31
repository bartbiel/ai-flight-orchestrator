from fastapi import FastAPI

from api.airport_endpoint import router as airport_router
from api.faiss_endpoint import router as faiss_router
from api.rag_endpoint import router as rag_router

app = FastAPI()

app.include_router(airport_router)
app.include_router(faiss_router)
app.include_router(rag_router)