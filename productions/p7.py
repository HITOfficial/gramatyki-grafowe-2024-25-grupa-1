from GramatykiGrafowe import Graph, Node, NodeQ, Production


def predicate(get_node):
    q = get_node(5)
    return q.R == 0


def transition(graph: Graph, get_node):
    q = get_node(5)
    q.R = 1  


def create_left_graph():
    graph = Graph()

    v1 = Node(id=1)
    v2 = Node(id=2)
    v3 = Node(id=3)
    v4 = Node(id=4)
    q = NodeQ(id=5, R=0)

    nodes = [v1, v2, v3, v4, q]
    for node in nodes:
        graph.add_node(node)

    edges = [
        (v1, q), (v2, q), (v3, q), (v4, q)
    ]
    for node1, node2 in edges:
        graph.add_edge(node1, node2)

    return graph


def create_start_graph():
    graph = Graph()

    v1 = Node(label="1", x=0, y=0, h=False)
    v2 = Node(label="2", x=10, y=0, h=False)
    v3 = Node(label="3", x=10, y=10, h=False)
    v4 = Node(label="4", x=0, y=10, h=False)
    q = NodeQ(x=5, y=5, R=0)

    nodes = [v1, v2, v3, v4, q]
    for node in nodes:
        graph.add_node(node)

    edges = [
        (v1, q), (v2, q), (v3, q), (v4, q)
    ]
    for node1, node2 in edges:
        graph.add_edge(node1, node2)

    return graph


def producion():
    return Production(create_left_graph(), transition, predicate, 5)


if __name__ == "__main__":

    graph = create_start_graph()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)
    graph.show()
