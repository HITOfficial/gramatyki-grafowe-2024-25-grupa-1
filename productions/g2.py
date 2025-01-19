from GramatykiGrafowe import Graph, Node, NodeQ, Production
import p1, p2, p3, p4, p7, p8, p9, p10, p11, p16, p17


def create_start_graph():
    graph = Graph()

    # Define outer square nodes
    v1 = Node(label="1", x=0, y=0, h=False)
    v2 = Node(label="2", x=300, y=0, h=False)
    v23 = Node(label="23", x=300, y=130, h=False)
    v3 = Node(label="3", x=300, y=300, h=False)
    v4 = Node(label="4", x=0, y=300, h=False)

    # Define middle nodes
    m1 = Node(label="M1", x=100, y=60, h=False)
    m2 = Node(label="M2", x=200, y=60, h=False)
    m3 = Node(label="M3", x=220, y=130, h=False)
    m4 = Node(label="M4", x=200, y=200, h=False)
    m5 = Node(label="M5", x=100, y=200, h=False)

    # Define Q nodes
    q1 = NodeQ(label="Q1", x=265, y=200, R=False)
    q2 = NodeQ(label="Q2", x=250, y=60, R=False)
    q3 = NodeQ(label="Q3", x=150, y=30, R=False)
    q4 = NodeQ(label="Q4", x=20, y=150, R=False)
    q5 = NodeQ(label="Q3", x=150, y=275, R=False)
    q6 = NodeQ(label="Q4", x=150, y=150, R=False)

    nodes = [v1, v2, v23, v3, v4, m1, m2, m3, m4, m5,
             q1, q2, q3, q4, q5, q6]

    for node in nodes:
        graph.add_node(node)

    # Define edges based on the shape in the image
    edges = [(v1, m1), (v2, m2), (v23, m3), (v3, m4), (v4, m5)]

    for node1, node2 in edges:
        graph.add_edge(node1, node2)

    edge_vertices = [v1, v2, v23, v3, v4]
    middle_vertices = [m1, m2, m3, m4, m5]

    for i in range(len(edge_vertices)):
        graph.add_edge(
            edge_vertices[i % len(edge_vertices)],
            edge_vertices[(i + 1) % len(edge_vertices)],
        )

    for i in range(len(middle_vertices)):
        graph.add_edge(
            middle_vertices[i % len(middle_vertices)],
            middle_vertices[(i + 1) % len(middle_vertices)],
        )

    # edge between edge_vertices and q
    for node in [m3, v23, v3, m4]:
        graph.add_edge(node, q1)

    for node in [m3, v23, v2, m2]:
        graph.add_edge(node, q2)

    for node in [m2, v2, v1, m1]:
        graph.add_edge(node, q3)

    for node in [m1, v1, v4, m5]:
        graph.add_edge(node, q4)

    for node in [m5, m4, v3, v4]:
        graph.add_edge(node, q5)

    for node in [m1, m2, m3, m4, m5]:
        graph.add_edge(node, q6)

    return graph
  

def print_node_coordinates(graph):
    print("Node Coordinates:")
    for node in graph.nodes:
        print(f"Node {node.label}: (x={node.x}, y={node.y})")


if __name__ == "__main__":

    productions = [
        p1.producion, p2.producion, p3.producion,
        p17.producion, p8.producion, p8.producion,
        p11.producion,
    ]
    operations = [
        (p7.producion(), 265, 200),
        productions,
        (p7.producion(), 228.75, 201.25),
        productions,
        (p7.producion(), 214.6875, 202.1875),
        productions,
    ]
    graph = create_start_graph()

    for idx, op in enumerate(operations):
        if isinstance(op, tuple):
            graph.apply_production(*op)
        else:
            graph.apply_productions(op)
    
        #print(f'{idx=}')
    #print_node_coordinates(graph)
    graph.show()

