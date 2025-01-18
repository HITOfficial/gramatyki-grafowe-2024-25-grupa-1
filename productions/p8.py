from GramatykiGrafowe import Graph, Node, NodeQ, Production

def predicate(get_node):
    v5 = get_node(5)
    q = get_node(6)
    q2 = get_node(7)
    return not q.R and v5.h and q2.R


def transition(g: Graph, get_node):
    q = get_node(6)
    q.R = True
    print('applied p8')


def create_left_graph():
    graph = Graph()

    v1 = Node(id=1)
    v2 = Node(id=2)
    v3 = Node(id=3)
    v4 = Node(id=4)
    v5 = Node(id=5)
    q = NodeQ(id=6)
    q2 = NodeQ(id=7)
    v6 = Node(id=8)
    v7 = Node(id=9)

    nodes = [v1, v2, v3, v4, v5, q, q2, v6, v7]

    for node in nodes:
        graph.add_node(node)

    edges = [
        (v2, v5, None),
        (v5, v3, None),
        (v1, q, None),
        (v2, q, None),
        (v3, q, None),
        (v4, q, None),
        (v3, q2, None),
        (v5, q2, None),
        (v6, q2, None),
        (v7, q2, None),
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
    q = NodeQ(label="Q6", x=5, y=5, R=False)
    q2 = NodeQ(label="Q7", x=15, y=7.5, R=True)
    v6 = Node(label="6", x=20, y=5, h=True)
    v7 = Node(label="7", x=20, y=10, h=True)

    nodes = [v1, v2, v3, v4, v5, q, q2, v6, v7]

    for node in nodes:
        graph.add_node(node)

    edges = [
        (v2, v5, None),
        (v5, v3, None),
        (v1, q, None),
        (v2, q, None),
        (v3, q, None),
        (v4, q, None),
        (v3, q2, None),
        (v5, q2, None),
        (v6, q2, None),
        (v7, q2, None),
    ]

    for node1, node2, B in edges:
        graph.add_edge(node1, node2, B)

    return graph


def producion():
    return Production(create_left_graph(), transition, predicate, 6)


if __name__ == "__main__":
    graph = create_start_graph()
    left_graph = create_left_graph()
    graph.show()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)
    print(applied)
    graph.show()
