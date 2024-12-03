from GramatykiGrafowe import Graph, Node, NodeQ, Production


def predicate(get_node):
    p = get_node(6)
    q = get_node(7)
    v5 = get_node(5)
    return not p.R and q.R and v5.h


def transition(g: Graph, get_node):
    p = get_node(6)
    p.R = True


def create_left_graph():
    graph = Graph()

    v1 = Node(id=1)
    v2 = Node(id=2)
    v3 = Node(id=3)
    v4 = Node(id=4)
    v5 = Node(id=5)
    p = Node(id=6)
    q = Node(id=7)
    v6 = Node(id=8)
    v7 = Node(id=9)
    v8 = Node(id=10)
    
    nodes = [v1, v2, v3, v4, v5, q, p, v6, v7, v8]

    for node in nodes:
        graph.add_node(node)

    edges = [
        (v2, v5, None),
        (v5, v3, None),
        (v1, p, None),
        (v2, p, None),
        (v3, p, None),
        (v4, p, None),
        (v8, p, None),
        (v3, q, None),
        (v5, q, None),
        (v6, q, None),
        (v7, q, None),
    ]

    for node1, node2, B in edges:
        graph.add_edge(node1, node2, B)

    return graph


def create_start_graph():
    graph = Graph()

    v1 = Node(label="1", x=0, y=0, h=False)
    v2 = Node(label="2", x=10, y=0, h=False)
    v3 = Node(label="3", x=10, y=10, h=False)
    v4 = Node(label="4", x=0, y=10, h=False)
    v5 = Node(label="5", x=10, y=5, h=True)
    p = NodeQ(label="P", x=5, y=5, R=False)
    v8 = Node(label="8", x=5, y=0, h=True)
    q = NodeQ(label="Q", x=15, y=7.5, R=True)
    v6 = Node(label="6", x=20, y=5, h=True)
    v7 = Node(label="7", x=20, y=10, h=True)

    nodes = [v1, v2, v3, v4, v5, q, p, v6, v7, v8]

    for node in nodes:
        graph.add_node(node)

    edges = [
        (v2, v5, None),
        (v5, v3, None),
        (v1, p, None),
        (v2, p, None),
        (v3, p, None),
        (v4, p, None),
        (v8, p, None),
        (v3, q, None),
        (v5, q, None),
        (v6, q, None),
        (v7, q, None),
    ]

    for node1, node2, B in edges:
        graph.add_edge(node1, node2, B)

    return graph


if __name__ == "__main__":

    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)
    graph.show()
