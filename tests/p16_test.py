import pytest
from GramatykiGrafowe import Graph, Node, NodeQ, Production
from productions.p16 import create_left_graph as create_left_graph_p16, predicate as predicate_p16, transition as transition_p16
from tests.p9_test import create_test_graph as create_test_graph_p9


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

    return graph, v1

def test_p16_a():
    
    graph, _ = create_test_graph()

    graph.show()

    left_graph = create_left_graph_p16()
    production = Production(left_graph, transition_p16, predicate_p16)
    applied = graph.apply_production(production)

    graph.show()

# @pytest.mark.skip(reason="Probably searching for isomorphism finds wrong graph or get_node() is broken")
def test_p16_b():
    
    graph, _, p = create_test_graph_p9()
    p.R = False

    graph.show()
    left_graph = create_left_graph_p16()
    production = Production(left_graph, transition_p16, predicate_p16)
    applied = graph.apply_production(production)

    graph.show()



