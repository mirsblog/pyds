from graph import Graph, DFS
from vertex import Vertex

def createGraph():

    g = Graph()
    for key in range(1,11):
        g.addVertex(key)

    g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(2,4)
    g.addEdge(2,5)
    g.addEdge(4,6)
    g.addEdge(3,5)
    g.addEdge(8,9)
    g.addEdge(9,10)

    return g

def createTree():
    g = Graph()
    for key in range(1,8):
        g.addVertex(key)

    g.addEdge(1,2)
    g.addEdge(2,4)
    g.addEdge(1,3)
    g.addEdge(2,5)
    g.addEdge(3,6)
    g.addEdge(3,7)
    
    return g

if __name__ == "__main__":

    # create a graph
    g = createTree()
    DFS(g, 1)
