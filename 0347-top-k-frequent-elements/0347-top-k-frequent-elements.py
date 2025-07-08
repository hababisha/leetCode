class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        m = Counter(nums)

        for key,val in m.items():
            if len(heap) < k:
                heapq.heappush(heap, (val,key))
            else:
                heapq.heappushpop(heap, (val,key))

        return [h[1] for h in heap]