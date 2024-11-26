from GramatykiGrafowe import Graph, Node
from GramatykiGrafowe.utils import center_coords


def predicate(get_node):
    p = get_node(6)
    return not p.R


def transition(g: Graph, get_node):
    p = get_node(6)
    p.R = True


def create_left_graph():
    graph = Graph()

    v1 = Node(id=1)
    v2 = Node(id=2)
    v3 = Node(id=3)
    v4 = Node(id=4)
    v5 = Node(id=5)
    p = Node(id=6)
    
    edge_vertices = [v1, v2, v3, v4, v5]

    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    graph.add_node(v4)
    graph.add_node(v5)
    graph.add_node(p)

    for v in edge_vertices:
        graph.add_edge(v, p)
    
    return graph


def create_start_graph():
    graph = Graph()

    v1 = Node(label="1", x=0, y=0, h=False)
    v2 = Node(label="2", x=10, y=0, h=False)
    v3 = Node(label="3", x=10, y=10, h=False)
    v4 = Node(label="4", x=0, y=10, h=False)
    v5 = Node(label="5", x=-5, y=5, h=False)
    p = Node(label="P", x=5, y=5, R=True)

    edge_vertices = [v1, v2, v3, v4, v5]

    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    graph.add_node(v4)
    graph.add_node(v5)
    graph.add_node(p)

    for v in edge_vertices:
        graph.add_edge(v, p)
    
    return graph


if __name__ == "__main__":

    graph = create_start_graph()
    left_graph = create_left_graph()
    applied = graph.apply_production(left_graph, transition=transition, predicate=predicate)
    graph.show()
