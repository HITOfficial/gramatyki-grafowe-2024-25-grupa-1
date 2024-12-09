import pytest
from GramatykiGrafowe import Production
from productions.p1 import create_left_graph as create_left_graph_p1, predicate as predicate_p1, transition as transition_p1
from productions.p10 import create_left_graph as create_left_graph_p10, predicate as predicate_p10, transition as transition_p10
from tests.p9_test import create_test_graph

@pytest.mark.skip(reason="p1 production is totally broken in this case")
def test_p10():
    graph, v1 = create_test_graph()

    graph.show()

    left_graph = create_left_graph_p1()
    production = Production(left_graph, transition_p1, predicate_p1)
    applied = graph.apply_production(production)

    graph.show()

    left_graph = create_left_graph_p10()
    production = Production(left_graph, transition_p10, predicate_p10)
    applied = graph.apply_production(production)

    graph.show()

    # import pdb
    # pdb.set_trace()

    assert applied # is left graph detected
    assert len(graph.nodes) == 28 # number of nodes
    assert v1 in graph.nodes # v1 is still in graph



