from src.GramatykiGrafowe import Graph, Node


def split_edge(g: Graph, v1:Node, v2: Node):
    v3 = Node(label="v", x=(v1.x + v2.x) / 2, y=(v1.y + v2.y) / 2)
    g.add_node(v3)
    g.remove_edge(v1, v2)
    g.add_edge(v1, v3)
    g.add_edge(v3, v2)

    return g, v3


def predicate(get_node):
    v1 = get_node(1)
    v2 = get_node(2)
    v3 = get_node(3)
    v4 = get_node(4)
    v5 = get_node(5)
    v6 = get_node(6)
    q = get_node(7)

    return q.R == 1 and v1.h == v2.h == v4.h == v5.h == 0 and v3.h == v6.h == 1


def transition(g: Graph, get_node):
    v_nodes = [get_node(i) for i in range(1, 7)]
    q = get_node(7)

    v_nodes[2].h = False
    v_nodes[5].h = False

    g, v7 = split_edge(g, v_nodes[3], v_nodes[4])
    g, v8 = split_edge(g, v_nodes[0], v_nodes[1])

    for i in [0, 1, 3, 4]:
        g.remove_edge(v_nodes[i], q)

    q.label = "v"
    q.h = False
    q.R = False

    g.add_edge(q, v7)
    g.add_edge(q, v8)

    g.add_edge(q, v_nodes[2])
    g.add_edge(q, v_nodes[5])

    parts = [[q, v7, v_nodes[4], v_nodes[5]],
             [q, v_nodes[2], v_nodes[3], v7],
             [q, v_nodes[2], v_nodes[1], v8],
             [q, v8, v_nodes[0], v_nodes[5]]]

    q_nodes = []
    for part in parts:
        q_x = 0
        q_y = 0
        for node in part:
            q_x += node.x
            q_y += node.y

        q_x = q_x / 4
        q_y = q_y / 4

        q_node = Node(label="Q", x=q_x, y=q_y, R=False)
        q_nodes.append(q_node)
        g.add_node(q_node)
        for node in part:
            g.add_edge(node, q_node)

    return g


def create_left_graph():
    graph = Graph()
    nodes = [Node(id=i) for i in range(1, 8)]

    for node in nodes:
        graph.add_node(node)

    for i in range(5):
        graph.add_edge(nodes[i], nodes[i+1])
        if (i+1) % 3 != 0:
            graph.add_edge(nodes[i], nodes[-1])
    graph.add_edge(nodes[5], nodes[0])

    return graph

