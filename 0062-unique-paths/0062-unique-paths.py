class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            if r == m-1 and c == n-1:
                return 1
            count = 0
            count += dfs(r+1,c)
            count += dfs(r, c+1)

            return count
        
        return dfs(0,0)