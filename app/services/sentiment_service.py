from app.graph.builder import build_graph

graph = build_graph()

def analyze_message(message: str):
    return graph.invoke({"raw_text": message})

def analyze_batch(messages: list[str]):
    results = []
    for msg in messages:
        results.append(analyze_message(msg))
    return results
