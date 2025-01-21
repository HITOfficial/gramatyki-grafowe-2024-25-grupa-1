from __future__ import annotations

from abc import ABC
from typing import Dict

import networkx as nx
from matplotlib import pyplot as plt

from copy import deepcopy

id_global = 100


class NodeAbstart(ABC):
    def __init__(
        self,
        label: str = "",
        x: float = 0,
        y: float = 0,
        id: int = -1,
    ):

        global id_global

        self.label = label
        self.x = x
        self.y = y
        self.id = id if id != -1 else id_global
        id_global = id_global + 1


class NodeQ(NodeAbstart):

    def __init__(
        self,
        label: str = "Q",
        x: float = 0,
        y: float = 0,
        R=True,
        id: int = -1,
    ):
        super().__init__(label, x, y, id)
        self.R = R
    
    def __repr__(self) -> str:
        return f"{self.label}(R={(int)(self.R)})"

    @staticmethod
    def from_nodes(v1: Node, v2: Node, v3: Node, v4: Node, R: bool = None):
        x = (v1.x + v2.x + v3.x + v4.x) / 4
        y = (v1.y + v2.y + v3.y + v4.y) / 4
        return NodeQ(x = x, y = y, R = R)

    @staticmethod
    def from_nodes5(v1: Node, v2: Node, v3: Node, v4: Node, v5: Node, R: bool = None):
        x = (v1.x + v2.x + v3.x + v4.x + v5.x) / 5
        y = (v1.y + v2.y + v3.y + v4.y + v5.y) / 5
        return NodeQ(x = x, y = y, R = R)


class Node(NodeAbstart):

    def __init__(
        self, label: str = "v", x: float = 0, y: float = 0, id: int = -1, h: bool = True
    ):
        super().__init__(label, x, y, id)
        self.h = h

    def __repr__(self) -> str:
        return f"{self.label}(h={(int)(self.h)})"


class Production:
    def __init__(self, left_graph: Graph, transition, predicate, q_id = None):
        self.left_graph = left_graph
        self.transition = transition
        self.predicate = predicate
        self.q_id = q_id


class Graph:

    def __init__(self):
        self.underlying = nx.Graph()
        self.nodes_lookup_table: Dict[int, Node] = {}

    def __contains__(self, node: NodeAbstart) -> bool:
        return self.has_node(node)

    @property
    def nodes(self):
        return self.underlying.nodes

    def add_node(self, node: NodeAbstart) -> None:
        self.underlying.add_node(node, node=node)
        self.nodes_lookup_table[node.id] = node

    def remove_node(self, node: NodeAbstart) -> None:
        self.underlying.remove_node(node)
        self.nodes_lookup_table.pop(node.id, None)

    def get_node(self, node_id: int):
        return self.nodes_lookup_table.get(node_id, None)

    def add_edge(self, u: NodeAbstart, v: NodeAbstart, B = None) -> None:
        self.underlying.add_edge(u, v, B = B)

    def remove_edge(self, u: NodeAbstart, v: NodeAbstart) -> None:
        self.underlying.remove_edge(u, v)

    def get_edge_b_value(self, u: NodeAbstart, v: NodeAbstart) -> bool:
        b_values = nx.get_edge_attributes(self.underlying, "B")
        return bool(b_values.get((u, v)) or b_values.get((v, u)))

    def has_node(self, node: NodeAbstart) -> bool:
        return node in self.underlying

    def apply_production(self, production: Production, x = None, y = None):

        def node_match(n1, n2):
            return type(n1['node']) == type(n2['node'])

        matcher = nx.algorithms.isomorphism.GraphMatcher(
            self.underlying, production.left_graph.underlying, node_match=node_match
        )
        # subgraph_isomorphic = matcher.subgraph_is_isomorphic()

        def get_izo_node(mapping, left, id: int):
            return mapping[left.get_node(id)]

        for mapping in matcher.subgraph_monomorphisms_iter():
            reverse_mapping = dict((v, k) for k, v in mapping.items())
            partial = lambda node_id: get_izo_node(reverse_mapping, production.left_graph, node_id)

            if production.predicate(partial):
                if x is not None and y is not None:
                    q = partial(production.q_id)
                    if q.x == x and q.y == y:
                        production.transition(self, partial)
                        return True
                    continue

                production.transition(self, partial)
                return True

        return False

    def apply_productions(self, productions, show_after=False):
    
        while True:
            found = False
            for production in productions:
                if self.apply_production(production()):
                    found = True

                    if show_after:
                        self.show(skip_q_nodes=True)
                    
                    break
            
            if not found:
                break


    def show(self, with_attr: bool = True, attr_label_offset: float = -0.5, skip_q_nodes = False):
        deep_copy = deepcopy(self)

        _, ax = plt.subplots()
        ax.set_aspect("equal", adjustable="datalim")
        ax.set(xlabel="$x$", ylabel="$y$")

        labels = {}
        pos = {}
        to_remove = []

        if skip_q_nodes:
            for node in deep_copy.underlying.nodes:
                if isinstance(node, NodeQ):
                    to_remove.append(node)

            for node in to_remove:
                deep_copy.remove_node(node)

        for node in deep_copy.underlying.nodes:
            labels[node] = node.label
            pos[node] = (node.x, node.y)

        nx.draw(
            deep_copy.underlying, 
            pos,
            node_color='lightblue',
            edge_color='gray',
            font_weight='bold',
            labels=labels
        )

        b_values = nx.get_edge_attributes(deep_copy.underlying, "B")
        edge_labels = {
            (edge): "B=" + str((int)(b_values[edge]))
            for edge in deep_copy.underlying.edges
            if b_values[edge] is not None}
        nx.draw_networkx_edge_labels(
            deep_copy.underlying, pos,
            edge_labels=edge_labels,
            font_color='black')

        if with_attr:
            labels, pos = {}, {}

            for node in deep_copy.underlying.nodes:
                pos[node] = (node.x, node.y + attr_label_offset)
                attr_text = "\n".join(
                    f"{key}={value}"
                    for key, value in vars(node).items()
                    if value is not None and key != 'label' and key != "x" and key != "y" and key != "id")
                labels[node] = attr_text

            nx.draw_networkx_labels(
                deep_copy.underlying,
                pos,
                labels=labels,
                font_weight='light',
                font_size='8')

        plt.show()
