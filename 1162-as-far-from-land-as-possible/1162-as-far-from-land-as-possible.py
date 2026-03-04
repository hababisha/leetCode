class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()

        def inbound(i,j):
            return 0 <= i < n and 0 <= j < n
        

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i,j))
        
        if len(q) == 0 or len(q) == n *n:
            return -1
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        dist = -1

        while q:
            dist += 1 
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nr,nc = dr+r, dc+c
                    if inbound(nr,nc) and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr,nc))
        return dist