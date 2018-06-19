# graph traversal in a grid

# bread first search
def bfs(grid):

    # check if grid m x n
    n = len(grid[0])
    for item in grid:
        if len(item) != n:
            raise Exception("grid is not m x n")

    visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    level = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

    q = []
    q.append((0, 0))
    visited[0][0] = 1
    level[0][0] = 0
    p = 0

    while q:
        n = len(q)
        p = p + 1
        while n:
            vertex = q.pop(0)
            n-=1

            y = vertex[0]
            x = vertex[1]

            for diff in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                ny = y + diff[0]
                nx = x + diff[1]
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    if not visited[ny][nx]:
                        q.append((ny, nx))
                        visited[ny][nx] = 1
                        level[ny][nx] = p

    return visited, level

# depth first search
def dfs(grid):
    n = len(grid[0])
    for item in grid:
        if len(item) != n:
            raise Exception("grid is not m x n")

    visited = [[0 for i in range(len(grid[0]))] for k in range(len(grid))]
    depth = [[0 for i in range(len(grid[0]))] for k in range(len(grid))]

    # start at (m, n)
    (m,n) = (1,1)
    visited[m][n] = 1
    depth[m][n] = 0

    def _dfs(vertex):
        y = vertex[0]
        x = vertex[1]
        visited[y][x] = 1

        # call _dfs recursively for each node that hasn't been visited
        for diff in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            ny = y + diff[0]
            nx = x + diff[1]
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                if not visited[ny][nx]:
                    _dfs((ny, nx))

    _dfs((m, n))
    return visited


if __name__ == "__main__":
    grid = [[1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [0, 0, 1, 0, 1]]
    print(bfs(grid))
    print(dfs(grid))
