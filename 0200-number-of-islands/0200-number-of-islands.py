class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        m, n = len(grid), len(grid[0])
        def inbound(r,c):
            return 0 <= r < m and 0 <= c < n
        

        def dfs(r,c):
            if not inbound(r,c) or grid[r][c] == "0":
                return 0
            grid[r][c] = "0"
            for dr, dc in dirs:
                nr, nc = dr+r, c+dc
                dfs(nr, nc)
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r,c)

        return ans