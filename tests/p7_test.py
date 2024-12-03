from src.GramatykiGrafowe import Graph, Node, NodeQ, Production
from productions.p7 import predicate, transition, create_left_graph


def split_edge(g: Graph, v1:Node, v2: Node):
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
    q = NodeQ(label="Q", x=5, y=5, R=False)

    if test_case == 0:
        nodes = [v1, v2, v3, v4, v1, q]

        for node in nodes[1:]:
            graph.add_node(node)

        for i in range(4):
            graph.add_edge(nodes[i], nodes[i + 1])
            graph.add_edge(nodes[i], nodes[-1])

        return graph, True
    elif test_case == 1:
        q.R = True

        nodes = [v1, v2, v3, v4, v1, q]

        for node in nodes[1:]:
            graph.add_node(node)

        for i in range(4):
            graph.add_edge(nodes[i], nodes[i + 1])
            graph.add_edge(nodes[i], nodes[-1])

        return graph, True
    elif test_case == 2:
        v23 = Node(label="5", x=10, y=5, h=True)
        v41 = Node(label="6", x=0, y=5, h=True)
        q.R = True

        nodes = [v1, v2, v23, v3, v4, v41, v1, q]

        for node in nodes[1:]:
            graph.add_node(node)

        for i in range(6):
            graph.add_edge(nodes[i], nodes[i + 1])
            if i % 3 != 2:
                graph.add_edge(nodes[i], nodes[-1])
        return graph, False
    elif test_case == 3:
        v5 = Node(label="5", x=-5, y=5, h=False)
        nodes = [v1, v2, v3, v4, v5, v1, q]

        for node in nodes[1:]:
            graph.add_node(node)

        for i in range(5):
            graph.add_edge(nodes[i], nodes[i + 1])
            graph.add_edge(nodes[i], nodes[-1])
        return graph, False
    elif test_case == 4:
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

        q0 = NodeQ(label='Q', x=2.5, y=2.5, R=0)
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

        return graph, True
    elif test_case == 5:
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

        q0 = NodeQ(label='Q', x=2.5, y=2.5, R=0)
        q1 = NodeQ(label='Q', x=7.5, y=2.5, R=1)
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

        return graph, True



def apply_test(graph: Graph, left_graph: Graph, expected_output, i=0, show_figs=False):
    if show_figs:
        graph.show()

    prod = Production(left_graph, transition, predicate)
    applied = graph.apply_production(prod)

    if applied and i > 3:
        count = 0
        for node in graph.nodes():
            if type(node) == NodeQ and node.R == 1:
                count += 1
        print(f"i: {i} count: {count}")
        if i == 4 and count > 1:
            return False

    if show_figs:
        graph.show()

    return applied == expected_output


def test_p7():
    left_graph = create_left_graph()

    N = 0
    N_TESTS = 6

    test_graphs = [create_test_graph(i) for i in range(N_TESTS)]
    for i, test_graph in enumerate(test_graphs):
        if apply_test(test_graph[0], left_graph, test_graph[1], i, i == 5):
            N += 1
        else:
            print(f"Wrong output in test graph: {i}")

    print(f"Tests passed : {(N / N_TESTS) * 100:.2f}%")
    return


if __name__ == "__main__":
    test_p7()
