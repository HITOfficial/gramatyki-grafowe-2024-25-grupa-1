from enum import Enum
from object import Object


class EEdge(Enum):
    A, B = 0, 1


class Edge(Object):
    ATTRIBUTE_P = 'p'

    def __init__(self, name, v, u, attributes=None):
        super().__init__(name, attributes)
        self.v, self.u = v, u
