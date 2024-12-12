from GramatykiGrafowe import Graph, Node, NodeQ, Production


def predicate(get_node):
    v1 = get_node(1)
    v2 = get_node(2)
    v3 = get_node(3)
    v4 = get_node(4)
    v5 = get_node(5)
    q = get_node(6)

    return q.R and not v1.h and not v2.h and not v3.h and not v4.h and v5.h


def transition(g: Graph, get_node):
    v1 = get_node(1)
    v2 = get_node(2)
    v3 = get_node(3)
    v4 = get_node(4)
    v5 = get_node(5)
    q = get_node(6)

    v12 = Node(x=(v1.x + v2.x) / 2, y=(v1.y + v2.y) / 2)
    v34 = Node(x=(v3.x + v4.x) / 2, y=(v3.y + v4.y) / 2)
    v41 = Node(x=(v4.x + v1.x) / 2, y=(v4.y + v1.y) / 2)

    v_center = Node(x=(v1.x + v2.x + v3.x + v4.x) / 4, y=(v1.y + v2.y + v3.y + v4.y) / 4)

    e12B = g.get_edge_b_value(v1, v2)
    e25B = g.get_edge_b_value(v2, v5)
    e34B = g.get_edge_b_value(v3, v4)
    e41B = g.get_edge_b_value(v4, v1)

    g.remove_edge(v1, v2)
    g.remove_edge(v3, v4)
    g.remove_edge(v4, v1)
    g.remove_edge(v1, q)
    g.remove_edge(v2, q)
    g.remove_edge(v3, q)
    g.remove_edge(v4, q)

    q1 = NodeQ(x=(v1.x + v12.x) / 2, y=(v1.y + v41.y) / 2)
    q2 = NodeQ(x=(v12.x + v2.x) / 2, y=(v2.y + v5.y) / 2)
    q3 = NodeQ(x=(v3.x + v34.x) / 2, y=(v5.y + v3.y) / 2)
    q4 = NodeQ(x=(v34.x + v4.x) / 2, y=(v4.y + v41.y) / 2)

    g.remove_node(q)

    nodes = [v12, v34, v41, v_center, q1, q2, q3, q4]

    for node in nodes:
        g.add_node(node)

    edges = [
        (v1, v12, e12B),
        (v12, v2, e12B),
        (v2, v5, e25B),
        (v5, v3, e25B),
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
        (q2, v5, None),
        (q2, v_center, None),
        (q3, v_center, None),
        (q3, v5, None),
        (q3, v3, None),
        (q3, v34, None),
        (q4, v41, None),
        (q4, v_center, None),
        (q4, v34, None),
        (q4, v4, None),
        (v_center, v12, False),
        (v_center, v5, False),
        (v_center, v34, False),
        (v_center, v41, False)
    ]

    for node1, node2, B in edges:
        g.add_edge(node1, node2, B)


def create_left_graph():
    graph = Graph()

    v1 = Node(id=1)
    v2 = Node(id=2)
    v3 = Node(id=3)
    v4 = Node(id=4)
    v5 = Node(id=5)
    q = NodeQ(id=6)

    nodes = [v1, v2, v3, v4, v5, q]

    for node in nodes:
        graph.add_node(node)

    edges = [
        (v1, v2, True),
        (v2, v5, True),
        (v5, v3, True),
        (v3, v4, True),
        (v4, v1, True),
        (v1, q, None),
        (v2, q, None),
        (v3, q, None),
        (v4, q, None),
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
    q = NodeQ(x=5, y=5, R=True)

    nodes = [v1, v2, v3, v4, v5, q]

    for node in nodes:
        graph.add_node(node)

    edges = [
        (v1, v2, True),
        (v2, v5, True),
        (v5, v3, True),
        (v3, v4, True),
        (v4, v1, True),
        (v1, q, None),
        (v2, q, None),
        (v3, q, None),
        (v4, q, None),
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
