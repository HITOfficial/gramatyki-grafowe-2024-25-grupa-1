import pytest
from GramatykiGrafowe import Graph, Node, NodeQ, Production
from productions.p10 import create_left_graph, predicate, transition

# @pytest.mark.skip(reason="p1 production is totally broken in this case")
def test_p10():
    graph, v1 = create_test_graph()

    graph.show()

    left_graph = create_left_graph()
    production = Production(left_graph, transition=transition, predicate=predicate)
    applied = graph.apply_production(production)

    graph.show()

    # import pdb
    # pdb.set_trace()

    assert applied # is left graph detected
    assert len(graph.nodes) == 28 # number of nodes
    assert v1 in graph.nodes # v1 is still in graph


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

    v6 = Node(label="6", x=5, y=0, h=True)

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
    graph.add_edge(v2, v5, True)
    graph.add_edge(v5, v3, True)
    graph.add_edge(v3, v4, True)
    graph.add_edge(v4, v1, False)

    # edge between edge_vertices and p
    for node in edge_vertices:
        graph.add_edge(node, p)

    graph.add_edge(v1, v6, False)
    graph.add_edge(v6, v2, False)

    return graph, v1
