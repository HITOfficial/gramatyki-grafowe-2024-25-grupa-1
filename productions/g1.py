from GramatykiGrafowe import Graph, Node, NodeQ
import p1, p2, p3, p4, p7, p8, p9, p10, p11, p16

def create_start_graph():
    graph = Graph()

    v1 = Node(label="1", x=0, y=0, h=False)
    v2 = Node(label="2", x=10, y=0, h=False)
    v3 = Node(label="3", x=10, y=10, h=False)
    v4 = Node(label="4", x=0, y=10, h=False)
    v5 = Node(label="5", x=3.5, y=2.5, h=False)
    v6 = Node(label="6", x=6.5, y=2.5, h=False)
    v7 = Node(label="7", x=8, y=5, h=False)
    v8 = Node(label="8", x=6.5, y=7.5, h=False)
    v9 = Node(label="9", x=3.5, y=7.5, h=False)
    v10 = Node(label="10", x=10, y=5, h=False)

    q1 = NodeQ.from_nodes(v1, v2, v6, v5, False)
    q2 = NodeQ.from_nodes(v2, v10, v7, v6, False)
    q3 = NodeQ.from_nodes(v7, v10, v3, v8, False)
    q4 = NodeQ.from_nodes(v8, v3, v4, v9, False)
    q5 = NodeQ.from_nodes(v1, v5, v9, v4, False)
    q6 = NodeQ.from_nodes5(v5, v6, v7, v8, v9, False)

    nodes = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, q1, q2, q3, q4, q5, q6]

    for node in nodes:
        graph.add_node(node)

    edges = [(v1, v2), (v2, v10), (v10, v3), (v3, v4), (v4, v1), 
             (v5, v6), (v6, v7), (v7, v8), (v8, v9), (v9, v5),
             (v1, v5), (v2, v6), (v10, v7), (v3, v8), (v4, v9),
             (q1, v1), (q1, v2), (q1, v5), (q1, v6),
             (q2, v2), (q2, v10), (q2, v7), (q2, v6),
             (q3, v7), (q3, v10), (q3, v3), (q3, v8),
             (q4, v8), (q4, v3), (q4, v4), (q4, v9),
             (q5, v1), (q5, v5), (q5, v9), (q5, v4),
             (q6, v5), (q6, v6), (q6, v7), (q6, v8), (q6, v9)]

    for node1, node2 in edges:
        graph.add_edge(node1, node2)

    return graph


if __name__ == "__main__":

    productions = [
        p1.producion, p2.producion, p3.producion,
        p9.producion, p10.producion, p11.producion,
        p16.producion, p8.producion, p8.producion
    ]
    operations = [
        (p16.producion(), 5.6, 5.0),
        productions,
        (p7.producion(), 7.025, 5.0),
        productions,
        (p7.producion(), 7.56875, 5.0),
        productions,
    ]
    graph = create_start_graph()
    # graph.show(skip_q_nodes=True)

    for idx, op in enumerate(operations):
        # print(f'{idx=}')

        if isinstance(op, tuple):
            graph.apply_production(*op)
            # graph.show(skip_q_nodes=True)
        else:
            graph.apply_productions(op, show_after=False)


    graph.show(skip_q_nodes=True)
