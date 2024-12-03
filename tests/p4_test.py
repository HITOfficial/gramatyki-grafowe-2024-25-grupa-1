from src.GramatykiGrafowe import Graph, Node, Production, NodeQ
from productions.p4 import predicate, transition, create_left_graph


def split_edge(g: Graph, v1: Node, v2: Node):
    B = g.underlying.get_edge_data(v1, v2)['B']
    v3 = Node(label="v", x=(v1.x + v2.x) / 2, y=(v1.y + v2.y) / 2, h=not B)
    g.add_node(v3)
    g.remove_edge(v1, v2)
    g.add_edge(v1, v3, B=B)
    g.add_edge(v3, v2, B=B)

    return g, v3


def create_test_graph(test_case):
    graph = Graph()

    v1 = Node(label="1", x=0, y=0, h=False)
    v2 = Node(label="2", x=10, y=0, h=False)
    v3 = Node(label="3", x=10, y=10, h=False)
    v4 = Node(label="4", x=0, y=10, h=False)

    if test_case == 0:
        v23 = Node(label="5", x=10, y=5, h=True)
        v41 = Node(label="6", x=0, y=5, h=True)
        q = NodeQ(label="Q", x=5, y=5, R=True)

        nodes = [v1, v2, v23, v3, v4, v41, v1, q]

        for node in nodes:
            graph.add_node(node)

        for i in range(6):
            graph.add_edge(nodes[i], nodes[i + 1], B=True)
            if i % 3 != 2:
                graph.add_edge(nodes[i], nodes[-1])

        return graph, True

    elif test_case == 1:
        v12 = Node(label="5", x=5, y=0, h=True)
        v34 = Node(label="6", x=5, y=10, h=True)
        q = NodeQ(label="Q", x=5, y=5, R=True)

        nodes = [v1, v12, v2, v3, v34, v4, v1, q]

        for node in nodes:
            graph.add_node(node)

        for i in range(6):
            graph.add_edge(nodes[i], nodes[i + 1], B = True)
            if i % 3 != 1:
                graph.add_edge(nodes[i], nodes[-1])

        return graph, True

    elif test_case == 2:
        v5 = Node(label="5", x=-5, y=5, h=False)
        q = NodeQ(label="Q", x=5, y=5, R=True)

        nodes = [v1, v2, v3, v4, v5, v1, q]

        for node in nodes:
            graph.add_node(node)

        for i in range(5):
            graph.add_edge(nodes[i], nodes[i + 1], B=True)
            graph.add_edge(nodes[i], nodes[-1])

        return graph, False

    elif test_case == 3:
        v12 = Node(label="5", x=5, y=0, h=False)
        v34 = Node(label="6", x=5, y=10, h=True)
        q = NodeQ(label="Q", x=5, y=5, R=True)

        nodes = [v1, v12, v2, v3, v34, v4, v1, q]

        for node in nodes:
            graph.add_node(node)

        for i in range(6):
            graph.add_edge(nodes[i], nodes[i + 1], B=True)
            if i % 3 != 1:
                graph.add_edge(nodes[i], nodes[-1])

        return graph, True

    elif test_case == 4:
        v12 = Node(label="5", x=5, y=0, h=False)
        v34 = Node(label="6", x=5, y=10, h=False)
        q = NodeQ(label="Q", x=5, y=5, R=True)

        nodes = [v1, v12, v2, v3, v34, v4, v1, q]

        for node in nodes:
            graph.add_node(node)

        for i in range(6):
            graph.add_edge(nodes[i], nodes[i + 1], B=True)
            if i % 3 != 1:
                graph.add_edge(nodes[i], nodes[-1])

        return graph, True

    elif test_case == 5:
        v12 = Node(label="5", x=5, y=0, h=True)
        v34 = Node(label="6", x=5, y=10, h=True)
        q = NodeQ(label="Q", x=5, y=5, R=False)

        nodes = [v1, v12, v2, v3, v34, v4, v1, q]

        for node in nodes:
            graph.add_node(node)

        for i in range(6):
            graph.add_edge(nodes[i], nodes[i + 1], B=True)
            if i % 3 != 1:
                graph.add_edge(nodes[i], nodes[-1])

        return graph, True

    elif test_case == 6:

        v12 = Node(label="12", x=5, y=0, h=False)
        v23 = Node(label="23", x=10, y=5, h=False)
        v34 = Node(label="34", x=5, y=10, h=False)
        v41 = Node(label="41", x=0, y=5, h=False)

        v00 = Node(label="00", x=5, y=5, h=False)

        outer_nodes = [v1, v12, v2, v23, v3, v34, v4, v41, v1]

        for node in outer_nodes[1:]:
            graph.add_node(node)

        graph.add_node(v00)
        graph.add_edge(v12, v00)
        graph.add_edge(v23, v00)
        graph.add_edge(v34, v00)
        graph.add_edge(v41, v00)

        q0 = NodeQ(label='Q', x=2.5, y=2.5, R=1)
        q1 = NodeQ(label='Q', x=7.5, y=2.5, R=0)
        q2 = NodeQ(label='Q', x=7.5, y=7.5, R=0)
        q3 = NodeQ(label='Q', x=2.5, y=7.5, R=0)

        mini_parts = [[v1, v12, v00, v41, q0],
                      [v12, v2, v23, v00, q1],
                      [v3, v34, v00, v23, q2],
                      [v4, v41, v00, v34, q3]]

        for mini_part in mini_parts:
            graph.add_node(mini_part[-1])
            for node in mini_part[:-1]:
                graph.add_edge(node, mini_part[-1])

        for i in range(8):
            graph.add_edge(outer_nodes[i], outer_nodes[i + 1], B=True)

        graph, vA = split_edge(graph, v1, v12)
        graph, vB = split_edge(graph, v41, v00)

        vA.h = 1

        return graph, True

    elif test_case == 7:
        v_nodes_data = [("v11", 0, 0, False), ("v12", 0, 2.5, False), ("v13", 0, 5, False),
                   ("v14", 2.5, 5, False), ("v15", 5, 5, False), ("v16", 5, 2.5, False),
                   ("v17", 5, 0, False), ("v18", 2.5, 0, False), ("v19", 2.5, 2.5, False)]

        q_nodes_data = [("q11", 1.25, 1.25, False), ("q12", 3.75, 1.25, False), ("q13", 1.25, 3.75, False),
                        ("q14", 3.75, 3.75, False)]

        v_nodes = [Node(label=v[0], x=v[1], y=v[2], h=v[3]) for v in v_nodes_data]
        q_nodes = [NodeQ(label=v[0], x=v[1], y=v[2], R=v[3]) for v in q_nodes_data]

        for v_node in v_nodes:
            graph.add_node(v_node)

        for q_node in q_nodes:
            graph.add_node(q_node)

        for i in range(8):
            B = True if i < 4 or i == 6 else None
            graph.add_edge(v_nodes[i], v_nodes[i+1], B=B)
        graph.add_edge(v_nodes[0], v_nodes[-2], B=True)
        graph.add_edge(v_nodes[1], v_nodes[-1])
        graph.add_edge(v_nodes[3], v_nodes[-1])
        graph.add_edge(v_nodes[5], v_nodes[-1])

        mini_parts = [[0, 0, 1, 8, 7], [1, 8, 7, 6, 5], [2, 1, 2, 3, 8], [3, 8, 5, 4, 3]]

        for mini_part in mini_parts:
            q_idx = mini_part[0]
            for idx in mini_part[1:]:
                graph.add_edge(q_nodes[q_idx], v_nodes[idx])

        v_nodes2 = [Node(label=v[0], x=v[1]+10, y=v[2], h=v[3]) for v in v_nodes_data]
        q_nodes2 = [NodeQ(label=v[0], x=v[1]+10, y=v[2], R=v[3]) for v in q_nodes_data]

        for v_node in v_nodes2:
            graph.add_node(v_node)

        for q_node in q_nodes2:
            graph.add_node(q_node)

        for i in range(8):
            B = True if 7 > i > 1 else None
            graph.add_edge(v_nodes2[i], v_nodes2[i+1], B=B)

        graph.add_edge(v_nodes2[0], v_nodes2[-2], B=True)
        graph.add_edge(v_nodes2[1], v_nodes2[-1])
        graph.add_edge(v_nodes2[3], v_nodes2[-1])
        graph.add_edge(v_nodes2[5], v_nodes2[-1])

        mini_parts = [[0, 0, 1, 8, 7], [1, 8, 7, 6, 5], [2, 1, 2, 3, 8], [3, 8, 5, 4, 3]]

        for mini_part in mini_parts:
            q_idx = mini_part[0]
            for idx in mini_part[1:]:
                graph.add_edge(q_nodes2[q_idx], v_nodes2[idx])

        graph.add_edge(v_nodes[4], v_nodes2[2], B=True)
        graph.add_edge(v_nodes[6], v_nodes2[0], B=True)

        q_node = NodeQ(label="Q", x=7.5,y=2.5,R=True)

        graph.add_node(q_node)
        graph.add_edge(v_nodes[4], q_node)
        graph.add_edge(v_nodes[6], q_node)
        graph.add_edge(v_nodes2[0], q_node)
        graph.add_edge(v_nodes2[2], q_node)

        v_nodes2[1].h = True
        v_nodes[5].h = True

        return graph, True


def apply_test(graph: Graph, left_graph: Graph, expected_output, show_figs=False):
    if show_figs:
        graph.show()

    prod = Production(left_graph, transition, predicate)
    applied = graph.apply_production(prod)

    if show_figs:
        graph.show()

    return applied == expected_output


def test_p4():
    left_graph = create_left_graph()

    N = 0
    N_TESTS = 8

    test_graphs = [create_test_graph(i) for i in range(N_TESTS)]
    for i, test_graph in enumerate(test_graphs):
        if apply_test(test_graph[0], left_graph, test_graph[1], i == 7):
            N += 1
        else:
            print(f"Wrong output in test graph: {i}")

    print(f"Tests passed : {N}/{N_TESTS} ({(N / N_TESTS) * 100:.2f}%)")
    return


if __name__ == "__main__":
    test_p4()
