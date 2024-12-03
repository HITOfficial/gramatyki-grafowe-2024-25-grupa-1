from src.GramatykiGrafowe import Graph, Node, NodeQ, Production


def predicate(get_node):
    v1 = get_node(1)
    v2 = get_node(2)
    v3 = get_node(3)
    v4 = get_node(4)
    v5 = get_node(5)
    v6 = get_node(6)
    q = get_node(7)

    v_nodes = [v1, v2, v3, v4, v5, v6]
    for v_node in v_nodes:
        if type(v_node) != Node:
            return False
    if type(q) != NodeQ:
        return False

    return q.R and not v1.h and not v2.h and not v3.h and not v4.h and v5.h and v6.h


def transition(g: Graph, get_node):
    v1 = get_node(1)
    v2 = get_node(2)
    v3 = get_node(3)
    v4 = get_node(4)
    v5 = get_node(5)
    v6 = get_node(6)
    q = get_node(7)

    v34 = Node(label="v", x=(v3.x + v4.x) / 2, y=(v3.y + v4.y) / 2)
    v41 = Node(label="v", x=(v4.x + v1.x) / 2, y=(v4.y + v1.y) / 2)

    v_center = Node(
        label="v", x=(v1.x + v2.x + v3.x + v4.x) / 4, y=(v1.y + v2.y + v3.y + v4.y) / 4
    )

    g.remove_edge(v3, v4)
    g.remove_edge(v4, v1)
    g.remove_edge(v1, q)
    g.remove_edge(v2, q)
    g.remove_edge(v3, q)
    g.remove_edge(v4, q)

    q1 = NodeQ(label="Q", x=(v1.x + v6.x) / 2, y=(v1.y + v41.y) / 2)
    q2 = NodeQ(label="Q", x=(v6.x + v2.x) / 2, y=(v2.y + v5.y) / 2)
    q3 = NodeQ(label="Q", x=(v3.x + v34.x) / 2, y=(v5.y + v3.y) / 2)
    q4 = NodeQ(label="Q", x=(v34.x + v4.x) / 2, y=(v4.y + v41.y) / 2)

    g.remove_node(q)

    nodes = [v34, v41, v_center, q1, q2, q3, q4]

    for node in nodes:
        g.add_node(node)

    edges = [
        (v1, v6),
        (v6, v2),
        (v2, v5),
        (v5, v3),
        (v3, v34),
        (v34, v4),
        (v4, v41),
        (v41, v1),
        (q1, v1),
        (q1, v6),
        (q1, v_center),
        (q1, v41),
        (q2, v6),
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
        (v_center, v6),
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
    v6 = Node(id=6)
    q = Node(id=7)

    nodes = [v1, v2, v3, v4, v5, v6, q]

    for node in nodes:
        graph.add_node(node)

    edges = [
        (v1, v6),
        (v6, v2),
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


def create_test_graph():
    graph = Graph()

    v_nodes_data = [("v11", 0, 0, False), ("v12", 0, 2.5, False), ("v13", 0, 5, False),
                    ("v14", 2.5, 5, False), ("v15", 5, 5, False), ("v16", 5, 2.5, False),
                    ("v17", 5, 0, False), ("v18", 2.5, 0, False), ("v19", 2.5, 2.5, False)]

    q_nodes_data = [("q11", 1.25, 1.25, False), ("q12", 3.75, 1.25, False), ("q13", 1.25, 3.75, False),
                    ("q14", 3.75, 3.75, False)]

    v_nodes = [Node(label=v[0], x=v[1], y=v[2]+5, h=v[3]) for v in v_nodes_data]
    q_nodes = [NodeQ(label=v[0], x=v[1], y=v[2]+5, R=v[3]) for v in q_nodes_data]

    for v_node in v_nodes:
        graph.add_node(v_node)

    for q_node in q_nodes:
        graph.add_node(q_node)

    for i in range(8):
        B = True if i < 4 else None
        graph.add_edge(v_nodes[i], v_nodes[i + 1], B=B)
    graph.add_edge(v_nodes[0], v_nodes[-2])
    graph.add_edge(v_nodes[1], v_nodes[-1])
    graph.add_edge(v_nodes[3], v_nodes[-1])
    graph.add_edge(v_nodes[5], v_nodes[-1])

    v_nodes[-2].h = True
    v_nodes[-4].h = True

    mini_parts = [[0, 0, 1, 8, 7], [1, 8, 7, 6, 5], [2, 1, 2, 3, 8], [3, 8, 5, 4, 3]]

    for mini_part in mini_parts:
        q_idx = mini_part[0]
        for idx in mini_part[1:]:
            graph.add_edge(q_nodes[q_idx], v_nodes[idx])

    v_nodes2 = [Node(label=v[0], x=v[1]+5, y=v[2], h=v[3]) for v in v_nodes_data]
    q_nodes2 = [NodeQ(label=v[0], x=v[1]+5, y=v[2], R=v[3]) for v in q_nodes_data]

    v_nodes2[2] = v_nodes[-3]

    for v_node in v_nodes2:
        graph.add_node(v_node)

    for q_node in q_nodes2:
        graph.add_node(q_node)

    v_nodes2[1].h = True
    v_nodes2[3].h = True

    for i in range(8):
        B = True if 7 > i > 3 else None
        graph.add_edge(v_nodes2[i], v_nodes2[i + 1], B=B)
    graph.add_edge(v_nodes2[0], v_nodes2[-2], B=True)
    graph.add_edge(v_nodes2[1], v_nodes2[-1])
    graph.add_edge(v_nodes2[3], v_nodes2[-1])
    graph.add_edge(v_nodes2[5], v_nodes2[-1])

    mini_parts = [[0, 0, 1, 8, 7], [1, 8, 7, 6, 5], [2, 1, 2, 3, 8], [3, 8, 5, 4, 3]]

    for mini_part in mini_parts:
        q_idx = mini_part[0]
        for idx in mini_part[1:]:
            graph.add_edge(q_nodes2[q_idx], v_nodes2[idx])

    v_nodes3 = [Node(label='v', x=0, y=0, h=False), Node(label='v', x=10, y=10, h=False)]
    q_nodes3 = [NodeQ(label="q", x=2.5, y=2.5,R=True), NodeQ(label="q", x=7.5, y=7.5,R=False)]

    graph.add_node(v_nodes3[0])
    graph.add_node(v_nodes3[1])
    graph.add_node(q_nodes3[0])
    graph.add_node(q_nodes3[1])

    graph.add_edge(v_nodes3[0], q_nodes3[0])
    graph.add_edge(v_nodes3[0], v_nodes[0], B=True)
    graph.add_edge(v_nodes3[0], v_nodes2[0], B=True)
    graph.add_edge(q_nodes3[0], v_nodes2[0])
    graph.add_edge(q_nodes3[0], v_nodes[0])
    graph.add_edge(q_nodes3[0], v_nodes2[2])

    graph.add_edge(v_nodes3[1], v_nodes2[4], B=True)
    graph.add_edge(v_nodes3[1], v_nodes[4], B=True)
    graph.add_edge(v_nodes3[1], q_nodes3[1])
    graph.add_edge(q_nodes3[1], v_nodes2[4])
    graph.add_edge(q_nodes3[1], v_nodes[4])
    graph.add_edge(q_nodes3[1], v_nodes2[2])

    return graph


if __name__ == "__main__":
    test_graph = create_test_graph()
    left_graph = create_left_graph()

    test_graph.show()

    prod = Production(left_graph, transition, predicate)
    applied = test_graph.apply_production(prod)

    test_graph.show()
