class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (1,0), (0,-1), (-1, 0)]

        def inbound(x,y):
            return 0 <= x < m and 0 <= y < n

        def dfs(i,j):
            if not inbound(i,j) or grid[i][j] == "0":
                return 0
            
            grid[i][j] = "0"

            for dx, dy in dirs:
                nx, ny = dx + i, dy + j
                dfs(nx, ny)


        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r,c)

        return ans