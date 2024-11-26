from __future__ import annotations

from abc import ABC
from typing import Dict

import networkx as nx
from matplotlib import pyplot as plt

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
        label: str = "",
        x: float = 0,
        y: float = 0,
        R=True,
        id: int = -1,
    ):
        super().__init__(label, x, y, id)
        self.R = R


class Node(NodeAbstart):

    def __init__(
        self, label: str = "", x: float = 0, y: float = 0, id: int = -1, h: bool = True
    ):
        super().__init__(label, x, y, id)
        self.h = h


class Production:
    def __init__(self, left_graph: Graph, transition, predicate):
        self.left_graph = left_graph
        self.transition = transition
        self.predicate = predicate


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

    def add_edge(self, u: NodeAbstart, v: NodeAbstart) -> None:
        self.underlying.add_edge(u, v)

    def remove_edge(self, u: NodeAbstart, v: NodeAbstart) -> None:
        self.underlying.remove_edge(u, v)

    def has_node(self, node: NodeAbstart) -> bool:
        return node in self.underlying

    def apply_production(self, production: Production):
        matcher = nx.algorithms.isomorphism.GraphMatcher(
            self.underlying, production.left_graph.underlying
        )
        subgraph_isomorphic = matcher.subgraph_is_isomorphic()

        def get_izo_node(mapping, left, id: int):
            return mapping[left.get_node(id)]

        for mapping in matcher.subgraph_monomorphisms_iter():
            reverse_mapping = dict((v, k) for k, v in mapping.items())
            partial = lambda node_id: get_izo_node(reverse_mapping, production.left_graph, node_id)
            if production.predicate(partial):
                production.transition(self, partial)
                break

        return subgraph_isomorphic

    def show(self):
        _, ax = plt.subplots()
        ax.set_aspect("equal", adjustable="datalim")
        ax.set(xlabel="$x$", ylabel="$y$")

        labels = {}
        pos = {}

        for node in self.underlying.nodes:
            labels[node] = node.label
            pos[node] = (node.x, node.y)

        nx.draw(self.underlying, ax=ax, pos=pos, labels=labels)
        plt.show()
