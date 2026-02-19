from app.graph.builder import build_graph

def visualize():
    graph = build_graph()
    graph.get_graph().draw_mermaid_png("graph.png")
