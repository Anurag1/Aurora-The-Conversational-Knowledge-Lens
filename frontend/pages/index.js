import { useState } from "react";
import axios from "axios";
import GraphVisualization from "../components/GraphVisualization";

export default function Home() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState(null);

  async function ask() {
    const res = await axios.post("/api/query", { query });
    setResponse(res.data);
  }

  return (
    <main className="p-6 font-sans">
      <h1 className="text-3xl font-bold mb-4">Aurora: The Conversational Knowledge Lens</h1>
      <input className="border p-2 w-2/3" value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Ask a question..." />
      <button className="bg-green-600 text-white px-4 py-2 ml-2 rounded" onClick={ask}>Ask Aurora</button>
      {response && (
        <section className="mt-6">
          <h2 className="font-semibold">Summary:</h2>
          <p className="whitespace-pre-wrap">{response.summary}</p>
          <GraphVisualization data={{ nodes: [{ id: "Query" }], links: [] }} />
        </section>
      )}
    </main>
  );
}
