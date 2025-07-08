class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            maxx = -heapq.heappop(max_heap)
            reduced = maxx - math.floor(maxx / 2)
            heapq.heappush(max_heap, -reduced)
        
        return -sum(max_heap)
