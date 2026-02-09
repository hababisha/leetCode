class Solution:
    def maxMoves(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        memo = [[-1] * COLS for _ in range(ROWS)]
        dirs = (-1, 0, 1)

        def dfs(r, c):
            if memo[r][c] != -1:
                return memo[r][c]

            best = 0
            for dr in dirs:
                nr = r + dr
                nc = c + 1
                if 0 <= nr < ROWS and nc < COLS and grid[nr][nc] > grid[r][c]:
                    best = max(best, 1 + dfs(nr, nc))

            memo[r][c] = best
            return best

        ans = 0
        for r in range(ROWS):
            ans = max(ans, dfs(r, 0))

        return ans
