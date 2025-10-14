class Solution:
  def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    def inbound(x,y):
        return 0 <= x < m and 0 <= y < n


    def dfs(i, j):
        if not inbound(i,j) or grid[i][j] != 1:
            return 0

        grid[i][j] = 0
        val = 0
        for dr, dc in directions:
            val += dfs(i+dr, j+dc)
        return 1 + val

    maxx = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                maxx = max(maxx, dfs(i,j))

    return maxx