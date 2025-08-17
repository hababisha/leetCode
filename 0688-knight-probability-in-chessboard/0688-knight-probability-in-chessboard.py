class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(2,1), (2,-1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]

        def dp(move, x,y):
            if not (0 <= x < n  and 0 <= y < n):
                return 0.0
            if move == k:
                return 1.0

            p = 0.0

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                p += dp(move+1, nx, ny)
            return p / 8.0
        return dp(0, row, column)
