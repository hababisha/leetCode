

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        M = len(grid)
        
        if grid[0][0] == 1 or grid[M-1][M-1] == 1:
            return -1

        q = deque([(0, 0, 1)])  
        directions = [(0,1), (1,0), (0,-1), (-1,0),
                      (1,1), (-1,-1), (1,-1), (-1,1)]

        grid[0][0] = 1 

        while q:
            r, c, l = q.popleft()

            if r == M - 1 and c == M - 1:
                return l  

            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < M and 0 <= nc < M and grid[nr][nc] == 0:
                    q.append((nr, nc, l + 1))
                    grid[nr][nc] = 1 

        return -1 