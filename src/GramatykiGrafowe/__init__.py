from __future__ import annotations
from typing import Dict

from matplotlib import pyplot as plt
import networkx as nx

id_global = 100

class Node:
    def __init__(self, label: str = '', x: float = 0, y: float = 0, h: bool = True, R = True, id: int = -1):

        global id_global

        self.label = label
        self.x = x
        self.y = y
        self.id = id if id != -1 else id_global
        self.h = h
        self.R = R
        id_global = id_global + 1


class Graph:

    def __init__(self):
        self.underlying = nx.Graph()
        self.nodes_lookup_table: Dict[int, Node] = {}

    def __contains__(self, node: Node) -> bool:
        return self.has_node(node)

    @property
    def nodes(self):
        return self.underlying.nodes

    def add_node(self, node: Node) -> None:
        self.underlying.add_node(node, node=node)
        self.nodes_lookup_table[node.id] = node

    def remove_node(self, node: Node) -> None:
        self.underlying.remove_node(node)
        self.nodes_lookup_table.pop(node.id, None)

    def get_node(self, node_id: int):
        return self.nodes_lookup_table.get(node_id, None)

    def add_edge(self, u: Node, v: Node) -> None:
        self.underlying.add_edge(u, v)

    def remove_edge(self, u: Node, v: Node) -> None:
        self.underlying.remove_edge(u, v)

    def has_node(self, node: Node) -> bool:
        return node in self.underlying

    def apply_production(self, left_graph: Graph, transition, predicate):
        matcher = nx.algorithms.isomorphism.GraphMatcher(self.underlying, left_graph.underlying)
        subgraph_isomorphic = matcher.subgraph_is_isomorphic()

        def get_izo_node(mapping, left, id: int):
            return mapping[left.get_node(id)]

        for mapping in matcher.subgraph_monomorphisms_iter():
            reverse_mapping = dict((v,k) for k,v in mapping.items())
            partial = lambda node_id: get_izo_node(reverse_mapping, left_graph, node_id)     
            if predicate(partial):
                transition(self, partial)
                break

        return subgraph_isomorphic
    
    def show(self):
        _, ax = plt.subplots()
        ax.set_aspect('equal', adjustable='datalim')
        ax.set(xlabel='$x$', ylabel='$y$')

        labels = {}
        pos = {}
        
        for node in self.underlying.nodes:
            labels[node] = node.label
            pos[node] = (node.x, node.y)

        nx.draw(self.underlying, ax=ax, pos=pos, labels=labels)
        plt.show()
