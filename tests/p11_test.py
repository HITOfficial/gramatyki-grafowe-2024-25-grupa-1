from p11 import create_left_graph, predicate, transition
from p17_test import create_test_graph
from GramatykiGrafowe import Production, Graph, Node

def test_p11_production():
    graph = create_test_graph()
    graph.show()

    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)
    graph.show()


if __name__ == "__main__":
    graph = create_test_graph()
    graph.show()

    left_graph = create_left_graph()
    production = Production(left_graph, transition, predicate)
    applied = graph.apply_production(production)
    graph.show()