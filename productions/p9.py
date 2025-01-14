from GramatykiGrafowe import Graph, Node, NodeQ, Production
from GramatykiGrafowe.utils import center_coords


def predicate(get_node):
    v1 = get_node(1)
    v2 = get_node(2)
    v3 = get_node(3)
    v4 = get_node(4)
    v5 = get_node(5)
    q = get_node(6)

    return not any([not q.R, v1.h, v2.h, v3.h, v4.h, v5.h])


def transition(g: Graph, get_node):
    v1 = get_node(1)
    v2 = get_node(2)
    v3 = get_node(3)
    v4 = get_node(4)
    v5 = get_node(5)
    p = get_node(6)

    edge_vertices = [v1, v2, v5, v3, v4]

    # store old edge values
    edge_values = []

    for i in range(len(edge_vertices)):
        val = g.get_edge_b_value(
            edge_vertices[i % len(edge_vertices)],
            edge_vertices[(i + 1) % len(edge_vertices)],
        )

        edge_values.append(val)


    # remove old edges
    for i in range(len(edge_vertices)):
        g.remove_edge(
            edge_vertices[i % len(edge_vertices)],
            edge_vertices[(i + 1) % len(edge_vertices)],
        )

    for node in edge_vertices:
        g.remove_edge(node, p)

    g.remove_node(p)

    # create new nodes
    x, y = center_coords([v1, v2, v3, v4, v5])
    v_center = Node(x=x, y=y, h=False)

    x, y = center_coords([v1, v2])
    v12 = Node(x=x, y=y, h=not edge_values[0])

    x, y = center_coords([v2, v5])
    v25 = Node(x=x, y=y, h=not edge_values[1])

    x, y = center_coords([v5, v3])
    v53 = Node(x=x, y=y, h=not edge_values[2])

    x, y = center_coords([v3, v4])
    v34 = Node(x=x, y=y, h=not edge_values[3])

    x, y = center_coords([v4, v1])
    v41 = Node(x=x, y=y, h=not edge_values[4])

    # create new breach nodes
    q1_vertices = [v1, v12, v_center, v41]
    x, y = center_coords(q1_vertices)
    q1 = NodeQ(x=x, y=y, R=False)

    q2_vertices = [v2, v25, v_center, v12]
    x, y = center_coords(q2_vertices)
    q2 = NodeQ(x=x, y=y, R=False)

    q3_vertices = [v3, v34, v_center, v53]
    x, y = center_coords(q3_vertices)
    q3 = NodeQ(x=x, y=y, R=False)

    q4_vertices = [v4, v41, v_center, v34]
    x, y = center_coords(q4_vertices)
    q4 = NodeQ(x=x, y=y, R=False)

    q5_vertices = [v5, v53, v_center, v25]
    x, y = center_coords(q5_vertices)
    q5 = NodeQ(x=x, y=y, R=False)

    g.add_node(v12)
    g.add_node(v25)
    g.add_node(v53)
    g.add_node(v34)
    g.add_node(v41)
    g.add_node(v_center)
    g.add_node(q1)
    g.add_node(q2)
    g.add_node(q3)
    g.add_node(q4)
    g.add_node(q5)

    # outer edges
    g.add_edge(v1, v12, edge_values[0])
    g.add_edge(v12, v2, edge_values[0])
    g.add_edge(v2, v25, edge_values[1])
    g.add_edge(v25, v5, edge_values[1])
    g.add_edge(v5, v53, edge_values[2])
    g.add_edge(v53, v3, edge_values[2])
    g.add_edge(v3, v34, edge_values[3])
    g.add_edge(v34, v4, edge_values[3])
    g.add_edge(v4, v41, edge_values[4])
    g.add_edge(v41, v1, edge_values[4])

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


def create_left_graph():
    graph = Graph()

    v1 = Node(id=1)
    v2 = Node(id=2)
    v3 = Node(id=3)
    v4 = Node(id=4)
    v5 = Node(id=5)
    p = NodeQ(id=6)
    edge_vertices = [v1, v2, v5, v3, v4]

    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    graph.add_node(v4)
    graph.add_node(v5)
    graph.add_node(p)

    # edge between edge_vertices
    for i in range(len(edge_vertices)):
        graph.add_edge(
            edge_vertices[i % len(edge_vertices)],
            edge_vertices[(i + 1) % len(edge_vertices)],
        )

    # edge between edge_vertices and p
    for node in edge_vertices:
        graph.add_edge(node, p)

    return graph


def create_start_graph():
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

    # edge between edge_vertices
    for i in range(len(edge_vertices)):
        graph.add_edge(
            edge_vertices[i % len(edge_vertices)],
            edge_vertices[(i + 1) % len(edge_vertices)],
        )

    # edge between edge_vertices and p
    for node in edge_vertices:
        graph.add_edge(node, p)

    return graph


def producion():
    return Production(create_left_graph(), transition, predicate)


if __name__ == "__main__":

    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)
    graph.show()
