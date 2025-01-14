from GramatykiGrafowe import Graph, Node, NodeQ, Production
from GramatykiGrafowe.utils import center_coords
from productions.p16 import create_left_graph as create_left_graph_p16, predicate as predicate_p16, transition as transition_p16

from productions.p9 import create_left_graph as create_left_graph_p9, predicate as predicate_p9, transition as transition_p9

def create_test_graph():
    graph = Graph()

    v1 = Node(label="1", x=0, y=0, h=False)
    v2 = Node(label="2", x=10, y=0, h=False)
    v3 = Node(label="3", x=10, y=10, h=False)
    v4 = Node(label="4", x=0, y=10, h=False)
    v5 = Node(label="5", x=15, y=5, h=False)
    p = NodeQ(label="P", x=5, y=5, R=False)


    edge_vertices = [v1, v2, v5, v3, v4]

    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    graph.add_node(v4)
    graph.add_node(v5)
    graph.add_node(p)

    # edge between edge_vertices
    graph.add_edge(v1, v2)
    graph.add_edge(v2, v5)
    graph.add_edge(v5, v3)
    graph.add_edge(v3, v4)
    graph.add_edge(v4, v1)

    # edge between edge_vertices and p
    for node in edge_vertices:
        graph.add_edge(node, p)

    return graph

def test_p16_a():
    
    graph = create_test_graph()

    # graph.show()

    left_graph = create_left_graph_p16()
    production = Production(left_graph, transition_p16, predicate_p16)
    applied = graph.apply_production(production)

    # graph.show()

    assert applied

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

    return graph, p


def test_p16_b():
    
    graph, p = create_bigger_graph()
    p.R = False

    # graph.show()
    left_graph = create_left_graph_p16()
    production = Production(left_graph, transition_p16, predicate_p16)
    applied = graph.apply_production(production)

    # graph.show()

    assert applied
    

def test_p16_c():
    
    graph, p = create_bigger_graph()
    p.R = False

    # graph.show()

    left_graph = create_left_graph_p16()
    production = Production(left_graph, transition_p16, predicate_p16)
    applied = graph.apply_production(production)

    # graph.show()

    left_graph = create_left_graph_p9()
    production = Production(left_graph, transition_p9, predicate_p9)
    applied = graph.apply_production(production)

    # graph.show()

    assert applied