from abc import ABC


class Object(ABC):
    def __init__(self, name, attributes=None):
        self.name = name
        self.attributes = attributes if attributes is not None else dict()

    def __str__(self):
        name = self.name.name
        return f'{name}\n{self.attributes}' if len(self.attributes) > 0 else name
