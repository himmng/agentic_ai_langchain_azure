from langgraph.graph import StateGraph, END
from app.graph.state import SentimentState
from app.graph.nodes import preprocess_node, sentiment_node

def build_graph():
    builder = StateGraph(SentimentState)

    builder.add_node("preprocess", preprocess_node)
    builder.add_node("sentiment", sentiment_node)

    builder.set_entry_point("preprocess")
    builder.add_edge("preprocess", "sentiment")
    builder.add_edge("sentiment", END)

    return builder.compile()
