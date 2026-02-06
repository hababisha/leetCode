class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (1,0), (-1,0), (0,-1)] 

        def inbound(x,y):
            return 0 <= x < m and 0 <= y < n 
        
        def dfs(x,y):
            if not inbound(x,y) or grid[x][y] == 0:
                return 0
            
            res = grid[x][y]
            grid[x][y] = 0

            best = 0
            for dr, dc in dirs:
                nr, nc = x+dr, y+dc
                best = max(best, dfs(nr,nc))
            grid[x][y] = res


            return res+best


        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                   ans = max(ans, dfs(r,c))
        return ans
                
