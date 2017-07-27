from vertex import Vertex

class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.n = 0

    def addVertex(self, key):
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

def DFS(graph, start):
    def _dfs(start):
        start.visited = True
        print("visited ", start.key)
        for n in start.neighbors.iterkeys():
            if not n.visited:
                _dfs(n)


    if start not in graph.vertices:
        return

    _dfs(graph.vertices[start])
