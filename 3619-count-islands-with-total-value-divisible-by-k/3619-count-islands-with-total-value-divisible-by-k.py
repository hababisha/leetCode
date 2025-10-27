class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1], [1, 0], [-1,0], [0,-1]]

        def inbound(r,c):
            return 0 <= r < m and 0 <= c < n
    
        def dfs(r, c):
            if not inbound(r,c) or grid[r][c] == 0:
                return 0
            cur = grid[r][c]
            grid[r][c] = 0
            for dx, dy in dirs:
                nx, ny = dx + r, dy + c
                cur += dfs(nx, ny)
            return cur                


        ans = 0

        for r in range(m):
            for c in range(n):
                if not grid[r][c]:
                    continue
                if dfs(r,c)%k == 0:
                    ans += 1
        return ans