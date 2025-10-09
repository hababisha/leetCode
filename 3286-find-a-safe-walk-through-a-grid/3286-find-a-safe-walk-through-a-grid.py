class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        def inbound(x, y):
            return 0 <= x < m and 0 <= y < n
        
        seen = set()
        heap = [(grid[0][0], 0, 0)]  
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while heap:
            d, i, j = heapq.heappop(heap)

            if i == m - 1 and j == n - 1:
                return d < health

            if (i, j) in seen:
                continue
            seen.add((i, j))

            for dx, dy in dirs:
                nx, ny = i + dx, j + dy
                if not inbound(nx, ny) or (nx, ny) in seen:
                    continue
                nd = d + grid[nx][ny]
                if nd < health:  
                    heapq.heappush(heap, (nd, nx, ny))

        return False
