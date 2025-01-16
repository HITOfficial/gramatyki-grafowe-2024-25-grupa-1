from GramatykiGrafowe import Graph, Node, NodeQ, Production


def predicate(get_node):
    v1 = get_node(1)
    v2 = get_node(2)
    v3 = get_node(3)
    v4 = get_node(4)
    q = get_node(5)

    return q.R and not v1.h and not v2.h and not v3.h and not v4.h


def transition(g: Graph, get_node):
    v1 = get_node(1)
    v2 = get_node(2)
    v3 = get_node(3)
    v4 = get_node(4)
    q = get_node(5)

    e12B = g.get_edge_b_value(v1, v2)
    e23B = g.get_edge_b_value(v2, v3)
    e34B = g.get_edge_b_value(v3, v4)
    e41B = g.get_edge_b_value(v4, v1)

    v12 = Node(x=(v1.x + v2.x) / 2, y=(v1.y + v2.y) / 2, h = not e12B)
    v23 = Node(x=(v2.x + v3.x) / 2, y=(v2.y + v3.y) / 2, h = not e23B)
    v34 = Node(x=(v3.x + v4.x) / 2, y=(v3.y + v4.y) / 2, h = not e34B)
    v41 = Node(x=(v4.x + v1.x) / 2, y=(v4.y + v1.y) / 2, h = not e41B)

    v_center = Node(
        x=(v1.x + v2.x + v3.x + v4.x) / 4,
        y=(v1.y + v2.y + v3.y + v4.y) / 4,
        h=False)

    g.remove_edge(v1, v2)
    g.remove_edge(v2, v3)
    g.remove_edge(v3, v4)
    g.remove_edge(v4, v1)
    g.remove_edge(v1, q)
    g.remove_edge(v2, q)
    g.remove_edge(v3, q)
    g.remove_edge(v4, q)

    q1 = NodeQ.from_nodes(v1, v12, v_center, v41, False)
    q2 = NodeQ.from_nodes(v12, v2, v23, v_center, False)
    q3 = NodeQ.from_nodes(v_center, v23, v3, v34, False)
    q4 = NodeQ.from_nodes(v41, v_center, v34, v4, False)

    g.remove_node(q)

    nodes = [v12, v23, v34, v41, v_center, q1, q2, q3, q4]

    for node in nodes:
        g.add_node(node)
    
    edges = [
        (v1, v12, e12B),
        (v12, v2, e12B),
        (v2, v23, e23B),
        (v23, v3, e23B),
        (v3, v34, e34B),
        (v34, v4, e34B),
        (v4, v41, e41B),
        (v41, v1, e41B),
        (q1, v1, None),
        (q1, v12, None),
        (q1, v_center, None),
        (q1, v41, None),
        (q2, v12, None),
        (q2, v2, None),
        (q2, v23, None),
        (q2, v_center, None),
        (q3, v_center, None),
        (q3, v23, None),
        (q3, v3, None),
        (q3, v34, None),
        (q4, v41, None),
        (q4, v_center, None),
        (q4, v34, None),
        (q4, v4, None),
        (v_center, v12, None),
        (v_center, v23, None),
        (v_center, v34, None),
        (v_center, v41, None),
    ]

    for node1, node2, b in edges:
        g.add_edge(node1, node2, b)


def create_left_graph():
    graph = Graph()

    v1 = Node(id=1)
    v2 = Node(id=2)
    v3 = Node(id=3)
    v4 = Node(id=4)
    q = NodeQ(id=5)

    nodes = [v1, v2, v3, v4, q]

    for node in nodes:
        graph.add_node(node)

    edges = [(v1, v2), (v2, v3), (v3, v4), (v4, v1), (v1, q), (v2, q), (v3, q), (v4, q)]

    for node1, node2 in edges:
        graph.add_edge(node1, node2)

    return graph


def create_start_graph():
    graph = Graph()

    v1 = Node(label="1", x=0, y=0, h=False)
    v2 = Node(label="2", x=10, y=0, h=False)
    v3 = Node(label="3", x=10, y=10, h=False)
    v4 = Node(label="4", x=0, y=10, h=False)
    q = NodeQ(label="Q", x=5, y=5, R=True)

    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    graph.add_node(v4)
    graph.add_node(q)

    edges = [
        (v1, v2, False),
        (v2, v3, False),
        (v3, v4, False),
        (v4, v1, False),
        (v1, q, None),
        (v2, q, None),
        (v3, q, None),
        (v4, q, None)
    ]

    for node1, node2, b in edges:
        graph.add_edge(node1, node2, b)

    return graph


def producion():
    return Production(create_left_graph(), transition, predicate)


if __name__ == "__main__":

    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)
    graph.show()
