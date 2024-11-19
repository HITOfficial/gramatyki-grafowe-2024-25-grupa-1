from GramatykiGrafowe import Graph, Node


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

    v12 = Node(label="v", x=(v1.x + v2.x) / 2, y=(v1.y + v2.y) / 2)
    v34 = Node(label="v", x=(v3.x + v4.x) / 2, y=(v3.y + v4.y) / 2)
    v41 = Node(label="v", x=(v4.x + v1.x) / 2, y=(v4.y + v1.y) / 2)

    v_center = Node(
        label="v", x=(v1.x + v2.x + v3.x + v4.x) / 4, y=(v1.y + v2.y + v3.y + v4.y) / 4
    )

    g.remove_edge(v1, v2)
    g.remove_edge(v3, v4)
    g.remove_edge(v4, v1)
    g.remove_edge(v1, q)
    g.remove_edge(v2, q)
    g.remove_edge(v3, q)
    g.remove_edge(v4, q)

    q1 = Node(label="Q", x=(v1.x + v12.x) / 2, y=(v1.y + v41.y) / 2)
    q2 = Node(label="Q", x=(v12.x + v2.x) / 2, y=(v2.y + v5.y) / 2)
    q3 = Node(label="Q", x=(v3.x + v34.x) / 2, y=(v5.y + v3.y) / 2)
    q4 = Node(label="Q", x=(v34.x + v4.x) / 2, y=(v4.y + v41.y) / 2)

    g.remove_node(q)

    nodes = [v12, v34, v41, v_center, q1, q2, q3, q4]

    for node in nodes:
        g.add_node(node)

    edges = [
        (v1, v12),
        (v12, v2),
        (v2, v5),
        (v5, v3),
        (v3, v34),
        (v34, v4),
        (v4, v41),
        (v41, v1),
        (q1, v1),
        (q1, v12),
        (q1, v_center),
        (q1, v41),
        (q2, v12),
        (q2, v2),
        (q2, v5),
        (q2, v_center),
        (q3, v_center),
        (q3, v5),
        (q3, v3),
        (q3, v34),
        (q4, v41),
        (q4, v_center),
        (q4, v34),
        (q4, v4),
        (v_center, v12),
        (v_center, v5),
        (v_center, v34),
        (v_center, v41),
    ]

    for node1, node2 in edges:
        g.add_edge(node1, node2)


def create_left_graph():
    graph = Graph()

    v1 = Node(id=1)
    v2 = Node(id=2)
    v3 = Node(id=3)
    v4 = Node(id=4)
    v5 = Node(id=5)
    q = Node(id=6)

    nodes = [v1, v2, v3, v4, v5, q]

    for node in nodes:
        graph.add_node(node)

    edges = [
        (v1, v2),
        (v2, v5),
        (v5, v3),
        (v3, v4),
        (v4, v1),
        (v1, q),
        (v2, q),
        (v3, q),
        (v4, q),
    ]

    for node1, node2 in edges:
        graph.add_edge(node1, node2)

    return graph


def create_start_graph():
    graph = Graph()

    v1 = Node(label="1", x=0, y=0, h=False)
    v2 = Node(label="2", x=10, y=0, h=False)
    v3 = Node(label="3", x=10, y=10, h=False)
    v4 = Node(label="4", x=0, y=10, h=False)
    v5 = Node(label="5", x=10, y=5, h=True)
    q = Node(label="Q", x=5, y=5, R=True)

    nodes = [v1, v2, v3, v4, v5, q]

    for node in nodes:
        graph.add_node(node)

    edges = [
        (v1, v2),
        (v2, v5),
        (v5, v3),
        (v3, v4),
        (v4, v1),
        (v1, q),
        (v2, q),
        (v3, q),
        (v4, q),
    ]

    for node1, node2 in edges:
        graph.add_edge(node1, node2)

    return graph


if __name__ == "__main__":

    graph = create_start_graph()
    left_graph = create_left_graph()
    applied = graph.apply_production(
        left_graph, transition=transition, predicate=predicate
    )
    graph.show()
