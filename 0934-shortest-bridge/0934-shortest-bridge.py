class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1,0), (0,1), (-1,0),(0,-1)]
        visit = set()

        def inbound(r,c):
            return 0 <= r < n and 0 <= c < n
        
        def dfs(r,c):
            if not inbound(r,c) or grid[r][c] == 0 or (r,c) in visit:
                return

            visit.add((r,c))
            for dx, dy in dirs:
                nx, ny = r+dx, c + dy
                dfs(nx, ny)
        
        def bfs(r,c):
            ans = 0
            q = deque(visit)
            
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    for dx, dy in dirs:
                        nx, ny = i+dx, j + dy
                        if not inbound(nx,ny) or (nx,ny) in visit:
                            continue
                        
                        if grid[nx][ny]:
                            return ans
                        visit.add((nx,ny))
                        q.append((nx,ny))
                    
                ans += 1

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r,c)
                    return bfs(r,c)

                
                
            
       