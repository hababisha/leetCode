class Solution:
  def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    max_area = 0

    def dfs(i,j):
        if i < 0 or i >=m or j < 0 or j >= n or grid[i][j] != 1:
            return
        
        else:
            grid[i][j] = 0
            return 1 + dfs(i, j+1) + dfs(i, j-1) + dfs(i+1, j) + dfs(i-1, j)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i,j))
    
    return max_area
