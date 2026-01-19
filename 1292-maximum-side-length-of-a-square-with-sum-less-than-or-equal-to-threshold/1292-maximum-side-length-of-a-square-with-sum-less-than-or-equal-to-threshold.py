class Solution:
    def maxSideLength(self, grid: List[List[int]], threshold: int) -> int:
        m, n  = len(grid), len(grid[0])
        pref = [[0] * (n+1) for _ in range(m+1)]
        
        for r in range(m):
            for c in range(n):
                pref[r+1][c+1] += pref[r+1][c] + pref[r][c+1] + grid[r][c] - pref[r][c] 


        ans = min(m,n)
        print(pref)
        while ans:
            for i in range(ans, m):
                for j in range(ans, n):
                    left = pref[i][j-ans]
                    top = pref[i-ans][j]
                    topleft = pref[i-ans][j-ans]
                    res = pref[i][j] - left - top + topleft
                    if res <= threshold: return ans
            ans -= 1
        return 0 