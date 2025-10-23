from fastapi import FastAPI, Body
from elastic_connector import hybrid_search
from vertex_pipeline import summarize_with_gemini

app = FastAPI(title="Aurora AI Backend")

@app.get("/")
def home():
    return {"status": "Aurora backend running"}

@app.post("/query")
def query_endpoint(query: str = Body(..., embed=True)):
    results = hybrid_search(query)
    summary = summarize_with_gemini(query, results)
    return {"query": query, "summary": summary, "results": results}
