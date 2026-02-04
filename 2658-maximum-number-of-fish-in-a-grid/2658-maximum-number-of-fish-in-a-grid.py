class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def dfs(i,j):
            if not inbound(i,j) or grid[i][j] == 0:
                return 0
            res = grid[i][j]
            grid[i][j] = 0

            for dr, dc in dirs:
                nr, nc = dr + i, dc + j
                res +=  dfs(nr, nc)
            return res
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans = max(ans, dfs(r,c))
        return ans



       