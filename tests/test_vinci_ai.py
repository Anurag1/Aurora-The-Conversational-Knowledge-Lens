from vinci_ai import analyze_conversation


def test_unseen_layer_example():
    messages = [
        {"speaker": "A", "text": "Electric cars are good for the environment because they do not use fuel."},
        {"speaker": "B", "text": "True, but battery production creates pollution."},
    ]
    result = analyze_conversation(messages)
    assert result["contradictions"]
    assert result["missing"]
    assert result["emergent_insights"]


def test_single_speaker_is_safe():
    result = analyze_conversation([{"speaker": "A", "text": "A simple statement."}])
    assert result["emergent_insights"] == []
