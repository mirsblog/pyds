# find all islands

"""
If diagonal traversal is allowed:
    diff = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1-1), (1, 1)]
If diagonal traversal is not allowed:
    diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]
"""

def islands(g):
    m = len(g[0])
    n = len(g)

    # visited array
    visited = [[0 for i in range(m)] for j in range(n)]

    def _dfs(vertex):
        y = vertex[0]
        x = vertex[1]

        visited[y][x] = 1
        for diff in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1,
            -1), (1, 1)]:
            ny = y + diff[0]
            nx = x + diff[1]
            if 0 <= ny < n and 0 <= nx < m:
                if g[ny][nx] and not visited[ny][nx]:
                    _dfs((ny, nx))
    t = 0
    for j in range(n):
        for i in range(m):
            if g[j][i] and not visited[j][i]:
                _dfs((j, i))
                t += 1
    return t

if __name__ == "__main__":

    g = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]]
    n = islands(g)
    print(n)
