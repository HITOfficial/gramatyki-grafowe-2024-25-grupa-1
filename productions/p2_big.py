from GramatykiGrafowe import Graph, Node, NodeQ, Production
from p2 import create_left_graph, transition, predicate

def create_start_graph():
    graph = Graph()

    v1 = Node(label="1", x=0, y=0, h=False, )
    v2 = Node(label="2", x=10, y=0, h=False)
    v3 = Node(label="3", x=10, y=10, h=False)
    v4 = Node(label="4", x=0, y=10, h=False)
    v5 = Node(label="5", x=0, y=-5, h=True)
    v6 = Node(label="6", x=-10, y=10, h=False)
    v7 = Node(label="7", x=-5, y=0, h=True)
    v8 = Node(label="8", x=-10, y=0, h=False)
    v9 = Node(label="9", x=-10, y=-10, h=False)
    v10 = Node(label="10", x=0, y=-10, h=False)
    v12 = Node(label="12", x=10, y=-10, h=False)
    q1 = NodeQ(x=5, y=-5, R=True)
    q2 = NodeQ(x=-5, y=5, R=True)

    nodes = [
        v1, v2, v3, v4,
        v5, v6, v7, v8,
        v9, v10, v12,
        q1, q2]

    for node in nodes:
        graph.add_node(node)

    edges = [
        (v1, v2, False),
        (v2, v3, True),
        (v3, v4, True),
        (v4, v1, False),

        (v1, q1, None),
        (v2, q1, None),
        (v12, q1, None),
        (v10, q1, None),

        (v6, v8, True),
        (v8, v7, False),
        (v7, v1, False),
        (v4, v6, True),
        (v9, v10, True),

        (v12, v2, True),
        (v8, v9, True),
        (v5, v1, False),
        (v5, v10, False),
        (v10, v12, True),

        (v4, q2, None),
        (v6, q2, None),
        (v8, q2, None),
        (v1, q2, None)
    ]

    for node1, node2, B in edges:
        graph.add_edge(node1, node2, B)

    return graph


if __name__ == "__main__":

    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    
    while graph.apply_production(production):
        pass
    
    
    graph.show()
