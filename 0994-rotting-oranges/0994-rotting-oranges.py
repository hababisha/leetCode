class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0

        q = deque()
        m, n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        directions = [[0,1],[0,-1], [-1,0],[1,0]]
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                
                    if nx < 0 or nx == m or ny < 0 or ny == n or grid[nx][ny] != 1:
                        continue
                
                    grid[nx][ny] = 2
                    q.append([nx,ny])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1