from vertex import Vertex

class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.n = 0

    def addVertex(self, key):

        print("adding vertex ", key)
        # adding vertex to a graph
        if key not in self.vertices:
            self.vertices[key] = Vertex(key)
            self.n += 1

        return self.vertices[key]

    def addEdge(self, key1, key2, weight=0):
        if key1 not in self.vertices:
            self.addVertex(key1)
        if key2 not in self.vertices:
            self.addVertex(key2)
        self.vertices[key1].addNeighbor(self.vertices[key2], weight)

"""
depth first search
"""
def DFS(graph, start):
    def _dfs(start):
        start.visited = True
        print("visited ", start.key)
        for n in iter(start.neighbors.keys()):
            if not n.visited:
                _dfs(n)

    if start not in graph.vertices:
        return

    _dfs(graph.vertices[start])

"""
breadth first search
"""
def BFS(graph, start):

    if start not in graph.vertices:
        return

    stack = []
    stack.append(graph.vertices[start])

    while stack:
        node = stack.pop(0)
        node.visited = True
        print("visited:", node.key)

        for nbr in iter(node.neighbors.keys()):
            if not nbr.visited:
                stack.append(nbr)

"""
transpose of a graph
"""
def Transpose(graph):

    gT = Graph()

    # iterate over each vertex in graph
    for key, vertex in graph.vertices.items():
        # iterate over each neighbor of this vertex
        for neighbor, weight in vVertex.neighbors.items():
            # add vVertex as a neighbor to uVertex, i.e. add edge
            # (uVertex, uVertex) to gt
            neighborKey = neighbor.key
            gT.addEdge(neighborKey, key, weight)

    return gT
