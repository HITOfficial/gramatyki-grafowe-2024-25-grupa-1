from productions.p1 import create_left_graph, create_start_graph, predicate, transition


def test_p1():
    graph = create_start_graph()
    left_graph = create_left_graph()
    applied = graph.apply_production(
        left_graph, transition=transition, predicate=predicate
    )

    assert applied
