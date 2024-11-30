from productions.p2 import create_left_graph, create_start_graph, predicate, transition
from GramatykiGrafowe import Production, Graph, Node
import networkx as nx


def test_p2_production():
    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)

    assert applied, "Production was not applied successfully."


def test_p2_stats():
    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    graph.apply_production(production)

    nodes_labels = [node.label for node in graph.nodes]

    assert nx.number_of_edges(graph.underlying) == 28, \
        f"Expected 28 edges, found {len(graph.underlying.edges)}."

    assert nx.is_connected(graph.underlying), \
        "Graph is not connected."

    assert nx.number_of_nodes(graph.underlying) == 13, \
        f"Expected 13 nodes, found {len(graph.nodes)}."

    assert nodes_labels.count("Q") == 4, \
        "Expected 4 Q nodes, but found fewer or more."

    assert "Q" not in [node.label for node in graph.nodes if node.label != "Q"], \
        "Old Q node was not removed."


def test_p2_positions():
    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    graph.apply_production(production)

    positions = {(node.x, node.y): node.label for node in graph.nodes}
    expected_positions = [
        (5.0, 0.0),  # v12
        (5.0, 10.0),  # v34
        (0.0, 5.0),  # v41
        (5.0, 5.0),  # v_center
    ]

    for pos in expected_positions:
        assert pos in positions, \
            f"Expected node position {pos} not found."


def test_p2_connections():
    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    graph.apply_production(production)

    edges_to_check = [
        ("1", "Q"), ("2", "Q"), ("3", "Q"), ("4", "Q"), ("5", "Q"),
        ("1", "v"), ("2", "v"), ("3", "v"), ("4", "v"), ("5", "v"),
        ("v", "v"), ("v", "Q")
    ]

    for u_label, v_label in edges_to_check:
        assert any(
            (u.label == u_label and v.label == v_label) or
            (u.label == v_label and v.label == u_label)
            for u, v in graph.underlying.edges), \
            f"Expected edge between {u_label} and {v_label} not found."


def test_p2_disconnections():
    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    graph.apply_production(production)

    edges_to_check = [
        ("1", "2"), ("1", "3"), ("1", "4"),
        ("2", "3"), ("2", "4"),
        ("3", "4"),
        ("Q", "Q")
    ]

    for u_label, v_label in edges_to_check:
        assert not any(
            (u.label == u_label and v.label == v_label) or
            (u.label == v_label and v.label == u_label)
            for u, v in graph.underlying.edges), \
            f"Expected edge between {u_label} and {v_label} not found."


def test_p2_isomorphism():
    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    graph.apply_production(production)

    expected_graph = Graph()

    v1 = Node(label="1", x=0, y=0, h=False)
    v2 = Node(label="2", x=10, y=0, h=False)
    v3 = Node(label="3", x=10, y=10, h=False)
    v4 = Node(label="4", x=0, y=10, h=False)
    v5 = Node(label="5", x=10, y=5, h=True)
    v12 = Node(label="v", x=5, y=0)
    v34 = Node(label="v", x=5, y=10)
    v41 = Node(label="v", x=0, y=5)
    v_center = Node(label="v", x=5, y=5)

    nodes = [v1, v2, v3, v4, v5, v12, v34, v41, v_center]

    for node in nodes:
        expected_graph.add_node(node)

    edges = [
        (v1, v12), (v12, v2),
        (v2, v5), (v5, v3),
        (v3, v34), (v34, v4),
        (v4, v41), (v41, v1),
        (v12, v_center), (v5, v_center),
        (v34, v_center), (v41, v_center)
    ]

    for u, v in edges:
        expected_graph.add_edge(u, v)

    matcher = nx.algorithms.isomorphism.GraphMatcher(
        graph.underlying,
        expected_graph.underlying,
        node_match=lambda u, v: u["node"].label == v["node"].label)

    assert matcher.subgraph_is_isomorphic(), \
        "Graphs are not isomorphic after production."
