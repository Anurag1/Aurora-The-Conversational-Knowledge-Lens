from pprint import pprint

from vinci_ai import analyze_conversation

conversation = [
    {"speaker": "A", "text": "Electric cars are good for the environment because they do not use fuel."},
    {"speaker": "B", "text": "True, but battery production creates pollution."},
]

if __name__ == "__main__":
    pprint(analyze_conversation(conversation), sort_dicts=False)
