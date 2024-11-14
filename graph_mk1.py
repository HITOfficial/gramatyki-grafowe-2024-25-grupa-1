from enum import Enum
import networkx as nx
import matplotlib.pyplot as plt


class EFlush(Enum):
    Remove, Add = 0, 1


class Graph:
    def __init__(self, points, edges, productions):
        self.points = points
        self.edges = edges
        self.productions = productions
        self.prod_buffer = []

    def step(self):
        for edge in self.edges:
            production = self.productions.get(edge.name, None)

            if production is not None:
                production(self, edge)

        self._flush_buffer()

    def remove_edge_prod(self, edge):
        self.prod_buffer.append((edge, EFlush.Remove))

    def add_edge_prod(self, new_edge):
        self.prod_buffer.append((new_edge, EFlush.Add))

    def _flush_buffer(self):
        while self.prod_buffer:
            edge, action = self.prod_buffer.pop()

            if action is EFlush.Add:
                self.edges.append(edge)
            if action is EFlush.Remove:
                self.edges.remove(edge)

    def plot(self):
        nxg = nx.Graph()

        for point in self.points:
            nxg.add_node(point)
        for edge in self.edges:
            nxg.add_edge(edge.v, edge.u)

        pos = nx.spring_layout(nxg)
        nx.draw(
            nxg, pos,
            with_labels=True,
            node_color='lightblue',
            edge_color='gray',
            font_weight='bold')
        edge_labels = {(edge.v, edge.u): str(edge) for edge in self.edges}
        nx.draw_networkx_edge_labels(
            nxg, pos,
            edge_labels=edge_labels,
            font_color='black')
        plt.show()
