class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        heap = []
        ans = []

        for key,v in m.items():
            heapq.heappush(heap, (-v,key))
        
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            ans.append(num)
        return ans