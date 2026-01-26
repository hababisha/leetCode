class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        ans = 0
        heap = [-a, -b, -c]
        heapq.heapify(heap)
        while len(heap) > 1:
            val1 = heapq.heappop(heap) + 1
            val2 = heapq.heappop(heap) + 1

            ans += 1

            if val1: heapq.heappush(heap,val1)
            if val2: heapq.heappush(heap,val2)
        return ans
        
