from elasticsearch import Elasticsearch
from config import ELASTIC_URL, ELASTIC_API_KEY

es = Elasticsearch(ELASTIC_URL, api_key=ELASTIC_API_KEY)

def hybrid_search(query: str):
    body = {
        "query": {
            "bool": {
                "should": [
                    {"match": {"content": query}},
                    {"knn": {"content_vector": {"vector": [0.1]*768, "k": 5}}}
                ]
            }
        }
    }
    res = es.search(index="aurora-index", body=body)
    return [hit["_source"] for hit in res["hits"]["hits"]]
