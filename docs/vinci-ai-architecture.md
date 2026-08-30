# VINCI AI — The Unseen Between Minds

## Purpose

VINCI AI analyses communication between two people or agents to expose information that is implicit rather than explicitly stated: assumptions, contradictions, missing context, conceptual divergence, and genuinely emergent ideas.

The design in this document is adapted from the supplied VINCI AI architecture poster and expressed as an implementable research prototype.

## Core model

Let `K_A` and `K_B` be the current knowledge states of two participants and `C` be their communication:

`K_new = f(K_A, K_B, C)`

The interaction is treated as a transformation of the participants' knowledge states rather than merely a transcript-processing task.

## Pipeline

1. **Capture** — accept text, voice, gestures, drawings, media, questions, examples, corrections, and contextual signals.
2. **Mind modelling** — maintain compact, time-aware models for each participant: beliefs, experiences, goals, biases, language style, and thinking patterns.
3. **Interaction analysis** — extract semantic units and dialogue acts; detect assumptions, contradictions, information flow, alignment, and divergence.
4. **Emergence engine** — search for gaps, hidden links, hypothesis opportunities, and concepts that arise only through interaction.
5. **Knowledge extraction** — output emergent insights, new questions, novel concepts, hypotheses, and actionable ideas.
6. **Validation and ranking** — score evidence, uncertainty, contradiction strength, novelty, and usefulness.
7. **Learning** — update participant models and interaction memory after validation.

## Unseen layer

For every interaction the system should explicitly represent:

- **Implicit assumptions** — claims treated as true but not stated.
- **Shared assumptions** — beliefs both parties rely on without checking.
- **Contradictions** — incompatibilities within or across participant models.
- **Missing pieces** — information likely relevant to the decision but absent from the conversation.
- **New connections** — links that become salient only when two knowledge graphs interact.
- **Thinking shifts** — measurable changes in hypotheses, confidence, goals, or concepts over time.
- **Emergent knowledge** — information not attributable to a single participant's pre-existing state.

## Minimal data contract

```json
{
  "conversation_id": "string",
  "participants": ["A", "B"],
  "messages": [],
  "mind_models": {
    "A": {"beliefs": [], "goals": [], "concepts": []},
    "B": {"beliefs": [], "goals": [], "concepts": []}
  },
  "unseen": {
    "assumptions": [],
    "contradictions": [],
    "missing": [],
    "links": [],
    "emergent_insights": []
  }
}
```

## Example

Participant A: “Electric cars are good for the environment because they do not use fuel.”

Participant B: “True, but battery production creates pollution.”

A useful unseen analysis can identify the hidden assumption that tailpipe emissions are the only environmental variable, the missing lifecycle boundary, and the emergent question: **Which comparison metric and system boundary should define environmental impact?**

## Research position

This repository should be treated as a research prototype. Claims of novelty or superiority must be demonstrated experimentally against explicit baselines.

## Next validation milestones

- deterministic unit tests for assumption and contradiction extraction;
- synthetic conversation benchmark with known unseen facts;
- graph-based representation of participant concepts;
- ablation studies for mind modelling and the emergence layer;
- human evaluation of usefulness and novelty;
- optional LLM-backed analyzers behind a provider interface.
