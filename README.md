# Aurora: The Conversational Knowledge Lens

Aurora transforms scattered enterprise data into conversational, visual insight using Elastic Cloud and Google Cloud Vertex AI Gemini.

## VINCI AI — The Unseen Between Minds

This repository now contains a runnable **VINCI AI** research prototype inspired by the supplied architecture: analyze a conversation between two participants and explicitly surface an “unseen layer” of shared assumptions, potential contradictions, missing context, cross-mind links, and emergent insights.

### Prototype status

- Deterministic Python analyzer — implemented.
- Regression tests — implemented.
- GitHub Actions CI — implemented.
- Architecture specification — [`docs/vinci-ai-architecture.md`](docs/vinci-ai-architecture.md).
- Runnable demo — [`scripts/demo.py`](scripts/demo.py).

### Run locally

```bash
python -m pip install -U pytest
pytest -q
python scripts/demo.py
```

The current implementation intentionally uses deterministic heuristics so the baseline is testable and reproducible. LLM, speech, graph-memory, and visualization adapters can be added behind this stable interface in later phases.

## Research direction

VINCI AI treats communication as an interaction between evolving knowledge states. Its long-term objective is to investigate what emerges **between** minds rather than only what each participant explicitly says.

Research claims should be validated through benchmark datasets, ablations, human evaluation, and comparison with transcript-only baselines.
