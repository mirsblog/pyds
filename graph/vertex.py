class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        self.visited = False

    def addNeighbor(self, vertex, weight=0):
        self.neighbors[vertex] = weight
