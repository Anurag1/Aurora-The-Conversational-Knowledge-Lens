from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, asdict
from typing import Iterable

STOPWORDS = {
    "the", "a", "an", "and", "or", "to", "of", "in", "on", "for", "is",
    "are", "was", "were", "be", "because", "but", "that", "this", "it", "as",
    "with", "by", "at", "from", "they", "their", "we", "you", "i", "he", "she",
}

@dataclass(frozen=True)
class Insight:
    kind: str
    text: str
    confidence: float


def _tokens(text: str) -> list[str]:
    return [t.lower() for t in re.findall(r"[A-Za-z][A-Za-z'-]{2,}", text)]


def _concepts(text: str) -> set[str]:
    return {t for t in _tokens(text) if t not in STOPWORDS}


def analyze_conversation(messages: Iterable[dict]) -> dict:
    messages = list(messages)
    by_speaker: dict[str, list[str]] = {}
    for message in messages:
        speaker = str(message.get("speaker", "unknown"))
        by_speaker.setdefault(speaker, []).append(str(message.get("text", "")))

    speakers = list(by_speaker)
    if len(speakers) < 2:
        return {"assumptions": [], "contradictions": [], "missing": [], "links": [], "emergent_insights": []}

    concepts = {speaker: set().union(*(_concepts(t) for t in texts)) for speaker, texts in by_speaker.items()}
    shared = set.intersection(*(concepts[s] for s in speakers)) if speakers else set()
    union = set.union(*(concepts[s] for s in speakers)) if speakers else set()

    insights: list[Insight] = []

    # Contradiction heuristic: opposing cue words in adjacent turns.
    contradiction_pairs = [("good", "pollution"), ("safe", "dangerous"), ("always", "never"),
                           ("true", "false"), ("increase", "decrease"), ("clean", "dirty")]
    all_text = " ".join(t.lower() for ts in by_speaker.values() for t in ts)
    found_pairs = [p for p in contradiction_pairs if p[0] in all_text and p[1] in all_text]
    for a, b in found_pairs:
        insights.append(Insight("contradiction", f"Potential tension between '{a}' and '{b}'.", 0.72))

    # Missing-context heuristic: causal claims without an explicit boundary/metric.
    causal = any(w in all_text for w in ("because", "therefore", "causes", "leads to"))
    if causal and not any(w in all_text for w in ("metric", "lifecycle", "scope", "boundary", "timeframe")):
        insights.append(Insight("missing", "The causal claim lacks an explicit metric, scope, or system boundary.", 0.68))

    if shared:
        ranked = Counter(_tokens(" ".join(ts) for ts in by_speaker.values()))
        shared_ranked = sorted(shared, key=lambda x: ranked[x], reverse=True)[:8]
        insights.append(Insight("shared_assumption", f"Both participants discuss shared concepts: {', '.join(shared_ranked)}.", 0.61))

    # Emergent connection: concepts unique to each participant that can be paired.
    if len(speakers) >= 2:
        left = concepts[speakers[0]] - concepts[speakers[1]]
        right = concepts[speakers[1]] - concepts[speakers[0]]
        if left and right:
            pair = (sorted(left)[0], sorted(right)[0])
            insights.append(Insight("emergent_link", f"Potential cross-mind connection: '{pair[0]}' ↔ '{pair[1]}'.", 0.55))

    return {
        "assumptions": [asdict(i) for i in insights if i.kind == "shared_assumption"],
        "contradictions": [asdict(i) for i in insights if i.kind == "contradiction"],
        "missing": [asdict(i) for i in insights if i.kind == "missing"],
        "links": [asdict(i) for i in insights if i.kind == "emergent_link"],
        "emergent_insights": [asdict(i) for i in insights],
    }
