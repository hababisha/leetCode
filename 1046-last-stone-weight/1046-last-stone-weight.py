class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-i for i in stones]
        heapq.heapify(arr)
        
        while len(arr) > 1:
            s1 = -heapq.heappop(arr)
            s2 = -heapq.heappop(arr)

            if s1 != s2:
                heapq.heappush(arr, -(s1-s2))
        return -arr[0] if arr else 0