from GramatykiGrafowe import Graph, Node, NodeQ, Production
from GramatykiGrafowe.utils import center_coords


def predicate(get_node, base_graph):
    v1 = get_node(1)
    v2 = get_node(2)
    v3 = get_node(3)
    v4 = get_node(4)
    v5 = get_node(5)
    v6 = get_node(6)
    v7 = get_node(7)
    q = get_node(8)

    # print(f"\nPredicate: {v1} {v2} {v3} {v4} {v5} {v6} {v7} {q}\n")

    return not any([not q.R, v1.h, v2.h, v3.h, v4.h, v5.h, not v6.h, not v7.h])


def transition(g: Graph, get_node):
    v1 = get_node(1)
    v2 = get_node(2)
    v3 = get_node(3)
    v4 = get_node(4)
    v5 = get_node(5)
    v6 = get_node(6)
    v7 = get_node(7)
    p = get_node(8)

    # print(f"\nTransition: {v1} {v2} {v3} {v4} {v5} {v6} {v7} {p}\n")

    for node in [v1, v2, v3, v4, v5]:
        g.remove_edge(node, p)

    g.remove_node(p)

    edge_b_25 = g.get_edge_b_value(v2, v5)
    edge_b_53 = g.get_edge_b_value(v5, v3)
    edge_b_34 = g.get_edge_b_value(v3, v4)
    g.remove_edge(v2, v5)
    g.remove_edge(v5, v3)
    g.remove_edge(v3, v4)
    
    # create new nodes
    x, y = center_coords([v1, v2, v3, v4, v5])
    v_center = Node(label="v", x=x, y=y, h=False)

    v12 = v6
    v41 = v7

    x, y = center_coords([v2, v5])
    v25 = Node(label="v", x=x, y=y, h=(not edge_b_25))

    x, y = center_coords([v5, v3])
    v53 = Node(label="v", x=x, y=y, h=(not edge_b_53))

    x, y = center_coords([v3, v4])
    v34 = Node(label="v", x=x, y=y, h=(not edge_b_34))

    # create new breach nodes
    q1_vertices = [v1, v12, v_center, v41]
    x, y = center_coords(q1_vertices)
    q1 = NodeQ(label="Q", x=x, y=y, R=False)

    q2_vertices = [v2, v25, v_center, v12]
    x, y = center_coords(q2_vertices)
    q2 = NodeQ(label="Q", x=x, y=y, R=False)

    q3_vertices = [v3, v34, v_center, v53]
    x, y = center_coords(q3_vertices)
    q3 = NodeQ(label="Q", x=x, y=y, R=False)

    q4_vertices = [v4, v41, v_center, v34]
    x, y = center_coords(q4_vertices)
    q4 = NodeQ(label="Q", x=x, y=y, R=False)

    q5_vertices = [v5, v53, v_center, v25]
    x, y = center_coords(q5_vertices)
    q5 = NodeQ(label="Q", x=x, y=y, R=False)

    new_nodes = [v12, v25, v53, v34, v41, v_center, q1, q2, q3, q4, q5]
    for node in new_nodes:
        g.add_node(node)

    # outer edges
    g.add_edge(v2, v25, edge_b_25)
    g.add_edge(v25, v5, edge_b_25)
    g.add_edge(v5, v53, edge_b_53)
    g.add_edge(v53, v3, edge_b_53)
    g.add_edge(v3, v34, edge_b_34)
    g.add_edge(v34, v4, edge_b_34)

    # inner q1 edges
    g.add_edge(q1, v1)
    g.add_edge(q1, v12)
    g.add_edge(q1, v_center)
    g.add_edge(q1, v41)

    # inner q2 edges
    g.add_edge(q2, v2)
    g.add_edge(q2, v25)
    g.add_edge(q2, v_center)
    g.add_edge(q2, v12)

    # inner q3 edges
    g.add_edge(q3, v3)
    g.add_edge(q3, v34)
    g.add_edge(q3, v_center)
    g.add_edge(q3, v53)

    # inner q4 edges
    g.add_edge(q4, v4)
    g.add_edge(q4, v41)
    g.add_edge(q4, v_center)
    g.add_edge(q4, v34)

    # inner q5 edges
    g.add_edge(q5, v5)
    g.add_edge(q5, v53)
    g.add_edge(q5, v_center)
    g.add_edge(q5, v25)

    # inner center edges
    g.add_edge(v_center, v12, False)
    g.add_edge(v_center, v25, False)
    g.add_edge(v_center, v53, False)
    g.add_edge(v_center, v34, False)
    g.add_edge(v_center, v41, False)



    v6.h = False
    v6.label = "v"

    v7.h = False
    v7.label = "v"

    print('applied p11')


def create_left_graph():
    graph = Graph()

    v1 = Node(id=1)
    v2 = Node(id=2)
    v3 = Node(id=3)
    v4 = Node(id=4)
    v5 = Node(id=5)
    v6 = Node(id=6)
    v7 = Node(id=7)
    p = NodeQ(id=8)
    
    # print(f"\nGraph: {v1} {v2} {v3} {v4} {v5} {v6} {v7} {p}\n")

    nodes = [v1, v2, v3, v4, v5, v6, v7, p]
    for node in nodes:
        graph.add_node(node)

    edges = [
        (v1, v6, False),
        (v1, v7, False),
        (v2, v6, False),
        (v2, v5, False),
        (v3, v5, False),
        (v3, v4, False),
        (v4, v7, False),
        (p, v1, None),
        (p, v2, None),
        (p, v3, None),
        (p, v4, None),
        (p, v5, None),
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
    v5 = Node(label="5", x=15, y=5, h=False)
    v6 = Node(label="6", x=5, y=0, h=True)
    v7 = Node(label="7", x=0, y=5, h=True)
    p = NodeQ(label="P", x=5, y=5, R=True)


    nodes = [v1, v2, v3, v4, v5, v6, v7, p]
    for node in nodes:
        graph.add_node(node)

    edges = [
        (v1, v6, True),
        (v1, v7, True),
        (v2, v6, True),
        (v2, v5, True),
        (v3, v5, True),
        (v3, v4, True),
        (v4, v7, True),
        (p, v1, None),
        (p, v2, None),
        (p, v3, None),
        (p, v4, None),
        (p, v5, None),
    ]

    for node1, node2, B in edges:
        graph.add_edge(node1, node2, B)

    return graph


def producion():
    return Production(create_left_graph(), transition, predicate)


if __name__ == "__main__":

    graph = create_start_graph()
    graph.show()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)
    graph.show()
