from enum import Enum
from object import Object


class EPoint(Enum):
    v = 0


class Point(Object):
    def __init__(self, name, attributes=None):
        super().__init__(name, attributes)
