class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(m):
            s = 0
            for n in piles:
                s += math.ceil(n/m)
            return s <= h
        l, r = 1, max(piles)
        ans = -1
        while l <= r:
            mid = l + (r-l) // 2
            if helper(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


