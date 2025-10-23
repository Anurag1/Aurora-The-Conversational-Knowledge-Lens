from google.cloud import aiplatform
from config import GCP_PROJECT, GCP_LOCATION

aiplatform.init(project=GCP_PROJECT, location=GCP_LOCATION)

def summarize_with_gemini(query, results):
    text_block = "\n\n".join([r.get("content", "") for r in results])
    return f"Aurora summary for '{query}' based on {len(results)} documents:\n\n{text_block[:500]}..."
