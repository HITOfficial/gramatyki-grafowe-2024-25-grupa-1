
def center_coords(nodes):
    x = sum([node.x for node in nodes]) / len(nodes)
    y = sum([node.y for node in nodes]) / len(nodes)
    return x, y
