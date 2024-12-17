from GramatykiGrafowe import Production, Graph, Node, NodeQ


def test_applied():

    g1 = Graph()
    g1.add_node(Node())

    g2 = Graph()
    g2.add_node(Node())

    def predicate(get_node):
        return True
    
    def transition(g: Graph, get_node):
        return

    production = Production(g2, transition, predicate)
    applied = g1.apply_production(production)
    assert applied, "Production not applied."


def test_not_applied():

    g1 = Graph()
    g1.add_node(Node())

    g2 = Graph()
    g2.add_node(NodeQ())

    def predicate(get_node):
        return True
    
    def transition(g: Graph, get_node):
        return

    production = Production(g2, transition, predicate)
    applied = g1.apply_production(production)
    print(applied)

    assert not applied, "Production applied, but should not."
