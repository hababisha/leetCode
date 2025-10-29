class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        summ = sum(candies)
        if summ < k:
            return 0
        ans = -1
        def possible(mid):
            return sum(c // mid for c in candies) >= k
            
        l, r = 1, max(candies)
        while l <= r:
            mid = (r+l)//2

            if possible(mid):
                ans = mid
                l = mid +1
            else:
                r = mid - 1
        
        return ans