class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for x, y in points:
            dis = math.sqrt((x**2) + (y**2))
            heapq.heappush(heap, (dis, [x,y]))
        
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans