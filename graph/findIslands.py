# find all islands

def dfs(array, i, j, m, n):

    print("visiting (%d, %d)" %(i,j))

    # mark visited by unsetting
    array[i][j] = 0

    # iterate over 8 neighbors
    for x in [-1,0,1]:
        for y in [-1,0,1]:

            if x == 0 and  y == 0:
                continue

            nx = i + x
            ny = j + y

            if nx <0 or ny <0 or nx >= m or ny >= n:
                continue

            if array[nx][ny] != 0:
                dfs(array, nx, ny, m, n)


if __name__ == "__main__":
    # matrix
    islands = [[1,0,0,0],
            [1,1,0,0],
            [0,0,0,0],
            [1,1,0,0]]

    # finding all connected
    # paths gives the number of
    # islands

    m = len(islands)
    n = len(islands[0])
    total = 0

    for x in range(m):
        for y in range(n):
            if islands[x][y]:
                dfs(islands, x, y, m, n)
                total+=1

    print("total number of islands: %d" %total)
