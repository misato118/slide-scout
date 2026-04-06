from fastapi import FastAPI
from app.services.vector_db import VectorDBService

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test-chroma")
async def test_chroma():
    try:
        chroma_client = VectorDBService.get_client()
        collection = chroma_client.get_or_create_collection(name="my_test_collection")
        collection.upsert(
            documents=[
                "This is a document about pineapple",
                "This is a document about oranges",
            ],
            ids=["id1", "id2"],
        )

        results = collection.query(
            query_texts=["This is a query document about hawaii"],
            n_results=2,
        )

        return {
            "status": "success",
            "message": "Chroma test successful",
            "results": results,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}