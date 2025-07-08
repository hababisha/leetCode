class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-i for i in nums]

        heapq.heapify(arr)
        
        for _ in range(k):
            val = -heapq.heappop(arr)
        
        return val