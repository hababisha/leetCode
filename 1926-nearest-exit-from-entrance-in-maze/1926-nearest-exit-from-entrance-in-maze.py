class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        m, n = len(maze), len(maze[0])

        def inbound(nx,ny):
            return 0 <= nx < m and 0 <= ny < n
        while q:
            r,c,h = q.popleft()

            if (r == 0 or c == 0 or r == m-1 or c == n-1) and [r,c] != entrance:
                return h
            
            dirs = [[0,1],[1,0],[-1,0],[0,-1]]

            for dx, dy in dirs:
                nx, ny = dx + r, dy + c

                if inbound(nx,ny)  and maze[nx][ny] == ".":
                    maze[nx][ny] = "+"
                    q.append((nx,ny,h+1))

        return -1