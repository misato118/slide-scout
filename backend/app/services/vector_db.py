import chromadb
from chromadb.api import ClientAPI

class VectorDBService:
    _client: ClientAPI | None = None

    @classmethod
    def get_client(cls) -> ClientAPI:
        if cls._client is None:
            cls._client = chromadb.HttpClient(host="localhost", port=8001)
        return cls._client