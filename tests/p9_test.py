from productions.p9 import create_left_graph, create_start_graph, predicate, transition
from GramatykiGrafowe import Production, Graph, Node, NodeQ
import networkx as nx
from GramatykiGrafowe.utils import center_coords


def test_p9_production():
    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)

    assert applied, "Production was not applied successfully."


def test_p9_stats():
    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    graph.apply_production(production)

    nodes_labels = [node.label for node in graph.nodes]

    assert nx.number_of_edges(graph.underlying) == 35, \
        f"Expected 35 edges, found {len(graph.underlying.edges)}."

    assert nx.is_connected(graph.underlying), \
        "Graph is not connected."

    assert nx.number_of_nodes(graph.underlying) == 16, \
        f"Expected 16 nodes, found {len(graph.nodes)}."

    assert nodes_labels.count("Q") == 5, \
        "Expected 5 Q nodes, but found fewer or more."

    assert "Q" not in [node.label for node in graph.nodes if node.label != "Q"], \
        "Old Q node was not removed."


# sprawdzanie boundry, hanging
def test_p9_positions():
    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    graph.apply_production(production)

    positions = {(node.x, node.y): node.label for node in graph.nodes}
    expected_positions = [
        (5.0, 0.0),  # v12
        (12.5, 2.5),  # v25
        (12.5, 7.5),  # v53
        (5.0, 10.0),  # v34
        (0.0, 5.0),  # v41
        (7.0, 5.0),  # v_center
    ]

    for pos in expected_positions:
        assert pos in positions, \
            f"Expected node position {pos} not found."


def test_p9_connections():
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


def test_p9_disconnections():
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


def get_vertex(graph: Graph, label: str):
    vertices =  list(graph.nodes)
    for v in vertices:
        if label in str(v):
            return v
    raise ValueError("vertex not found in graph")


def create_bigger_graph():
    graph = Graph()

    v1 = Node(label="1", x=0, y=0, h=False)
    v2 = Node(label="2", x=10, y=0, h=False)
    v3 = Node(label="3", x=10, y=10, h=False)
    v4 = Node(label="4", x=0, y=10, h=False)
    v5 = Node(label="5", x=15, y=5, h=False)
    p = NodeQ(label="P", x=5, y=5, R=True)

    edge_vertices = [v1, v2, v5, v3, v4]

    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    graph.add_node(v4)
    graph.add_node(v5)
    graph.add_node(p)

    # edge between edge_vertices and p
    for node in edge_vertices:
        graph.add_edge(node, p)

    graph.add_edge(v1, v2, True)
    graph.add_edge(v2, v5, True)
    graph.add_edge(v5, v3, False)
    graph.add_edge(v3, v4, False)
    graph.add_edge(v4, v1, False)

    nodes = [
        Node(label="X1", x=-10, y=0, h=False),
        Node(label="X2", x=-7.5, y=12.5, h=False),
        Node(label="X3", x=5, y=20, h=False),
        Node(label="X4", x=17.5, y=10, h=False)        
        ]
    
    q1_x, q1_y = center_coords([nodes[0], v4])
    q2_x, q2_y = center_coords([nodes[2], v4])
    q3_x, q3_y = center_coords([nodes[3], v3])

    nodes.extend([
        NodeQ(label="Q1", x=q1_x, y=q1_y),
        NodeQ(label="Q2", x=q2_x, y=q2_y),
        NodeQ(label="Q3", x=q3_x, y=q3_y)
    ])
    for node in nodes:
        graph.add_node(node)


    graph.add_edge(nodes[0], v1, True)
    graph.add_edge(nodes[0], nodes[1], True)
    graph.add_edge(nodes[1], v4, False)
    graph.add_edge(nodes[1], nodes[2], True)
    graph.add_edge(nodes[2], v3, False)
    graph.add_edge(nodes[2], nodes[3], True)
    graph.add_edge(nodes[3], v5, True)

    graph.add_edge(nodes[4], nodes[0])
    graph.add_edge(nodes[4], nodes[1])
    graph.add_edge(nodes[4], v1)
    graph.add_edge(nodes[4], v4)

    graph.add_edge(nodes[5], nodes[1])
    graph.add_edge(nodes[5], nodes[2])
    graph.add_edge(nodes[5], v4)
    graph.add_edge(nodes[5], v3)

    graph.add_edge(nodes[6], nodes[2])
    graph.add_edge(nodes[6], nodes[3])
    graph.add_edge(nodes[6], v3)
    graph.add_edge(nodes[6], v5)

    return graph


def test_p9_isomorphism():
    graph = create_bigger_graph()    

    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)

    graph.show()
    applied = graph.apply_production(production)
    graph.show()

    assert applied # is left graph detected
    assert len(graph.nodes) == 23 # number of nodes



def create_test_graph():
    graph = Graph()

    v1 = Node(label="1", x=0, y=0, h=False)
    v2 = Node(label="2", x=10, y=0, h=False)
    v3 = Node(label="3", x=10, y=10, h=False)
    v4 = Node(label="4", x=0, y=10, h=False)
    v5 = Node(label="5", x=15, y=5, h=False)
    p = NodeQ(label="P", x=5, y=5, R=True)

    
    v7 = Node(label="7", x=0, y=-10, h=False)
    v8 = Node(label="8", x=10, y=-10, h=False)
    v9 = Node(label="9", x=-10, y=0, h=False)
    q1 = NodeQ(label="Q1", x=5, y=-5, R=True)
    q2 = NodeQ(label="Q2", x=-5, y=0, R=False)


    edge_vertices = [v1, v2, v5, v3, v4]

    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    graph.add_node(v4)
    graph.add_node(v5)
    graph.add_node(p)

    graph.add_node(v7)
    graph.add_node(v8)
    graph.add_node(v9)
    graph.add_node(q1)
    graph.add_node(q2)

    graph.add_edge(v1, v7, False)
    graph.add_edge(v2, v8, True)
    graph.add_edge(v7, v8, True)
    graph.add_edge(v1, q1)
    graph.add_edge(v2, q1)
    graph.add_edge(v7, q1)
    graph.add_edge(v8, q1)

    graph.add_edge(v4, v9, True)
    graph.add_edge(v9, v7, True)

    graph.add_edge(v1, q2)
    graph.add_edge(v4, q2)
    graph.add_edge(v9, q2)
    graph.add_edge(v7, q2)

    # edge between edge_vertices
    graph.add_edge(v1, v2, False)
    graph.add_edge(v2, v5, True)
    graph.add_edge(v5, v3, True)
    graph.add_edge(v3, v4, True)
    graph.add_edge(v4, v1, False)

    # edge between edge_vertices and p
    for node in edge_vertices:
        graph.add_edge(node, p)

    return graph

# def test_p1():
    
#     graph, v1 = create_test_graph()

#     graph.show()

#     left_graph = create_left_graph_p9()
#     production = Production(left_graph, transition_p9, predicate_p9)
#     applied = graph.apply_production(production)

#     graph.show()

#     # import pdb
#     # pdb.set_trace()

#     assert applied # is left graph detected
#     assert len(graph.nodes) == 21 # number of nodes
#     assert v1 in graph.nodes # v1 is still in graph

