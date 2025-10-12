class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [-1, 0], [0,-1]]
        seen = set()
        fresh, time = 0, 0

        def inbound(x, y):
            return 0 <= x < m and 0 <= y < n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))
                    seen.add((r,c))
                
                if grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                seen.add((x,y))

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in seen or not inbound(nx,ny) or grid[nx][ny] != 1:
                        continue
                    
                    seen.add((nx,ny))
                    q.append((nx,ny))
                    fresh -= 1
                    grid[nx][ny] = 2 
            time += 1
        return time if fresh == 0 else -1