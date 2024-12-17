from GramatykiGrafowe import Graph, Node, NodeQ, Production
from GramatykiGrafowe.utils import center_coords
from p17 import create_left_graph, predicate, transition


def create_test_graph():
    graph = Graph()

    v11 = Node(label="11", x=0, y=0, h=False)
    v12 = Node(label="12", x=1, y=1.5, h=False)  
    v13 = Node(label="13", x=2, y=3, h=False) 
    v14 = Node(label="14", x=3, y=1.5, h=False) 
    v15 = Node(label="15", x=4, y=0, h=False) 
    v16 = Node(label="16", x=3, y=-1.5, h=True)
    v17 = Node(label="17", x=2, y=-3, h=False)
    v18 = Node(label="18", x=1, y=-1.5, h=False)
    v19 = Node(label="19", x=2, y=0, h=False)
    q11x, q11y = center_coords([v11,v12,v18,v19])
    q11 = NodeQ(label="Q", x=q11x, y=q11y, R=False)
    q12x, q12y = center_coords([v12,v13,v14,v19])
    q12 = NodeQ(label="Q", x=q12x, y=q12y, R=False)
    q13x, q13y = center_coords([v14,v15,v16,v19])
    q13 = NodeQ(label="Q", x=q13x, y=q13y, R=True)
    q14x, q14y = center_coords([v16,v17,v18,v19])
    q14 = NodeQ(label="Q", x=q14x, y=q14y, R=False)
    nodes1 = [v11, v12, v13, v14, v15, v16, v17, v18, v19, q11, q12, q13, q14]
    v21 = Node(label="21", x=3+1, y=2+1.5, h=False)  
    v22 = Node(label="22", x=4+2, y=1+3, h=False) 
    v23 = Node(label="23", x=4+3, y=1+1.5, h=False) 
    v24 = Node(label="24", x=4+4, y=1+0, h=False) 
    v25 = Node(label="25", x=3+3, y=2-1.5, h=True)
    v26 = Node(label="26", x=3+2, y=2+0, h=False)
    q21x, q21y = center_coords([v13,v21,v26,v14])
    q21 = NodeQ(label="Q", x=q21x, y=q21y, R=False)
    q22x, q22y = center_coords([v21,v22,v23,v26])
    q22 = NodeQ(label="Q", x=q22x, y=q22y, R=False)
    q23x, q23y = center_coords([v23,v24,v25,v26])
    q23 = NodeQ(label="Q", x=q23x, y=q23y, R=False)
    q24x, q24y = center_coords([v26,v25,v15,v14])
    q24 = NodeQ(label="Q", x=q24x, y=q24y, R=False)
    nodes2 = [v21, v22, v23, v24, v25, v26, q21, q22, q23, q24]
    v31 = Node(label="31", x=10, y=2, h=False)  
    v32 = Node(label="32", x=12, y=-1, h=False) 
    q31x, q31y = center_coords([v22,v31,v32,v24])
    q31 = NodeQ(label="Q", x=q31x, y=q31y, R=False)
    nodes3 = [v31, v32, q31]
    v41 = Node(label="41", x=6, y=-5, h=False)
    p41x, p41y = center_coords([v17,v15,v24,v32,v41])
    p41 = NodeQ(label="P", x=p41x, y=p41y, R=False)
    nodes4 = [v41, p41]
    edges1 = [
        (v11, v12, True),
        (v12, v13, True),
        (v13, v14, False),
        (v14, v15, False),
        (v15, v16, False),
        (v16, v17, False),
        (v17, v18, True),
        (v18, v11, True),
        (v12, v19, False),
        (v14, v19, False),
        (v16, v19, False),
        (v18, v19, False),
        (v11, q11, False),
        (v12, q11, False),
        (v18, q11, False),
        (v19, q11, False),
        (v12, q12, False),
        (v13, q12, False),
        (v14, q12, False),
        (v19, q12, False),
        (v14, q13, False),
        (v15, q13, False),
        (v16, q13, False),
        (v19, q13, False),
        (v16, q14, False),
        (v17, q14, False),
        (v18, q14, False),
        (v19, q14, False),
    ]
    edges2 = [
        (v13, v21, True),
        (v21, v22, True),
        (v22, v23, False),
        (v23, v24, False),
        (v24, v25, False),
        (v25, v26, False),
        (v25, v15, False),
        (v21, v26, False),
        (v23, v26, False),
        (v25, v26, False),
        (v14, v26, False),
        (v13, q21, False),
        (v21, q21, False),
        (v26, q21, False),
        (v14, q21, False),
        (v21, q22, False),
        (v22, q22, False),
        (v23, q22, False),
        (v26, q22, False),
        (v26, q23, False),
        (v23, q23, False),
        (v24, q23, False),
        (v25, q23, False),
        (v14, q24, False),
        (v26, q24, False),
        (v25, q24, False),
        (v15, q24, False),
    ]
    edges3 = [
        (v22, v31, True),
        (v24, v32, False),
        (v31, v32, True),
        (v22, q31, False),
        (v31, q31, False),
        (v32, q31, False),
        (v24, q31, False),
    ]
    edges4 = [
        (v17, v41, True),
        (v32, v41, True),
        (v41, p41, False),
        (v17, p41, False),
        (v15, p41, False),
        (v24, p41, False),
        (v32, p41, False),
    ]
    
    for node in nodes1 + nodes2 + nodes3 + nodes4:
        graph.add_node(node)
    for node1, node2, B in edges1 + edges2 + edges3 + edges4:
        graph.add_edge(node1, node2, B)

    return graph


if __name__ == "__main__":
    graph = create_test_graph()
    graph.show()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)
    graph.show()

