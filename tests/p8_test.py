from GramatykiGrafowe import Graph, Node, NodeQ, Production
from GramatykiGrafowe.utils import center_coords
from productions.p8 import create_left_graph, predicate, transition

def create_test_graph():
    graph = Graph()

    v11 = Node(label="11", x=0, y=0, h=False)
    v13 = Node(label="13", x=2, y=3, h=False) 
    v14 = Node(label="14", x=3, y=1.5, h=True) 
    v15 = Node(label="15", x=4, y=0, h=False) 
    v17 = Node(label="17", x=2, y=-3, h=False)
    q1x, q1y = center_coords([v11,v13,v15,v17])
    q1 = NodeQ(label="Q", x=q1x, y=q1y, R=False)
    nodes1 = [v11, v13, v14, v15, v17, q1]
    v21 = Node(label="21", x=3+1, y=2+1.5, h=False)  
    v22 = Node(label="22", x=4+2, y=1+3, h=False) 
    v23 = Node(label="23", x=4+3, y=1+1.5, h=False) 
    v24 = Node(label="24", x=4+4, y=1+0, h=False) 
    v25 = Node(label="25", x=3+3, y=2-1.5, h=True)
    v26 = Node(label="26", x=3+2, y=2+0, h=False)
    q21x, q21y = center_coords([v13,v21,v26,v14])
    q21 = NodeQ(label="Q", x=q21x, y=q21y, R=True)
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
    p41 = NodeQ(label="P", x=p41x, y=p41y, R=True)
    nodes4 = [v41, p41]
    edges1 = [
        (v11, q1, None),
        (v13, q1, None),
        (v15, q1, None),
        (v17, q1, None),
        (v11, v13, True),
        (v13, v14, False),
        (v14, v15, False),
        (v15, v17, False),
        (v17, v11, True),
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
        (v13, q21, None),
        (v21, q21, None),
        (v26, q21, None),
        (v14, q21, None),
        (v21, q22, None),
        (v22, q22, None),
        (v23, q22, None),
        (v26, q22, None),
        (v26, q23, None),
        (v23, q23, None),
        (v24, q23, None),
        (v25, q23, None),
        (v14, q24, None),
        (v26, q24, None),
        (v25, q24, None),
        (v15, q24, None),
    ]
    edges3 = [
        (v22, v31, True),
        (v24, v32, False),
        (v31, v32, True),
        (v22, q31, None),
        (v31, q31, None),
        (v32, q31, None),
        (v24, q31, None),
    ]
    edges4 = [
        (v17, v41, True),
        (v32, v41, True),
        (v41, p41, None),
        (v17, p41, None),
        (v15, p41, None),
        (v24, p41, None),
        (v32, p41, None),
    ]
    
    for node in nodes1 + nodes2 + nodes3 + nodes4:
        graph.add_node(node)
    for node1, node2, B in edges1 + edges2 + edges3 + edges4:
        graph.add_edge(node1, node2, B)

    return graph

def test_p8():
    graph = create_test_graph()
    # graph.show()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)
    # graph.show()
    assert applied
    # return


if __name__ == "__main__":
    graph = create_test_graph()
    # graph.show()
    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)
    # graph.show()
