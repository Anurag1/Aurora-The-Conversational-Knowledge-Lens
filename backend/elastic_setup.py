from elasticsearch import Elasticsearch
import json
from config import ELASTIC_URL, ELASTIC_API_KEY

INDEX_NAME = "aurora-index"

def setup_index():
    es = Elasticsearch(ELASTIC_URL, api_key=ELASTIC_API_KEY)

    mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "integer"},
                "content": {"type": "text"},
                "content_vector": {"type": "dense_vector", "dims": 768}
            }
        }
    }

    if es.indices.exists(index=INDEX_NAME):
        print(f"Index '{INDEX_NAME}' already exists.")
    else:
        es.indices.create(index=INDEX_NAME, body=mapping)
        print(f"Created index '{INDEX_NAME}'")

    with open("../data/sample_docs.json", "r") as f:
        docs = json.load(f)

    for doc in docs:
        doc["content_vector"] = [0.01] * 768
        es.index(index=INDEX_NAME, document=doc)

    print(f"Indexed {len(docs)} documents.")

if __name__ == "__main__":
    setup_index()
