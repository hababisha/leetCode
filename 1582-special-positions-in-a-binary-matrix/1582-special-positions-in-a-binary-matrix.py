class Solution:
    def numSpecial(self, grid: List[List[int]]) -> int:
        ans = 0
        m,n = len(grid), len(grid[0])
        rowCount = [0] * m
        colCount = [0] * n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    rowCount[r] += 1
                    colCount[c] += 1
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if rowCount[r] == 1 and colCount[c] == 1:
                        ans += 1
        return ans